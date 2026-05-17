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
* **Comandos não encontrados**: Se um comando não for encontrado, verifique se o nome do comando está correto e se o comando está disponível na versão atual do Copilot CLI.
* **Parâmetros inválidos**: Verifique se os parâmetros passados para os comandos são válidos e se atendem aos requisitos do comando.
* **Sessões async**: Ao utilizar sessões async, certifique-se de que as sessões sejam corretamente iniciadas e terminadas para evitar problemas de concorrência.
* **Acesso a recursos**: Certifique-se de que os recursos necessários (como arquivos, diretórios, etc.) estejam disponíveis e acessíveis antes de tentar utilizá-los.
* **Limites de recursos**: Esteja ciente dos limites de recursos (como memória, CPU, etc.) e planeje as tarefas de acordo para evitar problemas de desempenho.
* **Segurança**: Sempre utilize práticas de segurança adequadas ao trabalhar com comandos e recursos do Copilot CLI, especialmente ao lidar com informações sensíveis ou ao executar comandos que possam ter implicações de segurança.

Além disso, é importante:

* **Testar os comandos**: Antes de executar comandos em produção, teste-os em um ambiente de desenvolvimento ou teste para garantir que funcionem corretamente.
* **Verificar a documentação**: Verifique a documentação do Copilot CLI regularmente para estar ciente de novas funcionalidades, mudanças e melhorias.
* **Reportar erros**: Se encontrar erros ou problemas, reporte-os à equipe de suporte do Copilot CLI para que possam ser corrigidos e melhorados.