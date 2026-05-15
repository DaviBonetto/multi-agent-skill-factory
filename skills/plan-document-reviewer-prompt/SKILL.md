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

    *   **Planos incompletos:** Se o plano estiver incompleto ou faltar informações essenciais, o revisor deve solicitar mais detalhes antes de aprovar.
    *   **Conflitos de especificação:** Se houver conflitos entre a especificação e o plano, o revisor deve identificar e documentar esses conflitos para resolução.
    *   **Tarefas ambíguas:** Se as tarefas forem ambíguas ou não estiverem claramente definidas, o revisor deve solicitar esclarecimentos antes de aprovar.
    *   **Dependências não declaradas:** Se houver dependências não declaradas entre tarefas ou componentes, o revisor deve identificar e documentar essas dependências para garantir a integridade do plano.
    *   **Riscos de segurança:** Se o plano apresentar riscos de segurança, como a falta de autenticação ou autorização adequadas, o revisor deve destacar esses riscos e recomendar mitigações.
    *   **Compliance regulatória:** Se o plano não atender aos requisitos regulatórios aplicáveis, o revisor deve identificar as lacunas e recomendar ações corretivas.

**Reviewer returns:** Status, Issues (if any), Recommendations