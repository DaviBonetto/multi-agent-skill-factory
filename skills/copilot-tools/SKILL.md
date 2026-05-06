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

## Tratamento de Exceções e Edge Cases

Ao utilizar as ferramentas do Copilot CLI, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Comandos não suportados**: Certifique-se de que os comandos utilizados são suportados pela plataforma e pela versão do Copilot CLI.
* **Limites de recursos**: Tenha em mente os limites de recursos (como memória e processamento) ao executar comandos que consomem muitos recursos.
* **Conflitos de nome**: Evite conflitos de nome entre variáveis e comandos.
* **Segurança**: Sempre verifique se os comandos estão sendo executados com as permissões necessárias e se os dados estão sendo tratados de forma segura.
* **Timeouts**: Defina timeouts adequados para comandos que podem demorar muito tempo para serem executados.
* **Erros de rede**: Trate erros de rede que podem ocorrer ao executar comandos que dependem de conexões de rede.
* **Dependências**: Verifique se as dependências necessárias estão instaladas e configuradas corretamente.

Além disso, é importante:

* **Testar os comandos**: Teste os comandos antes de executá-los em produção para garantir que eles estão funcionando corretamente.
* **Monitorar os logs**: Monitore os logs para detectar erros ou problemas que possam ocorrer durante a execução dos comandos.
* **Documentar os comandos**: Documente os comandos utilizados e os parâmetros passados para facilitar a depuração e manutenção.