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

Para garantir a segurança, é importante verificar se as dependências necessárias estão instaladas e configuradas corretamente. Além disso, é fundamental garantir que as permissões de acesso sejam adequadas para evitar acessos não autorizados.

## ⚠️ Tratamento de Exceções e Edge Cases

### Casos de Erro

*   Se o pacote `pi-subagents` não estiver instalado, o sistema deve retornar uma mensagem de erro indicando que a funcionalidade de subagentes não está disponível.
*   Se a extensão todo/task não estiver instalada, o sistema deve usar o plano ou o arquivo `TODO.md` para rastrear tarefas.
*   Se ocorrer um erro ao executar uma ação, o sistema deve registrar o erro e retornar uma mensagem de erro para o usuário.

### Edge Cases

*   Se o usuário tentar criar uma tarefa com um nome vazio, o sistema deve retornar uma mensagem de erro indicando que o nome da tarefa é obrigatório.
*   Se o usuário tentar marcar uma tarefa como concluída que não existe, o sistema deve retornar uma mensagem de erro indicando que a tarefa não existe.
*   Se o sistema estiver configurado para usar um arquivo `TODO.md` para rastrear tarefas e o arquivo não existir, o sistema deve criar o arquivo automaticamente.

### Tratamento de Exceções

*   O sistema deve ter um mecanismo de tratamento de exceções para lidar com erros inesperados.
*   O sistema deve registrar todos os erros e exceções para que possam ser analisados e corrigidos posteriormente.
*   O sistema deve retornar mensagens de erro claras e concisas para o usuário, indicando o que deu errado e como corrigir o problema.