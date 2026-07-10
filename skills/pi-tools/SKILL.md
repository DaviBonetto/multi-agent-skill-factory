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

Para garantir a segurança, é importante:
- Validar as entradas de usuário para evitar injeção de comandos maliciosos.
- Utilizar permissões mínimas necessárias para executar as ações.
- Manter os pacotes e dependências atualizados para evitar vulnerabilidades conhecidas.

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções

- **Subagent não instalado**: Se o pacote `pi-subagents` não estiver instalado, o sistema deve executar as ações sequencialmente na sessão atual ou informar que a capacidade de subagent é opcional e não está instalada.
- **Todo/Task não instalado**: Se não houver uma extensão todo/task instalada, o sistema deve usar arquivos de plano do Superpowers, listas de tarefas em Markdown ou um arquivo `TODO.md` local para rastrear tarefas.
- **Erros de sintaxe**: O sistema deve lidar com erros de sintaxe nos arquivos de configuração ou nos comandos de ação, fornecendo mensagens de erro claras e úteis.

### Edge Cases

- **Multiplos subagents**: Se múltiplos subagents forem solicitados, o sistema deve ser capaz de lidar com a execução paralela ou sequencial deles, dependendo das capacidades do subagent instalado.
- **Tarefas concorrentes**: Se múltiplas tarefas forem solicitadas simultaneamente, o sistema deve ser capaz de lidar com a concorrência, garantindo que as tarefas sejam executadas corretamente e sem perda de dados.
- **Limites de recursos**: O sistema deve ser capaz de lidar com limites de recursos, como memória ou processamento, e fornecer mensagens de erro apropriadas se esses limites forem atingidos.