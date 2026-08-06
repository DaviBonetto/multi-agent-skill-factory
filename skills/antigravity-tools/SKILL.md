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

*   Se o subagente não for encontrado, o erro será tratado como uma exceção `SubagentNotFoundError`.
*   Se o subagente não tiver permissão para executar uma ação, o erro será tratado como uma exceção `PermissionError`.

### Erros de Leitura e Escrita de Arquivos

*   Se o arquivo não for encontrado, o erro será tratado como uma exceção `FileNotFoundError`.
*   Se o arquivo não puder ser lido ou escrito devido a permissões, o erro será tratado como uma exceção `PermissionError`.

### Tratamento de Conflitos de Versão

*   Se houver um conflito de versão ao atualizar um arquivo, o erro será tratado como uma exceção `VersionConflictError`.
*   O sistema deve ser capaz de lidar com conflitos de versão e fornecer uma solução para resolvê-los.

### Edge Cases

*   **Tamanho do Arquivo**: O sistema deve ser capaz de lidar com arquivos de tamanhos variados, desde pequenos até muito grandes.
*   **Tipo de Arquivo**: O sistema deve ser capaz de lidar com diferentes tipos de arquivos, incluindo texto, imagens, áudio e vídeo.
*   **Caracteres Especiais**: O sistema deve ser capaz de lidar com caracteres especiais em nomes de arquivos e conteúdo.

### Segurança

*   **Autenticação**: O sistema deve exigir autenticação para acessar e modificar arquivos.
*   **Autorização**: O sistema deve ter um sistema de autorização para controlar quem pode acessar e modificar arquivos.
*   **Criptografia**: O sistema deve usar criptografia para proteger os arquivos em trânsito e em repouso.