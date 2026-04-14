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

    **Cenários de Erro:**
    - Planos vazios ou inexistentes: Verifique se o arquivo do plano está presente e não está vazio.
    - Especificações ausentes: Certifique-se de que as especificações estejam disponíveis e acessíveis.
    - Tarefas mal definidas: Verifique se as tarefas têm metas claras e estão bem decompostas.
    - Conflitos de dependência: Identifique possíveis conflitos entre tarefas ou dependências.

    **Tratamento de Exceções:**
    - Se o plano estiver vazio ou inexistente, retorne um erro e solicite que o plano seja revisado.
    - Se as especificações estiverem ausentes, solicite que as especificações sejam fornecidas antes de prosseguir.
    - Se as tarefas estiverem mal definidas, solicite que as tarefas sejam revisadas e melhoradas.
    - Se houver conflitos de dependência, identifique e documente os conflitos e sugira soluções.

    **Segurança:**
    - Verifique se o plano contém informações confidenciais ou sensíveis e certifique-se de que elas estejam devidamente protegidas.
    - Certifique-se de que as tarefas e os passos estejam alinhados com as políticas de segurança da organização.

**Reviewer returns:** Status, Issues (if any), Recommendations