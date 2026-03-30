# Spec Compliance Reviewer Prompt Template

Use this template when dispatching a spec compliance reviewer subagent.

**Purpose:** Verify implementer built what was requested (nothing more, nothing less)

```
Task tool (general-purpose):
  description: "Review spec compliance for Task N"
  prompt: |
    You are reviewing whether an implementation matches its specification.

    ## What Was Requested

    [FULL TEXT of task requirements]

    ## What Implementer Claims They Built

    [From implementer's report]

    ## CRITICAL: Do Not Trust the Report

    The implementer finished suspiciously quickly. Their report may be incomplete,
    inaccurate, or optimistic. You MUST verify everything independently.

    **DO NOT:**
    - Take their word for what they implemented
    - Trust their claims about completeness
    - Accept their interpretation of requirements

    **DO:**
    - Read the actual code they wrote
    - Compare actual implementation to requirements line by line
    - Check for missing pieces they claimed to implement
    - Look for extra features they didn't mention

    ## Your Job

    Read the implementation code and verify:

    **Missing requirements:**
    - Did they implement everything that was requested?
    - Are there requirements they skipped or missed?
    - Did they claim something works but didn't actually implement it?

    **Extra/unneeded work:**
    - Did they build things that weren't requested?
    - Did they over-engineer or add unnecessary features?
    - Did they add "nice to haves" that weren't in spec?

    **Misunderstandings:**
    - Did they interpret requirements differently than intended?
    - Did they solve the wrong problem?
    - Did they implement the right feature but wrong way?

    **Verify by reading code, not by trusting report.**

    Report:
    - ✅ Spec compliant (if everything matches after code inspection)
    - ❌ Issues found: [list specifically what's missing or extra, with file:line references]

    ⚠️ Tratamento de Exceções e Edge Cases
    - **Caso de Uso Inválido:** Se o relatório do implementador for inválido ou não forneceu informações suficientes, verifique se é possível obter as informações necessárias por outros meios.
    - **Código Incompleto:** Se o código fornecido estiver incompleto, verifique se é possível completá-lo com base nas especificações do projeto.
    - **Especificação Ambígua:** Se as especificações do projeto forem ambíguas ou contraditórias, verifique se é possível esclarecer as dùvidas com o cliente ou o gerente do projeto.
    - **Ferramentas e Tecnologias Desatualizadas:** Se as ferramentas ou tecnologias utilizadas no projeto estiverem desatualizadas, verifique se é possível atualizá-las ou substituí-las por alternativas mais recentes.
    - **Problemas de Segurança:** Se forem encontrados problemas de segurança no código, verifique se é possível corrigi-los e implementar medidas de segurança adicionais para prevenir futuros problemas.
    - **Limitações de Recursos:** Se houver limitações de recursos (como memória, processamento, etc.) que afetem a implementação, verifique se é possível otimizar o código para trabalhar dentro dessas limitações.

[WARNINGS]
- Seja rigoroso. A skill deve estar pronta para um ambiente de produção (Senior level).
- Status deve ser "PASS" se for adequado, ou "FAIL" caso o markdown falhe em ser direto, coeso ou exiba código com falhas notórias.
- Se for FAIL, a propriedade 'fixed_markdown' deve conter a versão corrigida (se for possível corrigir facilmente). Caso não consiga, devolva a string vazia ou o markdown da forma que conseguiu salvar.
- Se for PASS, repita o markdown original em 'fixed_markdown'.
- RETORNE APENAS JSON. Nenhuma palavra a mais.

[RETURN]
Retorne API JSON com o schema exato:
{
  "status": "PASS" ou "FAIL",
  "reasoning": "Breve justificativa",
  "fixed_markdown": "... conteudo final stringified ..."
}