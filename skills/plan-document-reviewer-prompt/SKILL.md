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

    - **Planos vazios ou inexistentes:** Verifique se o plano está vazio ou se o arquivo não existe. Se isso ocorrer, retorne um erro indicando que o plano não está disponível para revisão.
    - **Especificações inconsistentes:** Se a especificação for inconsistente ou contenha erros, verifique se o plano consegue lidar com essas inconsistências. Se não, indique isso como um problema.
    - **Tarefas mal definidas:** Se as tarefas estiverem mal definidas ou forem muito vagas, indique isso como um problema, pois pode causar dificuldades durante a implementação.
    - **Dependências não declaradas:** Verifique se há dependências não declaradas entre as tarefas. Se encontrar, indique isso como um problema, pois pode afetar a ordem de execução das tarefas.
    - **Erros de formatação:** Se o plano contiver erros de formatação que possam afetar a legibilidade ou a compreensão do plano, indique isso como um problema.
    - **Segurança:** Verifique se o plano contém informações sensíveis ou se há riscos de segurança associados à implementação do plano. Se encontrar, indique isso como um problema e forneça recomendações para mitigar esses riscos.

**Reviewer returns:** Status, Issues (if any), Recommendations