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

*   **Erro de Permissão**: Em caso de falta de permissão para executar uma ação, o agente deve retornar uma mensagem de erro clara e concisa, indicando a ação que não pôde ser executada e o motivo.
*   **Arquivos Não Encontrados**: Se um arquivo solicitado não for encontrado, o agente deve informar o usuário sobre o erro e, se possível, sugerir alternativas ou ações para resolver a situação.
*   **Comandos Inválidos**: Para comandos inválidos ou malformados, o agente deve retornar uma mensagem de erro que ajude o usuário a entender o que deu errado e como corrigir o comando.
*   **Subagentes Não Instalados**: Se um subagente necessário não estiver instalado, o agente deve explicar a situação ao usuário e fornecer instruções sobre como instalar o subagente necessário ou alternativas para alcançar o objetivo desejado.
*   **Exceções de Execução**: Em caso de exceções durante a execução de uma ação, o agente deve capturar a exceção, registrar o erro para análise posterior e retornar uma mensagem de erro ao usuário, mantendo a aplicação estável e segura.
*   **Limites de Recursos**: Se o agente atingir limites de recursos (como memória ou capacidade de processamento), deve priorizar a estabilidade do sistema, cancelar operações não essenciais e notificar o usuário sobre a situação, sugerindo ajustes ou melhorias para evitar tais limitações no futuro.