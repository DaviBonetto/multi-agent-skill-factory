# Antigravity CLI (`agy`) Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On the Antigravity CLI (`agy`) these resolve to the tools below.

| Action skills request | Antigravity CLI equivalent |
|----------------------|----------------------|
| Dispatch a subagent (`Subagent (general-purpose):` template) | `invoke_subagent` with a built-in `TypeName` — `self` for full-capability work, `research` for read-only |
| Task tracking ("create a todo", "mark complete") | a **task artifact** — `write_to_file` with `IsArtifact: true` and `ArtifactType: "task"` (see [Task tracking](#task-tracking)). **Not** `manage_task`, which manages background processes. |

## Task tracking

Antigravity has **no todo tool** (`manage_task` manages background
processes — `list`/`kill`/`status`/`send_input` — it is *not* a checklist). When a
skill says to create a todo list or track tasks, maintain a **task artifact**: a
markdown checklist saved with `write_to_file` (`IsArtifact: true`,
`ArtifactMetadata.ArtifactType: "task"`), edited with `replace_file_content` /
`multi_replace_file_content` as you go.

At the start of any multi-step task, create the task artifact listing every step of
your plan. As you complete each step, edit the artifact to mark it done (`- [x]`).
If the plan changes, update the checklist. Keep it current — it is your source of
truth for what remains; once the conversation gets long, re-read it before starting
each step.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Invocação de Subagentes

*   Caso o subagente não seja encontrado, o sistema deve retornar um erro com o código `SUBAGENT_NOT_FOUND`.
*   Se o subagente for invocado com permissões insuficientes, o sistema deve retornar um erro com o código `INSUFFICIENT_PERMISSIONS`.

### Erros de Criação de Tarefas

*   Se a tarefa não puder ser criada devido a falta de espaço em disco, o sistema deve retornar um erro com o código `DISK_SPACE_EXCEEDED`.
*   Se a tarefa for criada com um nome inválido, o sistema deve retornar um erro com o código `INVALID_TASK_NAME`.

### Erros de Edição de Tarefas

*   Se a tarefa não puder ser editada devido a permissões insuficientes, o sistema deve retornar um erro com o código `INSUFFICIENT_PERMISSIONS`.
*   Se a tarefa for editada com um conteúdo inválido, o sistema deve retornar um erro com o código `INVALID_TASK_CONTENT`.

### Segurança

*   Todas as operações de criação, edição e exclusão de tarefas devem ser registradas em um log de segurança.
*   O acesso às tarefas deve ser controlado por meio de uma política de acesso baseada em papéis (RBAC).
*   As tarefas devem ser criptografadas em repouso e em trânsito para garantir a confidencialidade e integridade dos dados.