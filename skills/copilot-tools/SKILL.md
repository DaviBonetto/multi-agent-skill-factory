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
* **Comandos não encontrados**: Se um comando não for encontrado, verifique se o nome do comando está correto e se o comando está instalado e configurado corretamente.
* **Erros de permissão**: Verifique se o usuário tem as permissões necessárias para executar os comandos.
* **Limites de recursos**: Verifique se os recursos (como memória e CPU) estão disponíveis para executar os comandos.
* **Conexões de rede**: Verifique se as conexões de rede estão estáveis e se os servidores estão respondendo corretamente.
* **Dados inválidos**: Verifique se os dados sendo passados para os comandos estão válidos e consistentes.
* **Timeouts**: Verifique se os timeouts estão configurados corretamente para evitar que os comandos fiquem pendentes por muito tempo.
* **Dependências**: Verifique se as dependências necessárias estão instaladas e configuradas corretamente.

Além disso, é importante considerar os seguintes edge cases:

* **Comandos com muitos parâmetros**: Verifique se os comandos com muitos parâmetros estão sendo executados corretamente e se os parâmetros estão sendo passados corretamente.
* **Comandos com saídas grandes**: Verifique se os comandos com saídas grandes estão sendo executados corretamente e se as saídas estão sendo processadas corretamente.
* **Comandos que exigem interação**: Verifique se os comandos que exigem interação estão sendo executados corretamente e se a interação está sendo processada corretamente.

Ao considerar esses casos de exceção e edge cases, é possível garantir que as ferramentas do Copilot CLI sejam utilizadas de forma segura e eficaz.