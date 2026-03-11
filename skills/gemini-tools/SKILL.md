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

* **Erros de sintaxe**: Verifique se as entradas de usuário estão corretas e se os comandos estão bem formatados.
* **Arquivos não encontrados**: Trate os casos em que os arquivos especificados não existem ou não podem ser acessados.
* **Permissões insuficientes**: Verifique se o usuário tem permissões suficientes para executar as ações necessárias.
* **Exceções de rede**: Trate os casos em que a conexão de rede falha ou é interrompida.
* **Limites de recursos**: Verifique se os recursos necessários (como memória ou processamento) estão disponíveis e suficientes.
* **Entradas inválidas**: Trate os casos em que as entradas de usuário são inválidas ou inconsistentes.
* **Conflitos de nomes**: Verifique se os nomes de arquivos ou variáveis não entram em conflito com outros nomes existentes.
* **Segurança**: Verifique se as ações executadas não comprometem a segurança do sistema ou dos dados.

Além disso, é importante implementar mecanismos de tratamento de erros e exceções para garantir que a skill possa se recuperar de erros e continuar executando corretamente. Isso pode incluir:

* **Try-catch**: Use blocos try-catch para capturar e tratar exceções.
* **Verificação de erros**: Verifique se as operações foram bem-sucedidas e trate os erros caso contrário.
* **Logs de erro**: Registre os erros e exceções para facilitar a depuração e o diagnóstico.
* **Recuperação de erros**: Implemente mecanismos de recuperação de erros para permitir que a skill se recupere de erros e continue executando corretamente.