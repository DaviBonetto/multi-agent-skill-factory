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

Ao utilizar as ferramentas do Copilot CLI, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Comandos não suportados**: Certifique-se de que os comandos utilizados são suportados pela versão do Copilot CLI que está sendo utilizada.
* **Agentes não disponíveis**: Verifique se os agentes necessários estão instalados e configurados corretamente.
* **Sessões assíncronas**: Tenha cuidado ao trabalhar com sessões assíncronas, pois elas podem afetar o comportamento do sistema.
* **Limites de recursos**: Esteja ciente dos limites de recursos do sistema, como memória e processamento, para evitar sobrecarga.
* **Segurança**: Sempre verifique a segurança dos comandos e parâmetros utilizados, especialmente ao trabalhar com dados sensíveis.
* **Dependências**: Certifique-se de que todas as dependências necessárias estão instaladas e configuradas corretamente.
* **Versões incompatíveis**: Verifique se as versões do Copilot CLI e dos agentes são compatíveis entre si.

Além disso, é importante ter um plano de tratamento de exceções e edge cases, incluindo:

* **Log de erros**: Registre todos os erros e exceções para facilitar a depuração.
* **Notificação de erros**: Notifique os usuários e administradores sobre erros e exceções.
* **Recuperação de erros**: Tenha um plano para recuperar de erros e exceções, incluindo a possibilidade de reexecutar comandos ou restaurar o estado do sistema.
* **Testes**: Realize testes regulares para garantir que o sistema esteja funcionando corretamente e para detectar possíveis erros e exceções.