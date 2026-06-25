# Pi Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On Pi these resolve to the tools below.

| Action skills request | Pi equivalent |
| --- | --- |
| Invoke a skill | Pi native skills: load the relevant `SKILL.md` with `read`, or let the human use `/skill:name` |
| Read a file | `read` |
| Create a file | `write` |
| Edit a file | `edit` |
| Run a shell command | `bash` |
| Search file contents | `grep` when active; otherwise `bash` with `rg`/`grep` |
| Find files by name | `find` or `bash` with shell globs |
| List files and subdirectories | `ls` when active; otherwise `bash` with `ls` |
| Dispatch a subagent (`Subagent (general-purpose):` template) | Use an installed subagent tool such as `subagent` from `pi-subagents` if available |
| Task tracking ("create a todo", "mark complete") | Use an installed todo/task tool if available, otherwise track tasks in the plan or `TODO.md` |

## Skills

Pi discovers skills from configured skill directories and installed Pi packages. A Superpowers Pi package should expose `skills/` through its `pi.skills` manifest entry. Pi does not expose Claude Code's `Skill` tool, but the agent should still follow the Superpowers rule: when a skill applies, load and follow it before responding.

## Subagents

Pi core does not ship a standard subagent tool. The `pi-subagents` package is a strong optional companion and provides a `subagent` tool with single-agent, chain, parallel, async, forked-context, and resume/status workflows. If no subagent tool is available, do not fabricate `Task` calls; execute sequentially in the current session or explain that the optional subagent capability is not installed.

## Task lists

Pi core does not ship a standard task-list tool. If a todo/task extension is installed, use its documented tool. Otherwise use Superpowers plan files, checklists in Markdown, or a repo-local `TODO.md` for task tracking. Older Superpowers docs may refer to `TodoWrite`; treat that as the task-tracking action above.

## ⚠️ Tratamento de Exceções e Edge Cases

*   **Erro de Permissão**: Ao tentar executar uma ação que exige permissão de administrador, mas o usuário atual não tem permissão, o sistema deve retornar uma mensagem de erro clara e concisa, indicando a necessidade de permissão de administrador.
*   **Arquivos Não Encontrados**: Se um arquivo solicitado não for encontrado, o sistema deve retornar uma mensagem de erro indicando que o arquivo não foi encontrado e, se possível, sugerir ações alternativas.
*   **Comandos Inválidos**: Se um comando inválido for passado para o sistema, ele deve retornar uma mensagem de erro clara, indicando o comando inválido e, se possível, sugerir a sintaxe correta.
*   **Subagentes Não Instalados**: Se um subagente for solicitado, mas não estiver instalado, o sistema deve explicar que o subagente não está instalado e, se possível, fornecer instruções para instalar o subagente.
*   **Limites de Recursos**: Se o sistema atingir um limite de recursos (como memória ou capacidade de processamento), ele deve retornar uma mensagem de erro indicando o limite atingido e, se possível, sugerir ações para mitigar o problema.
*   **Erros de Conexão**: Se ocorrer um erro de conexão ao tentar acessar um recurso externo, o sistema deve retornar uma mensagem de erro clara, indicando o erro de conexão e, se possível, sugerir ações para resolver o problema.
*   **Entrada Inválida**: Se a entrada fornecida for inválida ou inconsistente, o sistema deve retornar uma mensagem de erro clara, indicando a entrada inválida e, se possível, sugerir a entrada correta.
*   **Dependências Não Atendidas**: Se uma dependência necessária não for atendida, o sistema deve retornar uma mensagem de erro clara, indicando a dependência não atendida e, se possível, fornecer instruções para atender à dependência.