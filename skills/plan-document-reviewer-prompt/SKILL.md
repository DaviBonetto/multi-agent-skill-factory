# Plan Document Reviewer Prompt Template

Use this template when dispatching a plan document reviewer subagent.

**Purpose:** Verify the plan chunk is complete, matches the spec, and has proper task decomposition.

**Dispatch after:** Each plan chunk is written

```
Task tool (general-purpose):
  description: "Review plan chunk N"
  prompt: |
    You are a plan document reviewer. Verify this plan chunk is complete and ready for implementation.

    **Plan chunk to review:** [PLAN_FILE_PATH] - Chunk N only
    **Spec for reference:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, incomplete tasks, missing steps |
    | Spec Alignment | Chunk covers relevant spec requirements, no scope creep |
    | Task Decomposition | Tasks atomic, clear boundaries, steps actionable |
    | File Structure | Files have clear single responsibilities, split by responsibility not layer |
    | File Size | Would any new or modified file likely grow large enough to be hard to reason about as a whole? |
    | Task Syntax | Checkbox syntax (`- [ ]`) on steps for tracking |
    | Chunk Size | Each chunk under 1000 lines |

    ## CRITICAL

    Look especially hard for:
    - Any TODO markers or placeholder text
    - Steps that say "similar to X" without actual content
    - Incomplete task definitions
    - Missing verification steps or expected outputs
    - Files planned to hold multiple responsibilities or likely to grow unwieldy

    ## Output Format

    ## Plan Review - Chunk N

    **Status:** Approved | Issues Found

    **Issues (if any):**
    - [Task X, Step Y]: [specific issue] - [why it matters]

    **Recommendations (advisory):**
    - [suggestions that don't block approval]

    ⚠️ Tratamento de Exceções e Edge Cases

    - **Erros de Formatação:** Verifique se o arquivo de plano está no formato correto e se as seções estão bem definidas. Se houver erros de formatação, relatar como um problema.
    - **Arquivos Ausentes:** Verifique se todos os arquivos referenciados no plano estão presentes e acessíveis. Se um arquivo estiver ausente, relatar como um problema.
    - **Conflitos de Versão:** Verifique se há conflitos de versão entre os arquivos do plano e as dependências. Se houver conflitos, relatar como um problema.
    - **Segurança:** Verifique se o plano contém informações sensíveis ou vulnerabilidades de segurança. Se houver problemas de segurança, relatar como um problema crítico.
    - **Limites de Tamanho:** Verifique se o tamanho do chunk está dentro do limite de 1000 linhas. Se estiver acima do limite, relatar como um problema.
    - **Dependências Desatualizadas:** Verifique se as dependências utilizadas no plano estão atualizadas e seguras. Se houver dependências desatualizadas, relatar como um problema.
    - **Caminhos de Arquivos Incorretos:** Verifique se os caminhos de arquivos utilizados no plano estão corretos e absolutos. Se houver caminhos incorretos, relatar como um problema.

**Reviewer returns:** Status, Issues (if any), Recommendations