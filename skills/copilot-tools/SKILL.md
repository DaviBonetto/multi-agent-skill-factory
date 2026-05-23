# Copilot CLI Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Copilot CLI equivalent |
|-----------------|----------------------|
| `Read` (file reading) | `view` |
| `Write` (file creation) | `create` |
| `Edit` (file editing) | `edit` |
| `Bash` (run commands) | `bash` |
| `Grep` (search file content) | `grep` |
| `Glob` (search files by name) | `glob` |
| `Skill` tool (invoke a skill) | `skill` |
| `WebFetch` | `web_fetch` |
| `Task` tool (dispatch subagent) | `task` with `agent_type: "general-purpose"` or `"explore"` |
| Multiple `Task` calls (parallel) | Multiple `task` calls |
| Task status/output | `read_agent`, `list_agents` |
| `TodoWrite` (task tracking) | `sql` with built-in `todos` table |
| `WebSearch` | No equivalent — use `web_fetch` with a search engine URL |
| `EnterPlanMode` / `ExitPlanMode` | No equivalent — stay in the main session |

## Async shell sessions

Copilot CLI supports persistent async shell sessions, which have no direct Claude Code equivalent:

| Tool | Purpose |
|------|---------|
| `bash` with `async: true` | Start a long-running command in the background |
| `write_bash` | Send input to a running async session |
| `read_bash` | Read output from an async session |
| `stop_bash` | Terminate an async session |
| `list_bash` | List all active shell sessions |

## Additional Copilot CLI tools

| Tool | Purpose |
|------|---------|
| `store_memory` | Persist facts about the codebase for future sessions |
| `report_intent` | Update the UI status line with current intent |
| `sql` | Query the session's SQLite database (todos, metadata) |
| `fetch_copilot_cli_documentation` | Look up Copilot CLI documentation |
| GitHub MCP tools (`github-mcp-server-*`) | Native GitHub API access (issues, PRs, code search) |

## ⚠️ Tratamento de Exceções e Edge Cases

Ao utilizar as ferramentas do Copilot CLI, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Comandos não suportados**: Verifique se o comando utilizado é suportado pela plataforma e se está sendo utilizado corretamente.
* **Erros de permissão**: Verifique se o usuário tem as permissões necessárias para executar o comando.
* **Erros de rede**: Verifique se a conexão de rede está estável e se o servidor está respondendo corretamente.
* **Timeouts**: Verifique se os timeouts estão configurados corretamente e se os comandos estão sendo executados dentro do tempo limite.
* **Tratamento de erros**: Verifique se os erros estão sendo tratados corretamente e se as mensagens de erro estão sendo exibidas de forma clara e útil.
* **Validação de entrada**: Verifique se as entradas estão sendo validadas corretamente e se os dados estão sendo tratados de forma segura.
* **Segurança**: Verifique se as ferramentas estão sendo utilizadas de forma segura e se os dados estão sendo protegidos contra acessos não autorizados.

Além disso, é importante considerar os seguintes edge cases:

* **Comandos vazios**: Verifique como os comandos vazios são tratados e se eles causam erros ou comportamentos inesperados.
* **Comandos muito longos**: Verifique como os comandos muito longos são tratados e se eles causam erros ou comportamentos inesperados.
* **Caracteres especiais**: Verifique como os caracteres especiais são tratados e se eles causam erros ou comportamentos inesperados.
* **Entradas inválidas**: Verifique como as entradas inválidas são tratadas e se elas causam erros ou comportamentos inesperados.

Ao considerar esses casos de exceção e edge cases, é possível criar skills mais robustas e seguras que possam lidar com uma variedade de situações e cenários.