# Plan Document Reviewer Prompt Template

Use this template when dispatching a plan document reviewer subagent.

**Purpose:** Verify the plan is complete, matches the spec, and has proper task decomposition.

**Dispatch after:** The complete plan is written.

```
Task tool (general-purpose):
  description: "Review plan document"
  prompt: |
    You are a plan document reviewer. Verify this plan is complete and ready for implementation.

    **Plan to review:** [PLAN_FILE_PATH]
    **Spec for reference:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, incomplete tasks, missing steps |
    | Spec Alignment | Plan covers spec requirements, no major scope creep |
    | Task Decomposition | Tasks have clear boundaries, steps are actionable |
    | Buildability | Could an engineer follow this plan without getting stuck? |

    ## Calibration

    **Only flag issues that would cause real problems during implementation.**
    An implementer building the wrong thing or getting stuck is an issue.
    Minor wording, stylistic preferences, and "nice to have" suggestions are not.

    Approve unless there are serious gaps — missing requirements from the spec,
    contradictory steps, placeholder content, or tasks so vague they can't be acted on.

    ## Output Format

    ## Plan Review

    **Status:** Approved | Issues Found

    **Issues (if any):**
    - [Task X, Step Y]: [specific issue] - [why it matters for implementation]

    **Recommendations (advisory, do not block approval):**
    - [suggestions for improvement]

    ⚠️ Tratamento de Exceções e Edge Cases

    *   **Planos incompletos:** Se o plano estiver incompleto, verifique se há uma justificativa clara para a falta de informações. Se não houver, registre como um problema.
    *   **Especificações conflitantes:** Se as especificações forem conflitantes, tente resolver o conflito com base nas informações disponíveis. Se não for possível, registre como um problema.
    *   **Tarefas mal definidas:** Se as tarefas estiverem mal definidas, tente esclarecer as instruções. Se não for possível, registre como um problema.
    *   **Problemas de segurança:** Se houver problemas de segurança identificados no plano, registre como um problema crítico.
    *   **Limitações de recursos:** Se o plano exigir recursos que não estão disponíveis, registre como um problema.
    *   **Dependências não resolvidas:** Se houver dependências não resolvidas no plano, registre como um problema.
    *   **Riscos não mitigados:** Se houver riscos não mitigados no plano, registre como um problema.
    *   **Mudanças não documentadas:** Se houver mudanças no plano que não foram documentadas, registre como um problema.
    *   **Falta de testes:** Se o plano não incluir testes adequados, registre como um problema.
    *   **Problemas de escalabilidade:** Se o plano não for escalável, registre como um problema.
    *   **Problemas de manutenção:** Se o plano não for fácil de manter, registre como um problema.

**Reviewer returns:** Status, Issues (if any), Recommendations