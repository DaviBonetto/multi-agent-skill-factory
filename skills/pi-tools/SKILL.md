# Pi Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On Pi these resolve to the tools below.

| Action skills request | Pi equivalent |
| --- | --- |
| Dispatch a subagent (`Subagent (general-purpose):` template) | Use an installed subagent tool such as `subagent` from `pi-subagents` if available |
| Task tracking ("create a todo", "mark complete") | Use an installed todo/task tool if available, otherwise track tasks in the plan or `TODO.md` |

## Subagents

Pi core does not ship a standard subagent tool. The `pi-subagents` package is a strong optional companion and provides a `subagent` tool with single-agent, chain, parallel, async, forked-context, and resume/status workflows. If no subagent tool is available, do not fabricate `Task` calls; execute sequentially in the current session or explain that the optional subagent capability is not installed.

## Task lists

Pi core does not ship a standard task-list tool. If a todo/task extension is installed, use its documented tool. Otherwise use Superpowers plan files, checklists in Markdown, or a repo-local `TODO.md` for task tracking. Older Superpowers docs may refer to `TodoWrite`; treat that as the task-tracking action above.

## Segurança

Para garantir a segurança, é importante verificar se as ferramentas instaladas estão atualizadas e se os pacotes utilizados são de fontes confiáveis. Além disso, é fundamental implementar controles de acesso e autenticação para evitar o acesso não autorizado às ferramentas e aos dados.

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções

*   Caso o pacote `pi-subagents` não esteja instalado, uma exceção será lançada. Nesse caso, o sistema deve executar as ações sequencialmente na sessão atual ou explicar que a funcionalidade de subagente opcional não está instalada.
*   Se a extensão todo/task não estiver instalada, o sistema deve usar os arquivos de plano do Superpowers, listas de tarefas em Markdown ou um arquivo `TODO.md` local para rastrear as tarefas.
*   Em caso de falha na execução de uma ação, o sistema deve registrar o erro e notificar o usuário.

### Edge Cases

*   **Subagente não instalado**: Se o pacote `pi-subagents` não estiver instalado, o sistema deve ser capaz de executar as ações sequencialmente na sessão atual ou explicar que a funcionalidade de subagente opcional não está instalada.
*   **Extensão todo/task não instalada**: Se a extensão todo/task não estiver instalada, o sistema deve ser capaz de usar os arquivos de plano do Superpowers, listas de tarefas em Markdown ou um arquivo `TODO.md` local para rastrear as tarefas.
*   **Ação inválida**: Se uma ação inválida for solicitada, o sistema deve lançar uma exceção e notificar o usuário.
*   **Falta de permissão**: Se o usuário não tiver permissão para executar uma ação, o sistema deve lançar uma exceção e notificar o usuário.

Ao tratar esses casos, o sistema pode garantir que as ações sejam executadas de forma segura e confiável, mesmo em situações inesperadas.