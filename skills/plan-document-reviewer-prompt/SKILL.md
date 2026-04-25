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

    *   **Planos vazios ou inexistentes:** Verifique se o plano está vazio ou se o arquivo não existe. Se for o caso, retorne um erro com a mensagem "Plano vazio ou inexistente".
    *   **Especificações ausentes:** Verifique se as especificações estão disponíveis. Se não estiverem, retorne um erro com a mensagem "Especificações ausentes".
    *   **Tarefas mal definidas:** Verifique se as tarefas estão bem definidas e se os passos são claros. Se não estiverem, retorne um erro com a mensagem "Tarefas mal definidas".
    *   **Inconsistências:** Verifique se há inconsistências no plano, como tarefas contraditórias ou passos que não seguem a lógica. Se encontrar alguma inconsistência, retorne um erro com a mensagem "Inconsistência no plano".
    *   **Segurança:** Verifique se o plano contém informações sensíveis ou se há riscos de segurança. Se encontrar algum risco, retorne um erro com a mensagem "Risco de segurança detectado".
    *   **Erros de formatação:** Verifique se o plano está formatado corretamente e se não há erros de sintaxe. Se encontrar algum erro, retorne um erro com a mensagem "Erro de formatação".

**Reviewer returns:** Status, Issues (if any), Recommendations