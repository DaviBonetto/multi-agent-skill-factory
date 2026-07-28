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

### Erros de Permissão

* Ao criar um task artifact, verifique se o usuário tem permissão para escrever no arquivo. Caso contrário, lance um erro com a mensagem "Permissão negada para criar task artifact".
* Ao editar um task artifact, verifique se o usuário tem permissão para editar o arquivo. Caso contrário, lance um erro com a mensagem "Permissão negada para editar task artifact".

### Erros de Arquivo

* Ao criar um task artifact, verifique se o arquivo já existe. Caso exista, lance um erro com a mensagem "Task artifact já existe".
* Ao editar um task artifact, verifique se o arquivo existe. Caso não exista, lance um erro com a mensagem "Task artifact não encontrado".

### Edge Cases

* Se o task artifact for muito grande, considere implementar uma solução de paginação para evitar problemas de desempenho.
* Se o task artifact for compartilhado entre múltiplos usuários, considere implementar uma solução de controle de versão para evitar conflitos.

### Segurança

* Certifique-se de que os task artifacts sejam armazenados de forma segura, utilizando criptografia e autenticação adequadas.
* Certifique-se de que os usuários apenas possam acessar e editar os task artifacts para os quais têm permissão.