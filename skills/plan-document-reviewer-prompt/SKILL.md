# Plan Document Reviewer Prompt Template

Use this template when dispatching a plan document reviewer subagent.

**Purpose:** Verify the plan is complete, matches the spec, and has proper task decomposition.

**Dispatch after:** The complete plan is written.

```
Subagent (general-purpose):
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
    | Security | Potential security risks, data protection, and access control |

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

    *   **Arquivos ausentes ou corrompidos:** Verifique se os arquivos `[PLAN_FILE_PATH]` e `[SPEC_FILE_PATH]` existem e estão intactos. Se não, relatar o problema e solicitar os arquivos corretos.
    *   **Especificação incompleta:** Se a especificação for incompleta ou ambígua, relatar o problema e solicitar esclarecimentos.
    *   **Tarefas mal definidas:** Se as tarefas forem mal definidas ou não tiverem claro propósito, relatar o problema e solicitar revisão.
    *   **Riscos de segurança:** Se forem identificados riscos de segurança, relatar o problema e solicitar a implementação de medidas de segurança.
    *   **Limitações de recursos:** Se houver limitações de recursos (tempo, dinheiro, etc.) que afetem a implementação do plano, relatar o problema e solicitar ajustes no plano.
    *   **Dependências externas:** Se o plano depender de fatores externos (terceiros, infraestrutura, etc.), relatar o problema e solicitar um plano de contingência.

**Reviewer returns:** Status, Issues (if any), Recommendations