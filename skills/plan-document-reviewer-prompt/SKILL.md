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

    *   **Planos incompletos:** Se o plano estiver incompleto, verifique se há uma justificativa clara para a falta de informações. Se não houver, solicite mais detalhes antes de aprovar.
    *   **Specs desatualizados:** Se a especificação estiver desatualizada, verifique se o plano está alinhado com a versão mais recente da especificação. Se não estiver, solicite atualizações antes de aprovar.
    *   **Tarefas ambíguas:** Se as tarefas forem ambíguas ou não tiverem claro escopo, solicite esclarecimentos antes de aprovar.
    *   **Dependências não declaradas:** Verifique se há dependências não declaradas entre tarefas ou componentes. Se houver, solicite que sejam documentadas antes de aprovar.
    *   **Riscos não identificados:** Verifique se há riscos não identificados no plano. Se houver, solicite que sejam avaliados e mitigados antes de aprovar.
    *   **Conflitos de interesses:** Verifique se há conflitos de interesses entre as partes envolvidas no plano. Se houver, solicite que sejam resolvidos antes de aprovar.
    *   **Comunicação ineficaz:** Verifique se a comunicação entre as partes envolvidas no plano é clara e eficaz. Se não for, solicite melhorias antes de aprovar.
    *   **Mudanças não documentadas:** Verifique se há mudanças no plano que não foram documentadas. Se houver, solicite que sejam documentadas antes de aprovar.
    *   **Falta de recursos:** Verifique se há falta de recursos (humanos, materiais, financeiros) para executar o plano. Se houver, solicite que sejam alocados antes de aprovar.
    *   **Prazos não realistas:** Verifique se os prazos estabelecidos no plano são realistas. Se não forem, solicite que sejam ajustados antes de aprovar.

**Reviewer returns:** Status, Issues (if any), Recommendations