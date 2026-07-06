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

### Erros de Arquivo

*   Se o arquivo de task artifact não puder ser criado, verifique se o diretório de destino existe e se o usuário tem permissão para criar arquivos.
*   Se o arquivo de task artifact não puder ser editado, verifique se o arquivo existe e se o usuário tem permissão para editá-lo.

### Erros de Formatação

*   Se a formatação do task artifact estiver incorreta, verifique se o arquivo está no formato markdown e se as tags `IsArtifact` e `ArtifactType` estão corretas.
*   Se as tags `IsArtifact` e `ArtifactType` estiverem ausentes ou incorretas, o arquivo não será reconhecido como um task artifact.

### Erros de Conexão

*   Se a conexão com o servidor Antigravity falhar, verifique se o servidor está online e se a conexão está configurada corretamente.
*   Se a conexão for interrompida durante a edição do task artifact, o arquivo pode ficar corrompido. Nesse caso, é recomendável criar um novo task artifact e copiar as informações do arquivo corrompido.

### Edge Cases

*   Se o task artifact for muito grande, pode haver problemas de desempenho ao editá-lo. Nesse caso, é recomendável dividir o task artifact em arquivos menores.
*   Se o task artifact for compartilhado entre várias pessoas, é importante garantir que as permissões sejam configuradas corretamente para evitar conflitos de edição.