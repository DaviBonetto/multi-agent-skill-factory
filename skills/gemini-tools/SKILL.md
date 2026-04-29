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
Para garantir a robustez e segurança da skill, é importante considerar os seguintes casos de exceção e edge cases:

* **Erros de sintaxe**: Verificar se os comandos Gemini CLI estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
* **Arquivos não encontrados**: Tratar o caso de arquivos não encontrados durante a execução de comandos como `read_file` e `write_file`.
* **Permissões de acesso**: Verificar se o usuário tem permissão para executar os comandos Gemini CLI, especialmente aqueles que envolvem a criação ou edição de arquivos.
* **Comandos inválidos**: Tratar o caso de comandos inválidos ou desconhecidos, como `Task` tool, que não tem equivalente no Gemini CLI.
* **Exceções de execução**: Tratar exceções que ocorrem durante a execução de comandos, como erros de sintaxe ou falta de recursos.
* **Limites de recursos**: Verificar se os recursos disponíveis são suficientes para executar os comandos Gemini CLI, como memória e processamento.
* **Segurança**: Verificar se os comandos Gemini CLI estão sendo executados de forma segura, sem exposição de informações sensíveis ou vulnerabilidades de segurança.

Além disso, é importante implementar mecanismos de logging e monitoramento para detectar e tratar exceções e edge cases de forma eficaz. Isso pode incluir a implementação de try-catch blocks, logging de erros e exceções, e notificação de administradores em caso de erros críticos.