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

    * **Planos incompletos:** Se o plano estiver incompleto, verifique se há uma justificativa clara para a falta de informações. Se não houver, registre como um problema.
    * **Especificações conflitantes:** Se as especificações forem conflitantes, verifique se há uma explicação clara para a discrepância. Se não houver, registre como um problema.
    * **Tarefas ambíguas:** Se as tarefas forem ambíguas, verifique se há uma explicação clara para a ambiguidade. Se não houver, registre como um problema.
    * **Erros de formatação:** Se houver erros de formatação no plano, verifique se eles afetam a compreensão do plano. Se sim, registre como um problema.
    * **Falta de recursos:** Se o plano exigir recursos que não estão disponíveis, verifique se há uma justificativa clara para a falta de recursos. Se não houver, registre como um problema.
    * **Dependências não declaradas:** Se o plano depende de outros planos ou recursos que não estão declarados, verifique se há uma explicação clara para a dependência. Se não houver, registre como um problema.
    * **Riscos não identificados:** Se o plano não identificar riscos potenciais, verifique se há uma justificativa clara para a falta de identificação. Se não houver, registre como um problema.
    * **Mudanças não documentadas:** Se houver mudanças no plano que não foram documentadas, verifique se há uma explicação clara para a mudança. Se não houver, registre como um problema.

**Reviewer returns:** Status, Issues (if any), Recommendations