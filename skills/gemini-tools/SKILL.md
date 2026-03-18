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
Para garantir a robustez e segurança da skill, é fundamental tratar exceções e edge cases. Aqui estão algumas diretrizes:

* **Tratamento de erros**: Todas as chamadas de API e operações de sistema devem ser encapsuladas em try-catch para capturar e tratar erros de forma adequada.
* **Validação de entrada**: Todas as entradas de usuário devem ser validadas para evitar ataques de injeção de código ou outros tipos de ataques.
* **Tratamento de casos limite**: Casos limite, como arquivos vazios ou diretórios inexistentes, devem ser tratados de forma adequada para evitar erros ou comportamentos inesperados.
* **Segurança**: Todas as operações que envolvem acesso a arquivos ou sistemas devem ser realizadas com permissões adequadas e segurança para evitar acessos não autorizados.
* **Testes**: A skill deve ser testada exhaustivamente para garantir que todos os casos de uso sejam cobertos e que a skill funcione corretamente em diferentes ambientes e condições.

Exemplos de tratamento de exceções e edge cases:

* `try`-`catch` para capturar erros de leitura de arquivos: `try { read_file('arquivo.txt') } catch (e) { console.error('Erro ao ler arquivo:', e) }`
* Validação de entrada de usuário: `if (typeof userInput === 'string' && userInput.trim() !== '') { // processar entrada } else { console.error('Entrada inválida') }`
* Tratamento de casos limite: `if (fileExists('arquivo.txt')) { // processar arquivo } else { console.error('Arquivo não existe') }`

Ao seguir essas diretrizes e exemplos, é possível garantir que a skill seja robusta, segura e funcione corretamente em diferentes situações.