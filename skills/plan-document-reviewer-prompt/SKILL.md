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

    *   **Planos incompletos:** Se o plano estiver incompleto, verifique se os principais componentes estão presentes, como introdução, objetivos, escopo, cronograma e recursos necessários. Se algum desses componentes estiver faltando, registre como um problema.
    *   **Conflitos de especificação:** Se houver conflitos entre a especificação e o plano, tente resolver esses conflitos antes de aprovar o plano. Se não for possível resolver, registre como um problema.
    *   **Tarefas mal definidas:** Se as tarefas estiverem mal definidas ou forem vagas, tente esclarecer com o autor do plano. Se não for possível esclarecer, registre como um problema.
    *   **Dependências não declaradas:** Verifique se há dependências não declaradas entre as tarefas. Se houver, registre como um problema.
    *   **Riscos não identificados:** Verifique se há riscos não identificados no plano. Se houver, registre como um problema.
    *   **Recursos insuficientes:** Verifique se os recursos necessários para executar o plano estão disponíveis. Se não estiverem, registre como um problema.
    *   **Prazos irrealistas:** Verifique se os prazos estabelecidos no plano são realistas. Se não forem, registre como um problema.
    *   **Comunicação inadequada:** Verifique se a comunicação entre as equipes e stakeholders está clara e eficaz. Se não estiver, registre como um problema.

**Reviewer returns:** Status, Issues (if any), Recommendations