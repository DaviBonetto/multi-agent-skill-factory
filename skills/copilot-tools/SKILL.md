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
* **Comandos não suportados**: Certifique-se de que os comandos utilizados são suportados pelo Copilot CLI e que as versões são compatíveis.
* **Limites de recursos**: Tenha em mente os limites de recursos (como memória e processamento) ao executar comandos que consomem muitos recursos.
* **Segurança**: Sempre verifique se os comandos estão sendo executados com as permissões corretas e se os dados sensíveis estão sendo tratados de forma segura.
* **Conexões de rede**: Verifique se as conexões de rede estão estáveis e se os servidores estão respondendo corretamente.
* **Timeouts**: Defina timeouts adequados para os comandos para evitar que eles fiquem pendentes indefinidamente.
* **Tratamento de erros**: Implemente um tratamento de erros robusto para lidar com erros inesperados e fornecer feedback útil ao usuário.
* **Validação de dados**: Valide os dados de entrada e saída para garantir que eles estejam corretos e consistentes.
* **Compatibilidade**: Verifique a compatibilidade das ferramentas e comandos com diferentes plataformas e versões.

Ao considerar esses casos de exceção e edge cases, você pode criar skills mais robustas e confiáveis que forneçam uma melhor experiência ao usuário.