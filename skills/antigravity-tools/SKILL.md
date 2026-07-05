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
*   Caso o subagente não seja encontrado, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.
*   Se o subagente for invocado com parâmetros inválidos, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.

### Erros de Criação de Tarefas
*   Caso a tarefa não possa ser criada devido a permissões insuficientes, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.
*   Se a tarefa for criada com um nome inválido, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.

### Erros de Edição de Tarefas
*   Caso a tarefa não possa ser editada devido a permissões insuficientes, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.
*   Se a tarefa for editada com um nome inválido, o erro deve ser tratado e uma mensagem de erro clara deve ser exibida.

### Edge Cases
*   Caso a tarefa seja criada com um nome muito longo, o sistema deve truncar o nome e exibir uma mensagem de aviso.
*   Se a tarefa for criada com um nome que já existe, o sistema deve exibir uma mensagem de erro e solicitar um novo nome.

### Segurança
*   Todas as operações de criação, edição e exclusão de tarefas devem ser realizadas com autenticação e autorização adequadas.
*   Os dados das tarefas devem ser armazenados de forma segura e criptografada.