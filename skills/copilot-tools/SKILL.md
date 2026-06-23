# Copilot CLI Tool Mapping
Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On Copilot CLI these resolve to the tools below.

| Action skills request | Copilot CLI equivalent |
|----------------------|----------------------|
| Read a file | `view` |
| Create / edit / delete a file | `apply_patch` (Copilot CLI has no separate create/edit/write tools) |
| Run a shell command | `bash` |
| Search file contents | `rg` (ripgrep; Copilot CLI does not expose a `grep` tool) |
| Find files by name | `glob` |
| Fetch a URL | `web_fetch` |
| Search the web | `web_search` |
| Invoke a skill | `skill` |
| Dispatch a subagent (`Subagent (general-purpose):` template) | `task` with `agent_type: "general-purpose"` (other accepted types: `explore`, `task`, `code-review`, `research`, `configure-copilot`) |
| Multiple parallel dispatches | Multiple `task` calls in one response |
| Subagent status/output/control | `read_agent`, `list_agents`, `write_agent` |
| Task tracking ("create a todo", "mark complete") | `update_todo` |
| Enter / exit plan mode | No equivalent — stay in the main session |

## Instructions file

When a skill mentions "your instructions file", on Copilot CLI this is **`AGENTS.md`** at the repository root. If both `AGENTS.md` and `.github/copilot-instructions.md` are present, Copilot reads both.

## Personal skills directory

User-level skills live at **`~/.copilot/skills/`**. Copilot CLI also recognizes the cross-runtime alias **`~/.agents/skills/`**, which is shared with Codex and Gemini CLI. Each skill is a subdirectory containing a `SKILL.md` (with `name` and `description` frontmatter).

## Async shell sessions

Copilot CLI supports persistent async shell sessions:

| Tool | Purpose |
|------|---------|
| `bash` with `mode: "async"` (and optionally `detach: true`) | Start a long-running command in the background; returns a `shellId` |
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

*   **Erro de permissão**: Ao executar comandos que requerem permissões específicas, como `apply_patch` ou `bash`, certifique-se de que o usuário tem as permissões necessárias. Caso contrário, o comando falhará com um erro de permissão.
*   **Arquivos não encontrados**: Ao usar `view` ou `apply_patch`, se o arquivo especificado não existir, o comando retornará um erro de arquivo não encontrado.
*   **Comandos inválidos**: Se um comando inválido for passado para `bash` ou `write_bash`, o comando falhará com um erro de sintaxe.
*   **Sessões assíncronas**: Ao usar `bash` com `mode: "async"`, certifique-se de que o comando seja compatível com execução assíncrona. Além disso, ao usar `write_bash` ou `read_bash`, certifique-se de que a sessão assíncrona ainda esteja ativa.
*   **Limites de tamanho**: Ao usar `store_memory` ou `sql`, certifique-se de que os dados armazenados não excedam os limites de tamanho definidos pelo sistema.
*   **Erros de rede**: Ao usar `web_fetch` ou `web_search`, certifique-se de que a conexão de rede esteja estável e funcional. Erros de rede podem causar falhas nos comandos.
*   **Erros de sintaxe**: Ao usar `sql`, certifique-se de que a consulta seja sintaticamente correta. Erros de sintaxe podem causar falhas na execução da consulta.
*   **Erros de autenticação**: Ao usar GitHub MCP tools, certifique-se de que as credenciais de autenticação sejam válidas e corretas. Erros de autenticação podem causar falhas nos comandos.