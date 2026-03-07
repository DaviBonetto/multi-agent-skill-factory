import logging
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class Agent05Integrator:
    """
    DevOps Release Manager Agent
    Generates standard conventional commit messages based on generated skills.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def generate_commit_message(self, skill_title: str, skill_desc: str) -> str:
        system_prompt = f"""
[GOAL]
Você é o DevOps Release Manager (Agente 5).
Sua missão é gerar mensagens de commit semânticas (Conventional Commits).

[CONTEXT]
Título: {skill_title}
Descrição: {skill_desc}

[WARNINGS]
- OBRIGATÓRIO usar o padrão: feat(categoria): escopo em letras minúsculas.
- Adicione um corpo de commit explicando o impacto da inclusão desta skill no repositório.
- A mensagem deve ser concisa e profissional.

[RETURN]
Retorne apenas o texto exato do commit (com quebras de linha se necessário). SEM MARCADORES (```).
"""
        logger.info("Agent 5: Generating commit message...")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You output only the plain commit message text."},
                {"role": "user", "content": system_prompt}
            ],
            temperature=0.2
        )
        
        raw_output = response.choices[0].message.content
        
        if raw_output.startswith("```"):
            raw_output = "\n".join(raw_output.split("\n")[1:-1])
            
        return raw_output.strip()
