# Antigravity CLI (`agy`) Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On the Antigravity CLI (`agy`) these resolve to the tools below.

| Action skills request | Antigravity CLI equivalent |
|----------------------|----------------------|
| Dispatch a subagent (`Subagent (general-purpose):` template) | `invoke_subagent` with a built-in `TypeName` — `self` for full-capability work, `research` for read-only (see [Subagent support](#subagent-support)) |
| Task tracking ("create a todo", "mark complete") | a **task artifact** — `write_to_file` with `IsArtifact: true` and `ArtifactType: "task"` (see [Task tracking](#task-tracking)). **Not** `manage_task`, which manages background processes. |

## Task tracking

Antigravity has **no todo tool** (`manage_task` manages background processes — `list`/`kill`/`status`/`send_input` — it is *not* a checklist). When a skill says to create a todo list or track tasks, maintain a **task artifact**: a markdown checklist saved with `write_to_file` (`IsArtifact: true`, `ArtifactMetadata.ArtifactType: "task"`), edited with `replace_file_content` / `multi_replace_file_content` as you go.

At the start of any multi-step task, create the task artifact listing every step of your plan. As you complete each step, edit the artifact to mark it done (`- [x]`). If the plan changes, update the checklist. Keep it current — it is your source of truth for what remains; once the conversation gets long, re-read it before starting each step.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Invocação de Subagentes

*   Caso o subagente não seja encontrado, o sistema deve retornar um erro com uma mensagem clara indicando que o subagente não existe.
*   Se o subagente for invocado com permissões insuficientes, o sistema deve retornar um erro com uma mensagem indicando as permissões necessárias.

### Erros de Criação de Tarefas

*   Se a tarefa não puder ser criada devido a falta de espaço em disco, o sistema deve retornar um erro com uma mensagem indicando a necessidade de liberar espaço em disco.
*   Se a tarefa for criada com um nome duplicado, o sistema deve retornar um erro com uma mensagem indicando que a tarefa já existe.

### Erros de Edição de Tarefas

*   Se a tarefa não puder ser editada devido a permissões insuficientes, o sistema deve retornar um erro com uma mensagem indicando as permissões necessárias.
*   Se a tarefa for editada com um formato inválido, o sistema deve retornar um erro com uma mensagem indicando o formato correto.

### Segurança

*   Todas as operações de criação, edição e exclusão de tarefas devem ser registradas em um log de auditoria para fins de segurança e conformidade.
*   O sistema deve implementar autenticação e autorização para garantir que apenas usuários autorizados possam criar, editar e excluir tarefas.

### Edge Cases

*   Se a tarefa for criada com um nome vazio, o sistema deve retornar um erro com uma mensagem indicando que o nome da tarefa é obrigatório.
*   Se a tarefa for editada com um estado inválido (por exemplo, "concluída" quando a tarefa não foi iniciada), o sistema deve retornar um erro com uma mensagem indicando o estado válido.