# Antigravity CLI (`agy`) Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On the Antigravity CLI (`agy`) these resolve to the tools below.

| Action skills request | Antigravity CLI equivalent |
|----------------------|----------------------|
| Dispatch a subagent (`Subagent (general-purpose):` template) | `invoke_subagent` with a built-in `TypeName` — `self` for full-capability work, `research` for read-only |
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

Ao criar um task artifact, é importante considerar os seguintes casos:
* **Erro de permissão**: Se o usuário não tiver permissão para criar ou editar o arquivo, o sistema deve retornar um erro com uma mensagem clara e concisa.
* **Arquivo não encontrado**: Se o arquivo não for encontrado, o sistema deve criar um novo arquivo com o nome especificado.
* **Conflito de nomes**: Se dois ou mais task artifacts tiverem o mesmo nome, o sistema deve retornar um erro e solicitar que o usuário forneça um nome único.
* **Formato inválido**: Se o formato do task artifact for inválido, o sistema deve retornar um erro e solicitar que o usuário forneça um formato válido.
* **Tamanho do arquivo**: Se o tamanho do arquivo for muito grande, o sistema deve retornar um erro e solicitar que o usuário reduza o tamanho do arquivo.

Além disso, é importante considerar os seguintes edge cases:
* **Criar um task artifact vazio**: Se o usuário criar um task artifact vazio, o sistema deve permitir que o usuário adicione itens à lista.
* **Editar um task artifact vazio**: Se o usuário editar um task artifact vazio, o sistema deve permitir que o usuário adicione itens à lista.
* **Excluir um task artifact**: Se o usuário excluir um task artifact, o sistema deve remover o arquivo e todas as referências a ele.

Para lidar com esses casos, é recomendável implementar os seguintes tratamentos de erros:
* **Try-catch**: Use blocos try-catch para capturar e tratar erros de forma eficaz.
* **Validação de entrada**: Valide a entrada do usuário para garantir que ela esteja no formato correto e dentro dos limites permitidos.
* **Mensagens de erro**: Forneça mensagens de erro claras e concisas para ajudar o usuário a entender o que deu errado e como corrigir o problema.