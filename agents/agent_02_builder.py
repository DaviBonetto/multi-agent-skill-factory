import logging
import json
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class Agent02Builder:
    """
    Principal Engineer Agent
    Writes the initial draft for a single SKILL.md.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def generate_draft(self, briefing_json: str) -> str:
        system_prompt = f"""
[GOAL]
Você é o Principal Engineer (Agente 2) do Agentic-Skill-Forge.
Sua missão é redigir o conteúdo inicial de um arquivo SKILL.md com base em um briefing estratégico.

[CONTEXT]
Briefing: 
{briefing_json}

[WARNINGS]
- Use Markdown estruturado profissional. Seja técnico, direto e prático.
- Estrutura obrigatória: 
  1. Objetivo
  2. Pré-requisitos
  3. Passo a Passo Técnico / Exemplos de Código
  4. Validação
- Utilize YAML frontmatter apropriado no topo do arquivo com `name` e `description`.

[RETURN]
Retorne APENAS o conteúdo em Markdown. Não use blocos de código (```markdown) em volta do arquivo todo, apenas para scripts/códigos internos.
"""
        logger.info(f"Agent 2: Building draft for briefing...")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a technical writer that outputs only raw markdown content."},
                {"role": "user", "content": system_prompt}
            ],
            temperature=0.4
        )
        
        raw_output = response.choices[0].message.content
        
        # Clean up if the model wrapped it in ```markdown ```
        if raw_output.startswith("```markdown"):
            raw_output = raw_output[11:]
        if raw_output.startswith("```"):
            raw_output = raw_output[3:]
        if raw_output.endswith("```"):
            raw_output = raw_output[:-3]
            
        return raw_output.strip()
