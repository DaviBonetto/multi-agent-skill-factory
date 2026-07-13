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

Ao criar um task artifact, considere os seguintes casos:
* **Erro de permissão**: se o usuário não tiver permissão para criar ou editar o arquivo, o sistema deve retornar um erro claro e conciso.
* **Arquivo existente**: se o arquivo já existir, o sistema deve verificar se o arquivo é um task artifact válido e, se não for, retornar um erro.
* **Formato inválido**: se o formato do task artifact for inválido, o sistema deve retornar um erro e fornecer orientações sobre o formato correto.
* **Tamanho do arquivo**: se o tamanho do arquivo for muito grande, o sistema deve retornar um erro e fornecer orientações sobre o tamanho máximo permitido.
* **Conflito de nomes**: se dois ou mais task artifacts tiverem o mesmo nome, o sistema deve retornar um erro e fornecer orientações sobre como resolver o conflito.

Além disso, é importante considerar os seguintes edge cases:
* **Criar um task artifact vazio**: o sistema deve permitir que o usuário crie um task artifact vazio e forneça orientações sobre como preencher o arquivo.
* **Editar um task artifact vazio**: o sistema deve permitir que o usuário edite um task artifact vazio e forneça orientações sobre como preencher o arquivo.
* **Excluir um task artifact**: o sistema deve permitir que o usuário exclua um task artifact e forneça orientações sobre como confirmar a exclusão.

Para lidar com esses casos, o sistema deve implementar os seguintes tratamentos de erros:
* **Try-catch**: o sistema deve usar try-catch para capturar erros e fornecer mensagens de erro claras e concisas.
* **Validação de entrada**: o sistema deve validar a entrada do usuário para garantir que o formato do task artifact seja válido e que o arquivo não exista.
* **Mensagens de erro**: o sistema deve fornecer mensagens de erro claras e concisas para ajudar o usuário a entender o que deu errado e como corrigir o problema.