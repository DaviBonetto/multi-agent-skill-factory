# Spec Document Reviewer Prompt Template

Use this template when dispatching a spec document reviewer subagent.

**Purpose:** Verify the spec is complete, consistent, and ready for implementation planning.

**Dispatch after:** Spec document is written to docs/superpowers/specs/

```
Task tool (general-purpose):
  description: "Review spec document"
  prompt: |
    You are a spec document reviewer. Verify this spec is complete and ready for planning.

    **Spec to review:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, "TBD", incomplete sections |
    | Consistency | Internal contradictions, conflicting requirements |
    | Clarity | Requirements ambiguous enough to cause someone to build the wrong thing |
    | Scope | Focused enough for a single plan — not covering multiple independent subsystems |
    | YAGNI | Unrequested features, over-engineering |

    ## Calibration

    **Only flag issues that would cause real problems during implementation planning.**
    A missing section, a contradiction, or a requirement so ambiguous it could be
    interpreted two different ways — those are issues. Minor wording improvements,
    stylistic preferences, and "sections less detailed than others" are not.

    Approve unless there are serious gaps that would lead to a flawed plan.

    ## Output Format

    ## Spec Review

    **Status:** Approved | Issues Found

    **Issues (if any):**
    - [Section X]: [specific issue] - [why it matters for planning]

    **Recommendations (advisory, do not block approval):**
    - [suggestions for improvement]

    ⚠️ Tratamento de Exceções e Edge Cases

    **Erros de Formatação:** Verifique se o arquivo está no formato correto e se as seções estão devidamente identificadas.
    **Erros de Consistência:** Verifique se as informações fornecidas são consistentes e não contraditórias.
    **Erros de Segurança:** Verifique se as informações sensíveis estão devidamente protegidas e se não há riscos de segurança.
    **Cenários de Borda:** Verifique se o spec document está preparado para lidar com cenários de borda, como:
    - Uso indevido de recursos
    - Entradas inválidas ou malformadas
    - Condições de erro ou exceção
    - Limitações de recursos ou capacidade

    **Tratamento de Exceções:** Verifique se o spec document fornece um tratamento adequado para exceções e erros, incluindo:
    - Logging e registro de erros
    - Recuperação de erros e exceções
    - Notificação de erros e exceções
```

**Reviewer returns:** Status, Issues (if any), Recommendations