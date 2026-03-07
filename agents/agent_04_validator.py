import json
import logging
from openai import OpenAI
from pydantic import BaseModel
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class ValidatorResponse(BaseModel):
    status: str
    reasoning: str
    fixed_markdown: str

class Agent04Validator:
    """
    Tech Lead Reviewer / QA Agent
    Reviews the refined draft and outputs PASS or FAIL along with fixes.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def validate_skill(self, refined_markdown: str) -> ValidatorResponse:
        system_prompt = f"""
[GOAL]
Você é o Tech Lead Revisor (Agente 4).
Sua missão é auditar o SKILL.md final. Se encontrar falhas arquiteturais, erros ou alucinações graves, reprove. Se sólido, aprove.

[CONTEXT]
Arquivo para revisão:
{refined_markdown}

[WARNINGS]
- Seja rigoroso. A skill deve estar pronta para um ambiente de produção (Senior level).
- Status deve ser "PASS" se for adequado, ou "FAIL" caso o markdown falhe em ser direto, coeso ou exiba código com falhas notórias.
- Se for FAIL, a propriedade 'fixed_markdown' deve conter a versão corrigida (se for possível corrigir facilmente). Caso não consiga, devolva a string vazia ou o markdown da forma que conseguiu salvar.
- Se for PASS, repita o markdown original em 'fixed_markdown'.
- RETORNE APENAS JSON. Nenhuma palavra a mais.

[RETURN]
Retorne API JSON com o schema exato:
{{
  "status": "PASS" ou "FAIL",
  "reasoning": "Breve justificativa",
  "fixed_markdown": "... conteudo final stringified ..."
}}
"""
        logger.info("Agent 4: Validating skill draft (QA) pass or fail...")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a QA bot that outputs strictly JSON."},
                {"role": "user", "content": system_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        raw_output = response.choices[0].message.content
        
        try:
            parsed = json.loads(raw_output)
            return ValidatorResponse(**parsed)
        except Exception as e:
            logger.error(f"Agent 4 Schema failed to parse: {e}")
            raise e
