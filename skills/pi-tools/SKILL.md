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

*   **Erro de permissão**: Ao tentar executar uma ação que exige permissão de administrador, o agente deve verificar se o usuário atual tem as permissões necessárias. Se não, o agente deve retornar uma mensagem de erro indicando a falta de permissão.
*   **Arquivo não encontrado**: Ao tentar ler ou editar um arquivo, o agente deve verificar se o arquivo existe. Se o arquivo não existir, o agente deve retornar uma mensagem de erro indicando que o arquivo não foi encontrado.
*   **Comando inválido**: Ao receber um comando inválido, o agente deve retornar uma mensagem de erro indicando que o comando é inválido e fornecer ajuda sobre como usar o comando corretamente.
*   **Subagente não instalado**: Ao tentar dispatchar um subagente, o agente deve verificar se o subagente está instalado. Se o subagente não estiver instalado, o agente deve retornar uma mensagem de erro indicando que o subagente não está instalado e fornecer instruções sobre como instalá-lo.
*   **Ferramenta de tarefa não instalada**: Ao tentar criar ou marcar uma tarefa como completa, o agente deve verificar se uma ferramenta de tarefa está instalada. Se a ferramenta de tarefa não estiver instalada, o agente deve usar o plano ou o arquivo `TODO.md` para rastrear as tarefas.
*   **Exceção de sintaxe**: Ao tentar executar uma ação que exige sintaxe específica, o agente deve verificar se a sintaxe está correta. Se a sintaxe estiver incorreta, o agente deve retornar uma mensagem de erro indicando a exceção de sintaxe e fornecer ajuda sobre como corrigir a sintaxe.