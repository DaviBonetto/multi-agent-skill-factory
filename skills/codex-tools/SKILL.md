## Subagent dispatch requires multi-agent support

Add to your Codex config (`~/.codex/config.toml`):

```toml
[features]
multi_agent = true
```

This enables `spawn_agent`, `wait_agent`, and `close_agent` for skills like `dispatching-parallel-agents` and `subagent-driven-development`. When using subagent-driven-development, you should always close implementer and reviewer subagents when they have finished all their work.

## Environment Detection

Skills that create worktrees or finish branches should detect their environment with read-only git commands before proceeding:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

- `GIT_DIR != GIT_COMMON` → already in a linked worktree (skip creation)
- `BRANCH` empty → detached HEAD (cannot branch/push/PR from sandbox)

See `using-git-worktrees` Step 0 and `finishing-a-development-branch` Step 1 for how each skill uses these signals.

## Codex App Finishing

When the sandbox blocks branch/push operations (detached HEAD in an externally managed worktree), the agent commits all work and informs the user to use the App's native controls:

- **"Create branch"** — names the branch, then commit/push/PR via App UI
- **"Hand off to local"** — transfers work to the user's local checkout

The agent can still run tests, stage files, and output suggested branch names, commit messages, and PR descriptions for the user to copy.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Configuração

*   Verifique se o arquivo `config.toml` existe e está correto antes de prosseguir.
*   Certifique-se de que a feature `multi_agent` esteja habilitada.

### Erros de Ambiente

*   Se o comando `git rev-parse --git-dir` falhar, verifique se o repositório Git está corretamente configurado.
*   Se o comando `git branch --show-current` retornar um erro, verifique se o HEAD está detached ou se há problemas com o repositório.

### Erros de Subagentes

*   Se um subagente falhar durante a execução, verifique os logs para identificar a causa raiz do problema.
*   Certifique-se de que os subagentes sejam fechados corretamente após a conclusão do trabalho.

### Erros de Comunicação

*   Se houver problemas de comunicação entre o agente e o App, verifique a conectividade de rede e os logs do App.
*   Certifique-se de que as mensagens sejam enviadas e recebidas corretamente.

### Edge Cases

*   Se o usuário estiver trabalhando em um repositório com permissões restritas, certifique-se de que o agente tenha as permissões necessárias para executar as ações.
*   Se o repositório estiver muito grande, considere otimizar o processo de criação de worktrees e finalização de branches para evitar problemas de desempenho.