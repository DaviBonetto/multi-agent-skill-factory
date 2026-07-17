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
- **Erro de permissão ao criar arquivo**: Se o sistema não tiver permissão para criar um arquivo, o comando `write_to_file` falhará. Nesse caso, é necessário verificar as permissões do diretório e garantir que o sistema tenha permissão de escrita.
- **Erro de permissão ao editar arquivo**: Se o sistema não tiver permissão para editar um arquivo existente, o comando `replace_file_content` ou `multi_replace_file_content` falhará. Verifique as permissões do arquivo e do diretório para garantir que o sistema tenha permissão de escrita.

### Erros de Arquivo
- **Arquivo não encontrado**: Se o arquivo especificado para `replace_file_content` ou `multi_replace_file_content` não existir, o comando falhará. Nesse caso, é necessário criar o arquivo antes de tentar editá-lo ou tratar o erro como um caso de exceção.
- **Arquivo corrompido**: Se o arquivo estiver corrompido ou não for um arquivo markdown válido, o comando `replace_file_content` ou `multi_replace_file_content` pode falhar ou produzir resultados inesperados. É importante validar a integridade do arquivo antes de tentar editá-lo.

### Outros Edge Cases
- **Conflitos de nomes de arquivos**: Se dois ou mais comandos tentarem criar arquivos com o mesmo nome, pode haver conflitos. É importante garantir que os nomes de arquivos sejam únicos ou implementar um mecanismo de resolução de conflitos.
- **Tamanho do arquivo**: Se o arquivo for muito grande, os comandos `replace_file_content` ou `multi_replace_file_content` podem falhar devido a limitações de tamanho. É importante implementar um mecanismo para lidar com arquivos de grande tamanho.

Ao lidar com esses edge cases e erros, é crucial implementar tratamento de exceções adequado para garantir a robustez e a confiabilidade do sistema. Isso pode incluir a implementação de retries, logs de erro, e notificações para o usuário ou administrador do sistema.