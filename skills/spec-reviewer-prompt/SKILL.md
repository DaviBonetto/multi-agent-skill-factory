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
    - Spec compliant (if everything matches after code inspection)
    - Issues found: [list specifically what's missing or extra, with file:line references]

    ⚠️ Tratamento de Exceções e Edge Cases
    ---------------------------

    Além das verificações acima, considere os seguintes casos de bordo e exceções:

    * **Código não disponível**: Se o código não estiver disponível para revisão, informe o problema e solicite o código.
    * **Código parcialmente disponível**: Se apenas parte do código estiver disponível, revise a parte disponível e solicite o restante.
    * **Requisitos ambíguos**: Se os requisitos forem ambíguos ou não claros, solicite esclarecimentos antes de proceder com a revisão.
    * **Implementação parcial**: Se a implementação for parcial, verifique se o que foi implementado está correto e solicite a conclusão da implementação.
    * **Erros de compilação**: Se o código não compilar, informe os erros de compilação e solicite correções.
    * **Erros de execução**: Se o código executar com erros, informe os erros de execução e solicite correções.
    * **Segurança**: Verifique se a implementação segue as práticas de segurança adequadas, como validação de entrada, tratamento de erros e proteção contra ataques comuns.
    * **Desempenho**: Verifique se a implementação é eficiente em termos de desempenho, considerando fatores como tempo de execução, uso de memória e recursos.

# Exemplo de Relatório
## Relatório de Revisão
- **Spec compliant**: (se tudo estiver correto)
- **Issues found**: (lista de problemas encontrados, com referèncias de arquivo e linha)
- **Recomendações**: (recomendações para melhorias ou correções)