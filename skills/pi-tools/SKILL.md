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

Para garantir a segurança, é importante verificar se o pacote `pi-subagents` está instalado e configurado corretamente antes de executar subagentes. Além disso, é recomendável validar as entradas e saídas dos subagentes para evitar possíveis vulnerabilidades.

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções

*   Se o pacote `pi-subagents` não estiver instalado, uma exceção deve ser lançada com uma mensagem clara indicando que o recurso de subagente é opcional e não está disponível.
*   Se um subagente não puder ser executado devido a uma falha de configuração ou dependência, uma exceção deve ser lançada com uma mensagem detalhada sobre o erro.

### Edge Cases

*   **Subagente não disponível**: Se o subagente não estiver disponível, o sistema deve executar as ações sequencialmente na sessão atual ou explicar que o recurso de subagente não está instalado.
*   **Tarefa não pode ser criada**: Se uma tarefa não puder ser criada devido à falta de um tool de tarefa instalado, o sistema deve usar o plano de ações ou um arquivo `TODO.md` local para rastrear as tarefas.
*   **Erros de sintaxe**: Se houver erros de sintaxe nos arquivos de configuração ou nas ações, o sistema deve lançar uma exceção com uma mensagem clara sobre o erro e a localização do problema.