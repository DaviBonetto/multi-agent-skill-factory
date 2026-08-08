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

### Erros de Arquivo

*   Caso o arquivo de task artifact não exista, um erro de arquivo não encontrado será retornado. Nesse caso, o sistema deve criar o arquivo e inicializá-lo com uma lista vazia.
*   Se o arquivo de task artifact estiver corrompido ou não for um arquivo markdown válido, um erro de parsing será retornado. Nesse caso, o sistema deve tentar recuperar o arquivo ou criar um novo.

### Erros de Permissão

*   Se o sistema não tiver permissão para criar ou editar o arquivo de task artifact, um erro de permissão será retornado. Nesse caso, o sistema deve solicitar permissão ao usuário ou utilizar um local de armazenamento alternativo.

### Edge Cases

*   **Multiplos usuários**: Se múltiplos usuários estiverem utilizando o sistema simultaneamente, é possível que haja conflitos ao editar o arquivo de task artifact. Nesse caso, o sistema deve implementar um mecanismo de controle de versão para garantir a integridade dos dados.
*   **Tamanhos de arquivo grandes**: Se o arquivo de task artifact for muito grande, pode haver problemas de desempenho ao editá-lo. Nesse caso, o sistema deve considerar a implementação de um mecanismo de paginação ou armazenamento em banco de dados.
*   **Caracteres especiais**: Se o nome do arquivo ou o conteúdo do task artifact contiver caracteres especiais, pode haver problemas de encoding ou parsing. Nesse caso, o sistema deve garantir que todos os caracteres sejam devidamente escapados ou tratados.