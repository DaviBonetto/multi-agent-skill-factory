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
    | Security | Potential security vulnerabilities, data protection, access control |
    | Error Handling | Proper error handling mechanisms, logging, and debugging |

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

    *   **Erros de sintaxe:** Verifique se o plano contém erros de sintaxe que possam afetar a implementação.
    *   **Exceções não tratadas:** Verifique se o plano contém exceções não tratadas que possam causar problemas durante a implementação.
    *   **Casos de bordo:** Verifique se o plano considera casos de bordo, como entrada inválida, condições de erro, etc.
    *   **Segurança:** Verifique se o plano considera questões de segurança, como proteção de dados, controle de acesso, etc.
    *   **Desempenho:** Verifique se o plano considera questões de desempenho, como otimização de recursos, tempo de resposta, etc.
    *   **Manutenção:** Verifique se o plano considera questões de manutenção, como atualizações, patches, etc.

    Em caso de exceções ou edge cases, o revisor deve:
    *   **Documentar:** Documentar as exceções ou edge cases encontradas.
    *   **Recomendar:** Recomendar soluções ou melhorias para lidar com as exceções ou edge cases.
    *   **Aprovar:** Aprovar o plano se as exceções ou edge cases não forem críticas.
    *   **Rejeitar:** Rejeitar o plano se as exceções ou edge cases forem críticas e não puderem ser resolvidas.
