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

    - **Planos vazios ou inexistentes:** Verifique se o arquivo do plano está vazio ou se não existe. Se isso ocorrer, retorne um status de "Issues Found" com uma descrição do problema.
    - **Especificações inconsistentes:** Se a especificação for inconsistente ou contiver erros, retorne um status de "Issues Found" com uma descrição do problema.
    - **Tarefas mal definidas:** Se as tarefas estiverem mal definidas ou forem vagas, retorne um status de "Issues Found" com uma descrição do problema.
    - **Conflitos de dependência:** Verifique se há conflitos de dependência entre as tarefas. Se isso ocorrer, retorne um status de "Issues Found" com uma descrição do problema.
    - **Problemas de segurança:** Verifique se o plano contém problemas de segurança, como a falta de autenticação ou autorização. Se isso ocorrer, retorne um status de "Issues Found" com uma descrição do problema.
    - **Limitações de recursos:** Verifique se o plano está dentro das limitações de recursos, como tempo, orçamento e pessoal. Se isso não ocorrer, retorne um status de "Issues Found" com uma descrição do problema.

**Reviewer returns:** Status, Issues (if any), Recommendations