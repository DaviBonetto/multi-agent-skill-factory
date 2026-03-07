import os
import glob
import logging
import random
from git import Repo
import shutil

logger = logging.getLogger(__name__)

class SkillHarvester:
    """
    Downloads raw external repositories, walks through them, finds .md skills,
    filters them against the local RAG, and outputs a list of ready-to-refine skill strings.
    """
    def __init__(self, local_rag, state_manager):
        self.local_rag = local_rag
        self.state_manager = state_manager
        self.repos = [
            "https://github.com/iaversao7-sketch/skills-master",
            "https://github.com/obra/superpowers",
            "https://github.com/huggingface/skills"
        ]
        self.clone_dir = "/tmp/harvest_repos"

    def harvest(self, max_skills=15) -> list[dict]:
        """
        Returns a list of dictionaries with structure:
        {"title": "Harvester Skill X", "folder_name": "...", "content": "..."}
        """
        self._clone_repos()
        md_files = self._gather_markdown_files()
        
        # Shuffle to get different skills every day
        random.shuffle(md_files)
        
        harvested_skills = []
        
        for file_path in md_files:
            if len(harvested_skills) >= max_skills:
                break
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Skip tiny files or huge files
                if len(content) < 100 or len(content) > 10000:
                    continue
                    
                filename = os.path.basename(file_path)
                folder_name = filename.replace('.md', '').replace(' ', '-')
                
                # Check duplication using existing semantic RAG
                if not self.local_rag.is_duplicate(content):
                    harvested_skills.append({
                        "title": filename,
                        "folder_name": folder_name,
                        "content": content
                    })
                    logger.info(f"Harvester selected unique skill: {filename}")
                else:
                    logger.debug(f"Harvester skipped duplicate skill: {filename}")
                    
            except Exception as e:
                logger.warning(f"Error reading file {file_path}: {e}")
                
        logger.info(f"Harvester successfully collected {len(harvested_skills)} unique raw skills.")
        return harvested_skills
        
    def _clone_repos(self):
        if os.path.exists(self.clone_dir):
            shutil.rmtree(self.clone_dir)
            
        os.makedirs(self.clone_dir, exist_ok=True)
        
        for repo_url in self.repos:
            repo_name = repo_url.split("/")[-1]
            target_path = os.path.join(self.clone_dir, repo_name)
            logger.info(f"Cloning external skills repository: {repo_name}...")
            try:
                Repo.clone_from(repo_url, target_path, depth=1)
            except Exception as e:
                logger.error(f"Failed to clone {repo_url}: {e}")

    def _gather_markdown_files(self):
        logger.info("Scanning cloned repositories for markdown skills...")
        search_pattern = os.path.join(self.clone_dir, "**", "*.md")
        files = glob.glob(search_pattern, recursive=True)
        
        # Filter out READMEs / index files
        valid_files = [f for f in files if not f.lower().endswith("readme.md") and not f.lower().endswith("index.md")]
        return valid_files
