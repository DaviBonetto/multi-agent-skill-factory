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

### Erros de Invocação de Subagentes

- **Erro de Permissão**: Se o subagente não tiver permissão para executar uma ação, o `invoke_subagent` retornará um erro de permissão. Nesse caso, o skill deve verificar as permissões do subagente e solicitar as permissões necessárias antes de tentar novamente.
- **Erro de Tipo de Subagente**: Se o tipo de subagente especificado for inválido, o `invoke_subagent` retornará um erro de tipo de subagente. Nesse caso, o skill deve verificar a documentação do subagente para garantir que o tipo de subagente esteja correto.

### Erros de Trabalho com Arquivos

- **Erro de Leitura de Arquivo**: Se o arquivo não existir ou não puder ser lido, o `read_file` retornará um erro de leitura de arquivo. Nesse caso, o skill deve verificar se o arquivo existe e se as permissões de leitura estão corretas antes de tentar novamente.
- **Erro de Escrita de Arquivo**: Se o arquivo não puder ser escrito, o `write_to_file` retornará um erro de escrita de arquivo. Nesse caso, o skill deve verificar se as permissões de escrita estão corretas e se o arquivo não está sendo usado por outro processo antes de tentar novamente.

### Edge Cases de Trabalho com Tarefas

- **Tarefa com Múltiplos Passos**: Se uma tarefa tiver múltiplos passos, o skill deve criar um artifact de tarefa para cada passo e atualizar o artifact à medida que cada passo for concluído.
- **Tarefa com Dependências**: Se uma tarefa tiver dependências, o skill deve verificar se as dependências estão satisfeitas antes de iniciar a tarefa. Se as dependências não estiverem satisfeitas, o skill deve aguardar até que as dependências sejam satisfeitas antes de iniciar a tarefa.

### Segurança

- **Validação de Entradas**: O skill deve validar todas as entradas para garantir que sejam válidas e seguras antes de processá-las.
- **Proteção contra Injeção de Comandos**: O skill deve proteger contra injeção de comandos garantindo que todas as entradas sejam validadas e sanitizadas antes de serem usadas em comandos.