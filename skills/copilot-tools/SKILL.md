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
* **Comandos não suportados**: Verifique se o comando utilizado é suportado pela plataforma e se está sendo utilizado corretamente.
* **Erros de permissão**: Verifique se o usuário tem as permissões necessárias para executar o comando.
* **Limites de recursos**: Verifique se os recursos necessários (como memória ou CPU) estão disponíveis para executar o comando.
* **Conflitos de nomes**: Verifique se os nomes de arquivos ou variáveis não estão conflitando com outros nomes utilizados na sessão.
* **Erros de conexão**: Verifique se a conexão com o servidor ou banco de dados está estabelecida corretamente.
* **Timeouts**: Verifique se os comandos estão sendo executados dentro do tempo limite estabelecido.
* **Erros de parsing**: Verifique se os dados estão sendo parseados corretamente e se os formatos estão sendo respeitados.

Além disso, é importante implementar mecanismos de tratamento de erros e exceções para lidar com situações inesperadas, como:

* **Try-catch**: Utilize blocos try-catch para capturar e tratar erros e exceções.
* **Logging**: Registre os erros e exceções para facilitar a depuração e o diagnóstico.
* **Retornos de erro**: Retorne códigos de erro ou mensagens de erro para indicar que um erro ocorreu.
* **Recuperação**: Implemente mecanismos de recuperação para tentar executar o comando novamente ou para executar uma ação alternativa.