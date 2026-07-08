# Antigravity CLI (`agy`) Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On the Antigravity CLI (`agy`) these resolve to the tools below.

| Action skills request | Antigravity CLI equivalent |
|----------------------|----------------------|
| Dispatch a subagent (`Subagent (general-purpose):` template) | `invoke_subagent` with a built-in `TypeName` — `self` for full-capability work, `research` for read-only (see [Subagent support](#subagent-support)) |
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

### Erros de Arquivo

*   Se o arquivo de task artifact não existir, crie-o com `write_to_file` antes de tentar editá-lo.
*   Se o arquivo de task artifact existir, mas não for um arquivo markdown, lance um erro com `raise_error` e uma mensagem de erro apropriada.
*   Se o arquivo de task artifact for corrompido ou não puder ser lido, lance um erro com `raise_error` e uma mensagem de erro apropriada.

### Erros de Permissão

*   Se o agente não tiver permissão para criar ou editar o arquivo de task artifact, lance um erro com `raise_error` e uma mensagem de erro apropriada.
*   Se o agente não tiver permissão para ler o arquivo de task artifact, lance um erro com `raise_error` e uma mensagem de erro apropriada.

### Outros Erros

*   Se ocorrer um erro desconhecido ao criar ou editar o arquivo de task artifact, lance um erro com `raise_error` e uma mensagem de erro apropriada.
*   Se o plano de tarefas for muito grande, considere dividir em tarefas menores e mais gerenciáveis.

### Exemplos de Edge Cases

*   Se o plano de tarefas for vazio, não crie o arquivo de task artifact.
*   Se o plano de tarefas tiver apenas uma tarefa, considere não criar o arquivo de task artifact e executar a tarefa diretamente.
*   Se o plano de tarefas for muito complexo, considere criar um arquivo de task artifact para cada tarefa ou grupo de tarefas relacionadas.