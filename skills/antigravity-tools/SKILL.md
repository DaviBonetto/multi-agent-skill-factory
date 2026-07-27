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
- **Arquivo não encontrado**: Se o arquivo de task artifact não for encontrado, uma exceção será lançada. Nesse caso, o sistema deve criar um novo arquivo com o nome especificado e inicializá-lo com uma lista vazia.
- **Permissão de escrita**: Se o sistema não tiver permissão para escrever no arquivo de task artifact, uma exceção de permissão será lançada. Nesse caso, o sistema deve solicitar permissão ao usuário ou utilizar um local de armazenamento alternativo.

### Erros de Formatação
- **Formatação inválida**: Se o arquivo de task artifact tiver uma formatação inválida (por exemplo, não for um arquivo markdown), o sistema deve lançar uma exceção e solicitar ao usuário que corrija o arquivo.

### Edge Cases
- **Tarefa com descrição vazia**: Se uma tarefa for criada com uma descrição vazia, o sistema deve permitir que o usuário edite a tarefa e adicione uma descrição.
- **Tarefa com mais de uma marcação de conclusão**: Se uma tarefa for marcada como concluída mais de uma vez, o sistema deve apenas manter a marcação de conclusão mais recente.

### Segurança
- **Validação de entrada**: O sistema deve validar todas as entradas de usuário para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- **Criptografia**: O sistema deve utilizar criptografia para proteger os arquivos de task artifact e evitar acessos não autorizados.