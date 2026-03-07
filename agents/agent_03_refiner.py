import logging
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class Agent03Refiner:
    """
    Staff Security & Reliability Engineer Agent
    Improves the initial draft by adding edge-cases and error handling.
    """
    def __init__(self, client: OpenAI, model: str = "llama-3.3-70b-versatile"):
        self.client = client
        self.model = model

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def refine_draft(self, draft_markdown: str) -> str:
        system_prompt = f"""
[GOAL]
Você é o Staff Security & Reliability Engineer (Agente 3).
Sua missão é receber um rascunho de uma skill e reescrevê-la inserindo edge-cases, tratamento de erros e segurança.

[CONTEXT]
Draft atual:
{draft_markdown}

[WARNINGS]
- Mantenha a formatação original em Markdown, principalmente o YAML no topo e títulos legíveis.
- OBRIGATORIAMENTE adicione uma nova seção "⚠️ Tratamento de Exceções e Edge Cases".
- A saída deve ser um arquivo SKILL.md válido.

[RETURN]
Retorne APENAS o texto bruto em Markdown. Nenhuma saudação ou conclusão.
"""
        logger.info("Agent 3: Refining skill draft...")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a technical editor refining raw markdown content."},
                {"role": "user", "content": system_prompt}
            ],
            temperature=0.3
        )
        
        raw_output = response.choices[0].message.content
        
        if raw_output.startswith("```markdown"):
            raw_output = raw_output[11:]
        if raw_output.startswith("```"):
            raw_output = raw_output[3:]
        if raw_output.endswith("```"):
            raw_output = raw_output[:-3]
            
        return raw_output.strip()
