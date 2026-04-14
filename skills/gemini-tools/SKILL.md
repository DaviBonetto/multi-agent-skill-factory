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
* **Exceções de tipo**: Ao tentar executar operações, é possível que ocorram exceções de tipo. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Limites de recursos**: Ao tentar executar operações, é possível que os limites de recursos sejam atingidos. Nesse caso, o sistema deve retornar um erro claro e conciso, indicando a causa do problema.
* **Subagentes**: Como o Gemini CLI não suporta subagentes, é importante considerar como as skills que dependem de subagentes serão executadas. Nesse caso, as skills devem ser adaptadas para usar a execução de sessão única via `executing-plans`.

Para lidar com esses casos de exceção e edge cases, é recomendado:

* **Validar inputs**: Validar os inputs antes de executar operações para evitar erros de permissão, arquivos não encontrados, comandos inválidos, exceções de tipo e limites de recursos.
* **Tratar erros**: Tratar erros de forma clara e concisa, retornando mensagens de erro claras e concisas para o usuário.
* **Adaptar skills**: Adaptar skills que dependem de subagentes para usar a execução de sessão única via `executing-plans`.
* **Monitorar recursos**: Monitorar os recursos do sistema para evitar que os limites sejam atingidos.