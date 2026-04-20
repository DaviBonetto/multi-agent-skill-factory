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

*   Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
*   Em caso de erros de sintaxe, o sistema deve retornar uma mensagem de erro clara e concisa, indicando a linha e a coluna onde o erro ocorreu.

### Erros de permissão

*   Verifique se o usuário tem permissão para executar o comando solicitado.
*   Em caso de erros de permissão, o sistema deve retornar uma mensagem de erro indicando que o usuário não tem permissão para executar o comando.

### Erros de arquivo

*   Verifique se o arquivo solicitado existe e se é possível ler ou escrever nele.
*   Em caso de erros de arquivo, o sistema deve retornar uma mensagem de erro indicando o problema com o arquivo.

### Erros de rede

*   Verifique se a conexão de rede está estável e se é possível se comunicar com o servidor remoto.
*   Em caso de erros de rede, o sistema deve retornar uma mensagem de erro indicando o problema com a conexão de rede.

### Edge Cases

*   **Comandos vazios**: Verifique se o comando está vazio ou se não contém parâmetros suficientes.
*   **Parâmetros inválidos**: Verifique se os parâmetros passados são válidos e se atendem aos requisitos do comando.
*   **Comandos desconhecidos**: Verifique se o comando solicitado é válido e se está registrado no sistema.
*   **Sobrecarga de trabalho**: Verifique se o sistema está sobrecarregado e se é possível executar o comando solicitado.

### Segurança

*   **Validação de entrada**: Verifique se os dados de entrada são válidos e se atendem aos requisitos de segurança.
*   **Autenticação**: Verifique se o usuário está autenticado e se tem permissão para executar o comando solicitado.
*   **Criptografia**: Verifique se os dados sensíveis estão criptografados e se são transmitidos de forma segura.

Ao tratar esses casos, é fundamental garantir que o sistema seja robusto, seguro e fácil de usar, proporcionando uma experiência satisfatória para os usuários.