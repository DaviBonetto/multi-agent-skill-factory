# Gemini CLI Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Gemini CLI equivalent |
|-----------------|----------------------|
| `Read` (file reading) | `read_file` |
| `Write` (file creation) | `write_file` |
| `Edit` (file editing) | `replace` |
| `Bash` (run commands) | `run_shell_command` |
| `Grep` (search file content) | `grep_search` |
| `Glob` (search files by name) | `glob` |
| `TodoWrite` (task tracking) | `write_todos` |
| `Skill` tool (invoke a skill) | `activate_skill` |
| `WebSearch` | `google_web_search` |
| `WebFetch` | `web_fetch` |
| `Task` tool (dispatch subagent) | No equivalent — Gemini CLI does not support subagents |

## No subagent support

Gemini CLI has no equivalent to Claude Code's `Task` tool. Skills that rely on subagent dispatch (`subagent-driven-development`, `dispatching-parallel-agents`) will fall back to single-session execution via `executing-plans`.

## Additional Gemini CLI tools

These tools are available in Gemini CLI but have no Claude Code equivalent:

| Tool | Purpose |
|------|---------|
| `list_directory` | List files and subdirectories |
| `save_memory` | Persist facts to GEMINI.md across sessions |
| `ask_user` | Request structured input from the user |
| `tracker_create_task` | Rich task management (create, update, list, visualize) |
| `enter_plan_mode` / `exit_plan_mode` | Switch to read-only research mode before making changes |

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de sintaxe

*   Certifique-se de que todos os comandos estejam corretamente formatados e que não haja erros de sintaxe.
*   Em caso de erros de sintaxe, o sistema deve retornar uma mensagem de erro clara e concisa.

### Erros de permissão

*   Verifique se o usuário tem as permissões necessárias para executar os comandos.
*   Em caso de erros de permissão, o sistema deve retornar uma mensagem de erro indicando a falta de permissão.

### Erros de arquivo

*   Verifique se os arquivos necessários estão presentes e acessíveis.
*   Em caso de erros de arquivo, o sistema deve retornar uma mensagem de erro indicando o problema com o arquivo.

### Edge cases

*   **Arquivos vazios**: Em caso de arquivos vazios, o sistema deve retornar uma mensagem de erro ou um resultado padrão.
*   **Arquivos muito grandes**: Em caso de arquivos muito grandes, o sistema deve ser capaz de lidar com eles de forma eficiente ou retornar uma mensagem de erro.
*   **Comandos inválidos**: Em caso de comandos inválidos, o sistema deve retornar uma mensagem de erro clara e concisa.

### Segurança

*   **Validação de entrada**: Certifique-se de que todas as entradas sejam validadas para evitar ataques de injeção de código.
*   **Uso de permissões**: Certifique-se de que as permissões sejam usadas de forma segura para evitar acessos não autorizados.
*   **Criptografia**: Certifique-se de que todos os dados sensíveis sejam criptografados para proteger a privacidade dos usuários.