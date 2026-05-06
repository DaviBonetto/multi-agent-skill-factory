# Gemini CLI Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Gemini CLI equivalent |
|-----------------|----------------------|
| `Read` (file reading) | `read_file` |
| `Write` (file creation) | `write_file` |
| `Edit` (file editing) | `replace` |
| `Bash` (run commands) | `run_shell_command` |
| `Grep` (search file content) | `grep_search` |
| `Glob` (search files by name) | `glob` |
| `TodoWrite` (task tracking) | `write_todos` |
| `Skill` tool (invoke a skill) | `activate_skill` |
| `WebSearch` | `google_web_search` |
| `WebFetch` | `web_fetch` |
| `Task` tool (dispatch subagent) | `@agent-name` (see [Subagent support](#subagent-support)) |

## Subagent support

Gemini CLI supports subagents natively via the `@` syntax. Use the built-in `@generalist` agent to dispatch any task — it has access to all tools and follows the prompt you provide.

When a skill says to dispatch a named agent type, use `@generalist` with the full prompt from the skill's prompt template:

| Skill instruction | Gemini CLI equivalent |
|-------------------|----------------------|
| `Task tool (superpowers:implementer)` | `@generalist` with the filled `implementer-prompt.md` template |
| `Task tool (superpowers:spec-reviewer)` | `@generalist` with the filled `spec-reviewer-prompt.md` template |
| `Task tool (superpowers:code-reviewer)` | `@code-reviewer` (bundled agent) or `@generalist` with the filled review prompt |
| `Task tool (superpowers:code-quality-reviewer)` | `@generalist` with the filled `code-quality-reviewer-prompt.md` template |
| `Task tool (general-purpose)` with inline prompt | `@generalist` with your inline prompt |

### Prompt filling

Skills provide prompt templates with placeholders like `{WHAT_WAS_IMPLEMENTED}` or `[FULL TEXT of task]`. Fill all placeholders and pass the complete prompt as the message to `@generalist`. The prompt template itself contains the agent's role, review criteria, and expected output format — `@generalist` will follow it.

### Parallel dispatch

Gemini CLI supports parallel subagent dispatch. When a skill asks you to dispatch multiple independent subagent tasks in parallel, request all of those `@generalist` or named subagent tasks together in the same prompt. Keep dependent tasks sequential, but do not serialize independent subagent tasks just to preserve a simpler history.

## Additional Gemini CLI tools

These tools are available in Gemini CLI but have no Claude Code equivalent:

| Tool | Purpose |
|------|---------|
| `list_directory` | List files and subdirectories |
| `save_memory` | Persist facts to GEMINI.md across sessions |
| `ask_user` | Request structured input from the user |
| `tracker_create_task` | Rich task management (create, update, list, visualize) |
| `enter_plan_mode` / `exit_plan_mode` | Switch to read-only research mode before making changes |

## ⚠️ Tratamento de Exceções e Edge Cases

Ao utilizar as ferramentas do Gemini CLI, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Arquivos não encontrados**: Certifique-se de que os arquivos referenciados existem e estão acessíveis.
* **Permissões insuficientes**: Verifique se você tem as permissões necessárias para executar as ações solicitadas.
* **Parâmetros vazios**: Verifique se os parâmetros obrigatórios estão sendo passados e não estão vazios.
* **Conflitos de nomes**: Evite conflitos de nomes entre arquivos, variáveis e funções.
* **Dependências não resolvidas**: Certifique-se de que todas as dependências necessárias estão resolvidas e disponíveis.
* **Limites de recursos**: Verifique se os recursos disponíveis (como memória e processamento) são suficientes para executar as ações solicitadas.
* **Erros de rede**: Verifique se a conexão de rede está estável e funcional.
* **Timeouts**: Verifique se os timeouts estão configurados corretamente para evitar erros de tempo limite.

Ao lidar com esses casos de exceção e edge cases, é importante:

* **Registrar erros**: Registre os erros e exceções para facilitar a depuração e resolução de problemas.
* **Proporcionar feedback**: Forneça feedback claro e conciso para o usuário sobre o que deu errado e como corrigir o problema.
* **Oferecer soluções**: Ofereça soluções ou alternativas para superar os problemas encontrados.
* **Documentar**: Documente os casos de exceção e edge cases para evitar que eles se repitam no futuro.