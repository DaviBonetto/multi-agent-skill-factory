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

### Erros de Permissão
- Ao criar ou editar um task artifact, verifique se o usuário tem permissão para escrever no arquivo. Caso contrário, lance um erro de permissão.
- Se o arquivo de task artifact não puder ser lido, lance um erro de permissão ou de arquivo não encontrado.

### Erros de Formatação
- Verifique se o task artifact está no formato de markdown correto. Se não estiver, lance um erro de formatação.
- Se o task artifact contiver caracteres inválidos, lance um erro de formatação.

### Edge Cases
- Se o task artifact for muito grande, considere paginar ou limitar o tamanho do arquivo.
- Se houver muitos task artifacts, considere implementar um sistema de gerenciamento de arquivos para evitar sobrecarga.
- Se o usuário tentar criar um task artifact com um nome de arquivo inválido, lance um erro de nome de arquivo inválido.

### Tratamento de Exceções
- Implemente um mecanismo de tratamento de exceções para lidar com erros inesperados, como erros de sistema ou erros de rede.
- Registre os erros e forneça feedback ao usuário sobre o que deu errado.

### Segurança
- Verifique se o task artifact não contém informações sensíveis, como senhas ou dados de cartão de crédito.
- Implemente um mecanismo de criptografia para proteger os dados do task artifact, se necessário.
- Verifique se o acesso ao task artifact é restrito apenas ao usuário autorizado.