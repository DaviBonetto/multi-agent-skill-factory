import json
import logging
from openai import OpenAI
from pydantic import BaseModel, ConfigDict
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

# Pydantic schema for strict JSON response from Agent 1
class SkillBriefing(BaseModel):
    folder_name: str
    title: str
    description: str
    complexity: str
    
class PlannerResponse(BaseModel):
    briefings: list[SkillBriefing]

class Agent01Planner:
    """
    Orquestrador / Planner Agent 
    Generates 20 unique skill briefings based on the existing skills corpus.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def generate_briefings(self, existing_skills_json: str) -> PlannerResponse:
        system_prompt = f"""
[GOAL]
Você é o Chief AI Planner (Agente 1) do Agentic-Skill-Forge.
Sua missão é gerar exatamente 20 briefings inéditos para novas habilidades (skills) técnicas avançadas.

[CONTEXT]
Abaixo está a lista de títulos das skills já existentes (para evitar duplicação):
{existing_skills_json}
Foco: Engenharia de Software, DevOps, Multi-Agentes, Segurança, Dados, Arquitetura de Sistemas, e Ferramentas modernas de IA.

[WARNINGS]
- PROIBIDO sugerir temas já listados no contexto ou skills não-técnicas.
- Você OBRIGATORIAMENTE deve retornar APENAS um objeto JSON. Sem introduções.

[RETURN]
Retorne este schema exato:
{{
  "briefings": [
    {{
      "folder_name": "Nome-da-Skill-Com-Hifens",
      "title": "Título legível",
      "description": "O que esta skill ensina ou automatiza",
      "complexity": "Senior"
    }}
  ]
}}
"""
        logger.info("Agent 1: Requesting 20 new skill briefings from Groq...")
        
        # We enforce JSON mode if the model supports it, but currently the prompt heavily instructs for JSON
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that strictly outputs JSON."},
                {"role": "user", "content": system_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        
        raw_output = response.choices[0].message.content
        logger.debug(f"Agent 1 Payload: {raw_output}")
        
        # Validate and return parsed object
        try:
            parsed = json.loads(raw_output)
            return PlannerResponse(**parsed)
        except Exception as e:
            logger.error(f"Agent 1 Output structure validation failed: {e}")
            raise e
