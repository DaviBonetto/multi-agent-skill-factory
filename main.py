import os
import sys
import logging
from dotenv import load_dotenv
from openai import OpenAI

# Core
from core.rate_limiter import RateLimiter
from core.local_rag import LocalRAG
from core.state_manager import StateManager

# Agents
from agents.agent_01_planner import Agent01Planner
from agents.agent_02_builder import Agent02Builder
from agents.agent_03_refiner import Agent03Refiner
from agents.agent_04_validator import Agent04Validator
from agents.agent_05_integrator import Agent05Integrator
from agents.agent_06_auditor import Agent06Auditor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("GROQ_API_KEY environment variable not set!")
        sys.exit(1)

    # Configure Groq client through OpenAI SDK
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

    models_config = {
        "planner": "llama-3.3-70b-versatile",
        "builder": "llama-3.3-70b-versatile",
        "refiner": "llama-3.3-70b-versatile",
        "validator": "llama-3.3-70b-versatile",
        "integrator": "llama-3.3-70b-versatile",
        "auditor": "llama-3.3-70b-versatile"
    }

    # Initialize Core
    rate_limiter = RateLimiter(max_requests=30, time_window=60.0)
    
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    skills_dir = os.environ.get("SKILLS_DIR", os.path.join(workspace_root, "skills"))
    
    local_rag = LocalRAG(skills_dir=skills_dir)
    state_manager = StateManager(tmp_dir="/tmp/agentic_skills_run")
    
    # Initialize Agents
    a1_planner = Agent01Planner(client, model=models_config["planner"])
    a2_builder = Agent02Builder(client, model=models_config["builder"])
    a3_refiner = Agent03Refiner(client, model=models_config["refiner"])
    a4_validator = Agent04Validator(client, model=models_config["validator"])
    a5_integrator = Agent05Integrator(client, model=models_config["integrator"])
    a6_auditor = Agent06Auditor(client, model=models_config["auditor"])

    # --- WAVE 1: Planning ---
    existing_skills_summary = local_rag.get_existing_skills_summary()
    
    briefings = state_manager.load_briefings()
    if not briefings:
        rate_limiter.wait_if_needed()
        planner_response = a1_planner.generate_briefings(existing_skills_summary)
        rate_limiter.add_delay()
        
        briefings_list = []
        for b in planner_response.briefings:
            # Anti-duplication check
            if not local_rag.is_duplicate(b.description):
                briefings_list.append(b.model_dump())
            else:
                logger.info(f"Skipping duplicate proposal: {b.title}")
                
        # Protect Free Groq Accounts from hitting the 100,000 Tokens Per Day (TPD) Limit instantly
        briefings = briefings_list[:5]
        state_manager.save_briefings(briefings)
        logger.info(f"Wave 1 Complete: {len(briefings)} unique briefings ready.")

    # --- WAVE 2: The Factory ---
    for b in briefings:
        skill_name = b["folder_name"]

        # Let's just catch any Exception inside the Factory Loop to allow graceful death
        try:
            # 1. Builder
            draft = state_manager.load_skill_draft(skill_name, "builder_draft")
            if not draft:
                rate_limiter.wait_if_needed()
                draft = a2_builder.generate_draft(str(b))
                rate_limiter.add_delay()
                state_manager.save_skill_draft(skill_name, "builder_draft", draft)

            # 2. Refiner
            refined = state_manager.load_skill_draft(skill_name, "refiner_draft")
            if not refined:
                rate_limiter.wait_if_needed()
                refined = a3_refiner.refine_draft(draft)
                rate_limiter.add_delay()
                state_manager.save_skill_draft(skill_name, "refiner_draft", refined)

            # 3. Validator (QA via loop)
            qa_status = "FAIL"
            attempts = 0
            max_attempts = 2  # Hard limit to avoid blowing tokens on one bad idea
            final_markdown = refined
            
            while qa_status == "FAIL" and attempts < max_attempts:
                attempts += 1
                rate_limiter.wait_if_needed()
                validation_result = a4_validator.validate_skill(final_markdown)
                rate_limiter.add_delay()
                
                qa_status = validation_result.status
                if qa_status == "PASS":
                    final_markdown = validation_result.fixed_markdown
                else:
                    logger.warning(f"Validation failed for {skill_name} on attempt {attempts}. Reason: {validation_result.reasoning}")
                    if validation_result.fixed_markdown:
                        final_markdown = validation_result.fixed_markdown

            if qa_status == "PASS" and final_markdown:
                state_manager.mark_skill_completed(skill_name, final_markdown)
            else:
                logger.error(f"Skill {skill_name} failed final validation and was discarded.")

        except Exception as e:
            if "Rate limit reached" in str(e) or "429" in str(e):
                logger.warning(f"Tokens Per Day Limit Hit during Wave 2! Breaking loop early: {str(e)}")
                break
            else:
                logger.error(f"Unhandled error for skill {skill_name}: {str(e)}")
                continue

    # --- WAVE 3: Integration ---
    report_data = state_manager.get_tmp_size_report()
    
    rate_limiter.wait_if_needed()
    audit_response = a6_auditor.run_final_audit(report_data)
    rate_limiter.add_delay()
    
    if audit_response.final_go_no_go:
        logger.info(f"Auditor APPROVED the batch. Message: {audit_response.system_message}")
        
        # In a real environment, this is where we copy files from /tmp_skills/ready_for_commit to real skills_dir
        # And then the bash script handles the git push.
        # Let's generate the commit message for the CI environment to pick up
        
        # We'll just generate a single commit message for the batch to save API calls
        rate_limiter.wait_if_needed()
        commit_msg = a5_integrator.generate_commit_message("Daily Auto-Generated Skills Batch", audit_response.system_message)
        
        # Export commit message so the CI/CD script can use it
        with open("/tmp/agentic_skills_run/commit_msg.txt", "w", encoding="utf-8") as f:
            f.write(commit_msg)
            
        logger.info("Pipeline Complete! Files ready in /tmp/agentic_skills_run/ready_for_commit/")
    else:
        logger.error(f"Auditor REJECTED the batch. Message: {audit_response.system_message}")
        sys.exit(1)

if __name__ == "__main__":
    main()
