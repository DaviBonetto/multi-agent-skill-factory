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

Ao utilizar os recursos do Copilot CLI, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Comandos não suportados**: Certifique-se de que os comandos utilizados são suportados pela plataforma e pela versão do Copilot CLI.
* **Erros de permissão**: Verifique se as permissões necessárias estão configuradas corretamente para executar os comandos.
* **Timeouts**: Defina timeouts adequados para os comandos que podem demorar mais tempo para executar.
* **Respostas vazias**: Verifique se as respostas dos comandos estão vazias ou nulas antes de processá-las.
* **Erros de rede**: Verifique se a conexão de rede está estável e se os comandos estão sendo executados corretamente.
* **Limites de recursos**: Verifique se os recursos necessários (como memória, CPU, etc.) estão disponíveis para executar os comandos.
* **Compatibilidade com diferentes sistemas operacionais**: Verifique se os comandos são compatíveis com diferentes sistemas operacionais e versões.

Além disso, é importante implementar tratamento de erros e exceções adequados para lidar com situações inesperadas, como:

* **Try-catch**: Utilize blocos try-catch para capturar e tratar erros e exceções.
* **Logging**: Registre os erros e exceções para facilitar a depuração e o diagnóstico.
* **Recuperação**: Implemente mecanismos de recuperação para lidar com erros e exceções, como retry ou fallback.

Ao considerar esses casos de exceção e edge cases, é possível desenvolver skills mais robustas e confiáveis que possam lidar com situações inesperadas e fornecer uma melhor experiência para os usuários.