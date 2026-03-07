import os
import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class StateManager:
    """
    Handles tracking state in the filesystem (/tmp_skills/) to ensure the CI/CD 
    doesn't lose data if it crashes partway through the loop.
    """
    def __init__(self, tmp_dir: str = "/tmp/agentic_skills"):
        self.tmp_dir = tmp_dir
        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir, exist_ok=True)
            logger.info(f"Created ephemeral directory: {self.tmp_dir}")

    def save_briefings(self, briefings: List[Dict[str, Any]]):
        """Saves the generated 20 briefings (from Agent 1) to disk."""
        path = os.path.join(self.tmp_dir, "briefings_state.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(briefings, f, indent=2)
            
    def load_briefings(self) -> List[Dict[str, Any]]:
        """Loads briefings if resuming."""
        path = os.path.join(self.tmp_dir, "briefings_state.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_skill_draft(self, skill_name: str, step: str, content: str):
        """
        Saves a skill at a specific stage: builder_draft, refiner_draft, final_validator
        """
        skill_dir = os.path.join(self.tmp_dir, skill_name)
        os.makedirs(skill_dir, exist_ok=True)
        
        file_path = os.path.join(skill_dir, f"{step}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def load_skill_draft(self, skill_name: str, step: str) -> str:
        """Loads a draft to resume process."""
        file_path = os.path.join(self.tmp_dir, skill_name, f"{step}.md")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def mark_skill_completed(self, skill_name: str, final_markdown: str):
        """Saves the fully validated skill ready for deployment."""
        skill_dir = os.path.join(self.tmp_dir, "ready_for_commit")
        os.makedirs(skill_dir, exist_ok=True)
        
        file_path = os.path.join(skill_dir, f"{skill_name}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_markdown)
        logger.info(f"Marked skill {skill_name} as COMPLETED and ready.")

    def get_ready_skills(self) -> List[str]:
        """Returns the list of skills that were fully validated."""
        skill_dir = os.path.join(self.tmp_dir, "ready_for_commit")
        if not os.path.exists(skill_dir):
            return []
            
        return [os.path.join(skill_dir, f) for f in os.listdir(skill_dir) if f.endswith('.md')]

    def get_tmp_size_report(self) -> Dict[str, Any]:
        """Provides an inventory of successfully processed files for Agent 6 (Auditor)."""
        ready_files = self.get_ready_skills()
        report = []
        for file in ready_files:
            size_kb = os.path.getsize(file) / 1024
            name = os.path.basename(file)
            report.append(f"{name} ({size_kb:.2f} KB)")
            
        return {
            "ready_count": len(ready_files),
            "files": report
        }
