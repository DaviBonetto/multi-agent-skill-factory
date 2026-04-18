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

* **Erros de permissão**: Ao tentar ler ou escrever arquivos, é possível que ocorram erros de permissão. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Arquivos não encontrados**: Ao tentar ler ou escrever arquivos, é possível que o arquivo não seja encontrado. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Comandos inválidos**: Ao tentar executar comandos, é possível que o comando seja inválido. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Limites de recursos**: Ao tentar executar comandos ou acessar arquivos, é possível que os recursos do sistema sejam limitados. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Subagent dispatch**: Como o Gemini CLI não suporta subagent dispatch, é importante considerar como as skills que dependem dessa funcionalidade serão afetadas. Nesse caso, as skills devem ser adaptadas para usar a execução de planos em vez de subagent dispatch.

Além disso, é importante considerar as seguintes medidas de segurança:

* **Validação de entrada**: Todas as entradas de usuário devem ser validadas para evitar ataques de injeção de código ou outros tipos de ataques.
* **Autenticação e autorização**: Todas as ações que requerem autenticação e autorização devem ser protegidas por mecanismos de segurança adequados.
* **Criptografia**: Todas as comunicações que requerem criptografia devem ser protegidas por mecanismos de criptografia adequados.

Ao considerar esses casos de exceção e edge cases, é possível criar skills mais robustas e seguras que possam ser utilizadas em uma variedade de situações.