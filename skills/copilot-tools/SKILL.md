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
* **Comandos não suportados**: Certifique-se de que os comandos utilizados são suportados pela plataforma e pela versão do Copilot CLI.
* **Limites de recursos**: Tenha em mente os limites de recursos (como memória e processamento) ao executar comandos que consomem muitos recursos.
* **Sessões async**: Ao utilizar sessões async, certifique-se de que os comandos sejam executados corretamente e que os resultados sejam processados adequadamente.
* **Erros de rede**: Verifique se os erros de rede estão sendo tratados corretamente, especialmente ao utilizar comandos que dependem de conexões de rede.
* **Segurança**: Certifique-se de que as credenciais e os dados sensíveis sejam tratados corretamente e de forma segura.
* **Casos de bordo**: Considere os casos de bordo, como quando um comando não retorna um resultado ou quando um erro ocorre durante a execução de um comando.

Além disso, é importante implementar mecanismos de tratamento de erros e exceções para garantir que as skills sejam robustas e confiáveis. Isso pode incluir:

* **Try-catch**: Utilize blocos try-catch para capturar e tratar erros e exceções.
* **Verificação de erros**: Verifique se os comandos retornam erros ou exceções e trate-os adequadamente.
* **Log de erros**: Registre os erros e exceções para que possam ser analisados e resolvidos posteriormente.
* **Recuperação de erros**: Implemente mecanismos de recuperação de erros para garantir que as skills possam se recuperar de erros e exceções.