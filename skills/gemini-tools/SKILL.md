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
| `Task` tool (dispatch subagent) | No equivalent — Gemini CLI does not support subagents |

## No subagent support
Gemini CLI has no equivalent to Claude Code's `Task` tool. Skills that rely on subagent dispatch (`subagent-driven-development`, `dispatching-parallel-agents`) will fall back to single-session execution via `executing-plans`.

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

* **Arquivos não encontrados**: Ao utilizar `read_file` ou `write_file`, certifique-se de que o arquivo existe e está acessível. Caso contrário, o sistema pode retornar um erro.
* **Permissões de arquivo**: Ao utilizar `write_file` ou `replace`, certifique-se de que o usuário tem permissão para escrever no arquivo.
* **Comandos inválidos**: Ao utilizar `run_shell_command`, certifique-se de que o comando é válido e não contém erros de sintaxe.
* **Resultados de busca vazios**: Ao utilizar `grep_search` ou `glob`, certifique-se de que o resultado da busca não está vazio.
* **Erros de rede**: Ao utilizar `google_web_search` ou `web_fetch`, certifique-se de que a conexão de rede está estável e funcionando corretamente.
* **Entrada de usuário inválida**: Ao utilizar `ask_user`, certifique-se de que a entrada do usuário é válida e não contém erros de sintaxe.
* **Tarefas duplicadas**: Ao utilizar `tracker_create_task`, certifique-se de que a tarefa não já existe para evitar duplicatas.
* **Modo de plano**: Ao utilizar `enter_plan_mode` ou `exit_plan_mode`, certifique-se de que o modo de plano está sendo utilizado corretamente para evitar erros de execução.

Ao considerar esses casos de exceção e edge cases, é possível garantir que as skills sejam executadas de forma segura e eficaz.