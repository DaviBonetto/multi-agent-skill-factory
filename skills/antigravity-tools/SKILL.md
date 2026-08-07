# Antigravity CLI (`agy`) Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On the Antigravity CLI (`agy`) these resolve to the tools below.

| Action skills request | Antigravity CLI equivalent |
|----------------------|----------------------|
| Dispatch a subagent (`Subagent (general-purpose):` template) | `invoke_subagent` with a built-in `TypeName` — `self` for full-capability work, `research` for read-only |
| Task tracking ("create a todo", "mark complete") | a **task artifact** — `write_to_file` with `IsArtifact: true` and `ArtifactType: "task"` (see [Task tracking](#task-tracking)). **Not** `manage_task`, which manages background processes. |

## Task tracking

Antigravity has **no todo tool** (`manage_task` manages background processes — `list`/`kill`/`status`/`send_input` — it is *not* a checklist). When a skill says to create a todo list or track tasks, maintain a **task artifact**: a markdown checklist saved with `write_to_file` (`IsArtifact: true`, `ArtifactMetadata.ArtifactType: "task"`), edited with `replace_file_content` / `multi_replace_file_content` as you go.

At the start of any multi-step task, create the task artifact listing every step of your plan. As you complete each step, edit the artifact to mark it done (`- [x]`). If the plan changes, update the checklist. Keep it current — it is your source of truth for what remains; once the conversation gets long, re-read it before starting each step.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Invocação de Subagentes

*   Caso o subagente não seja encontrado, uma exceção `SubagentNotFoundError` será lançada.
*   Se o subagente for invocado com permissões insuficientes, uma exceção `PermissionError` será lançada.

### Erros de Manipulação de Arquivos

*   Se o arquivo não for encontrado, uma exceção `FileNotFoundError` será lançada.
*   Se houver um erro ao escrever ou ler o arquivo, uma exceção `IOError` será lançada.

### Edge Cases

*   **Tarefa com muitos passos**: Se a tarefa tiver muitos passos, é recomendável dividir a tarefa em sub-tarefas menores e gerenciar cada uma delas separadamente.
*   **Tarefa com dependências**: Se a tarefa tiver dependências, é importante garantir que todas as dependências sejam resolvidas antes de iniciar a tarefa.
*   **Tarefa com prazos**: Se a tarefa tiver prazos, é importante garantir que a tarefa seja concluída dentro do prazo estabelecido.

### Tratamento de Exceções

*   Todas as exceções devem ser tratadas e registradas para garantir que o sistema permaneça estável e seguro.
*   É recomendável implementar um mecanismo de retry para lidar com erros temporários.

### Segurança

*   Todas as operações devem ser realizadas com permissões mínimas necessárias para evitar vulnerabilidades de segurança.
*   É recomendável implementar um mecanismo de autenticação e autorização para garantir que apenas usuários autorizados possam acessar e manipular as tarefas e arquivos.