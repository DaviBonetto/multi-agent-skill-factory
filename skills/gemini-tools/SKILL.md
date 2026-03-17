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

O tratamento de exceções e edge cases é crucial para garantir a estabilidade e segurança do sistema. Aqui estão alguns exemplos de como lidar com esses casos:

* **Arquivos não encontrados**: Ao usar `read_file` ou `write_file`, verifique se o arquivo existe antes de tentar acessá-lo. Se o arquivo não existir, gere um erro com uma mensagem clara e útil.
* **Permissões de arquivo**: Ao usar `write_file` ou `replace`, verifique se o usuário tem permissão para escrever no arquivo. Se não tiver, gere um erro com uma mensagem clara e útil.
* **Comandos inválidos**: Ao usar `run_shell_command`, verifique se o comando é válido e seguro antes de executá-lo. Se o comando for inválido ou inseguro, gere um erro com uma mensagem clara e útil.
* **Entrada de usuário**: Ao usar `ask_user`, verifique se a entrada do usuário é válida e segura antes de processá-la. Se a entrada for inválida ou insegura, gere um erro com uma mensagem clara e útil.
* **Exceções de sistema**: Ao usar qualquer ferramenta, esteja preparado para lidar com exceções de sistema, como falta de memória ou recursos. Gere um erro com uma mensagem clara e útil se ocorrer uma exceção de sistema.

Além disso, é importante considerar os seguintes edge cases:

* **Nomes de arquivos vazios**: Ao usar `read_file` ou `write_file`, verifique se o nome do arquivo é vazio. Se for vazio, gere um erro com uma mensagem clara e útil.
* **Diretórios vazios**: Ao usar `list_directory`, verifique se o diretório é vazio. Se for vazio, retorne uma lista vazia.
* **Entrada de usuário vazia**: Ao usar `ask_user`, verifique se a entrada do usuário é vazia. Se for vazia, gere um erro com uma mensagem clara e útil.

Ao lidar com esses casos, é importante fornecer mensagens de erro claras e úteis para ajudar o usuário a entender o que aconteceu e como corrigir o problema. Além disso, é importante garantir que o sistema seja seguro e estável, mesmo em casos de erro ou edge cases.