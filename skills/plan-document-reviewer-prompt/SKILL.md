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

    * **Planos incompletos:** Se o plano estiver incompleto, verificar se os principais componentes estão presentes e se há uma estrutura lógica.
    * **Especificações conflitantes:** Se as especificações forem conflitantes, verificar se há uma versão mais recente ou se há necessidade de esclarecimento.
    * **Tarefas mal definidas:** Se as tarefas estiverem mal definidas, verificar se há uma forma clara de executá-las e se há recursos necessários disponíveis.
    * **Problemas de segurança:** Se houver problemas de segurança, verificar se há medidas de segurança adequadas em vigor e se há necessidade de atualização.
    * **Erros de formatação:** Se houver erros de formatação, verificar se o plano está em um formato legível e se há necessidade de correção.
    * **Falta de documentação:** Se houver falta de documentação, verificar se há uma forma clara de acessar a documentação necessária e se há necessidade de criação de documentação adicional.
    * **Dependências não resolvidas:** Se houver dependências não resolvidas, verificar se há uma forma clara de resolver as dependências e se há necessidade de atualização.
    * **Problemas de compatibilidade:** Se houver problemas de compatibilidade, verificar se há uma forma clara de resolver os problemas de compatibilidade e se há necessidade de atualização.

**Reviewer returns:** Status, Issues (if any), Recommendations