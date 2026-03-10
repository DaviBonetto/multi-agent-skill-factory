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
    - **Caso de uso não previsto:** Verifique se o implementador lidou corretamente com casos de uso não previstos ou exceções.
    - **Entradas inválidas:** Verifique se o implementador tratou corretamente entradas inválidas ou edge cases.
    - **Condições de erro:** Verifique se o implementador implementou condições de erro e tratamento de exceções de acordo com as especificações.
    - **Segurança:** Verifique se o implementador seguiu as melhores práticas de segurança e se o código é seguro contra vulnerabilidades conhecidas.
    - **Desempenho:** Verifique se o implementador otimizou o código para desempenho e se o código é eficiente em termos de recursos.
    - **Manutenção:** Verifique se o implementador seguiu as melhores práticas de manutenção e se o código é fácil de entender e modificar.
```
Exemplos de edge cases e tratamento de erros que devem ser considerados:
- **Tratamento de erros de rede:** Verifique se o implementador lidou corretamente com erros de rede, como timeouts, conexões perdidas, etc.
- **Tratamento de erros de banco de dados:** Verifique se o implementador lidou corretamente com erros de banco de dados, como queries inválidas, permissões negadas, etc.
- **Tratamento de erros de segurança:** Verifique se o implementador lidou corretamente com erros de segurança, como injeção de SQL, cross-site scripting, etc.
- **Tratamento de erros de desempenho:** Verifique se o implementador lidou corretamente com erros de desempenho, como memoria insuficiente, processamento lento, etc.