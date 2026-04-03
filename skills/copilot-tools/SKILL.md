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
| `Task` tool (dispatch subagent) | `task` (see [Agent types](#agent-types)) |
| Multiple `Task` calls (parallel) | Multiple `task` calls |
| Task status/output | `read_agent`, `list_agents` |
| `TodoWrite` (task tracking) | `sql` with built-in `todos` table |
| `WebSearch` | No equivalent — use `web_fetch` with a search engine URL |
| `EnterPlanMode` / `ExitPlanMode` | No equivalent — stay in the main session |

## Agent types

Copilot CLI's `task` tool accepts an `agent_type` parameter:

| Claude Code agent | Copilot CLI equivalent |
|-------------------|----------------------|
| `general-purpose` | `"general-purpose"` |
| `Explore` | `"explore"` |
| Named plugin agents (e.g. `superpowers:code-reviewer`) | Discovered automatically from installed plugins |

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

* **Erros de sintaxe**: Ao usar o `bash` com comandos malformados, o sistema deve retornar um erro de sintaxe e não executar o comando.
* **Comandos não encontrados**: Se um comando não for encontrado, o sistema deve retornar um erro de comando não encontrado e não tentar executar um comando desconhecido.
* **Permissões insuficientes**: Se o usuário não tiver permissões suficientes para executar um comando, o sistema deve retornar um erro de permissão e não executar o comando.
* **Limites de recursos**: O sistema deve ter limites de recursos (como memória e CPU) para evitar que comandos consumam todos os recursos do sistema.
* **Tempo de execução**: O sistema deve ter um tempo de execução máximo para comandos para evitar que comandos fiquem executando indefinidamente.
* **Entrada inválida**: O sistema deve validar a entrada do usuário para evitar que comandos sejam executados com entrada inválida.
* **Conexão de rede**: O sistema deve lidar com erros de conexão de rede ao usar o `web_fetch` e outros comandos que dependem da conexão de rede.
* **Agentes não disponíveis**: Se um agente não estiver disponível, o sistema deve retornar um erro de agente não disponível e não tentar executar o comando.
* **Sessões de shell assíncronas**: O sistema deve lidar com erros de sessões de shell assíncronas, como a falta de recursos para criar uma nova sessão ou a perda de conexão com uma sessão existente.