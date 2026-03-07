import json
import logging
from openai import OpenAI
from pydantic import BaseModel
from typing import Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class AuditorResponse(BaseModel):
    batch_status: str
    files_counted: int
    final_go_no_go: bool
    system_message: str

class Agent06Auditor:
    """
    Global System Auditor Agent
    Verifies that the entire loop has completed successfully before initiating a release.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def run_final_audit(self, report_data: Dict[str, Any]) -> AuditorResponse:
        system_prompt = f"""
[GOAL]
Você é o Global System Auditor (Agente 6).
Sua missão é a validação final do pacote diário antes do merge.

[CONTEXT]
Relatório de arquivos gerados no diretório temporário:
{json.dumps(report_data, indent=2)}

[WARNINGS]
- Analise a quantidade de arquivos (esperado: 20 novos).
- Se o número for menor (ex: a API falhou em alguns, mas gerou outros), a flag `final_go_no_go` DEVE SER TRUE SOMENTE se pelo menos 1 skill foi completada (graceful degradation), MAS `batch_status` deve ser "INCOMPLETE" (ou "APPROVED" se 20).
- Se for 0 arquivos, `final_go_no_go` é FALSE.

[RETURN]
Retorne JSON com o schema OBRIGATÓRIO:
{{
  "batch_status": "APPROVED" ou "INCOMPLETE" ou "FAILED",
  "files_counted": NumeroInteiro,
  "final_go_no_go": true ou false,
  "system_message": "Relatório justificado para os logs CI/CD"
}}
"""
        logger.info("Agent 6: Running final global audit of generated assets...")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You strictly output JSON objects."},
                {"role": "user", "content": system_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.1
        )
        
        raw_output = response.choices[0].message.content
        
        try:
            parsed = json.loads(raw_output)
            return AuditorResponse(**parsed)
        except Exception as e:
            logger.error(f"Agent 6 Schema failed validation: {e}")
            raise e
