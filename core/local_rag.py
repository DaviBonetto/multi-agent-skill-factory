import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

class LocalRAG:
    """
    Local Retrieval-Augmented Generation context generator.
    Parses existing Markdown files and uses TF-IDF to find similarities and summarize context.
    """
    def __init__(self, skills_dir: str):
        self.skills_dir = skills_dir
        self.skills_corpus = []
        self.skills_metadata = []
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = None
        
        self._index_skills()

    def _index_skills(self):
        """Reads all Markdown files and builds the TF-IDF index in memory."""
        logger.info(f"Indexing skills from {self.skills_dir}...")
        
        if not os.path.exists(self.skills_dir):
            logger.warning(f"Skills directory {self.skills_dir} not found. Starting with empty knowledge base.")
            return

        for root, dirs, files in os.walk(self.skills_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # Just getting the title (first line or filename)
                        title = file.replace('.md', '').replace('-', ' ').title()
                        
                        self.skills_metadata.append({
                            "title": title,
                            "path": file_path
                        })
                        self.skills_corpus.append(content)
                    except Exception as e:
                        logger.error(f"Error reading {file_path}: {e}")
        
        if self.skills_corpus:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.skills_corpus)
            logger.info(f"Indexed {len(self.skills_corpus)} skills.")

    def get_existing_skills_summary(self) -> str:
        """Returns a string summarising existing skills for Agent 1 to avoid duplication."""
        # Join all titles to pass as context
        titles = [meta["title"] for meta in self.skills_metadata]
        return json.dumps(titles)

    def is_duplicate(self, proposed_description: str, threshold: float = 0.85) -> bool:
        """
        Check if a proposed skill idea strongly overlaps with an existing one.
        Returns True if a similar skill exists.
        """
        if self.tfidf_matrix is None or not self.skills_corpus:
            return False
            
        proposal_vec = self.vectorizer.transform([proposed_description])
        similarities = cosine_similarity(proposal_vec, self.tfidf_matrix)
        
        max_similarity = similarities[0].max() if len(similarities[0]) > 0 else 0
        if max_similarity > threshold:
            logger.info(f"Duplicate detected! Max similarity: {max_similarity:.2f}")
            return True
            
        return False
