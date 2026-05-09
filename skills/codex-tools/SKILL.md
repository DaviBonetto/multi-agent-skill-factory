# Codex Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Codex equivalent |
|-----------------|------------------|
| `Task` tool (dispatch subagent) | `spawn_agent` (see [Subagent dispatch requires multi-agent support](#subagent-dispatch-requires-multi-agent-support)) |
| Multiple `Task` calls (parallel) | Multiple `spawn_agent` calls |
| Task returns result | `wait_agent` |
| Task completes automatically | `close_agent` to free slot |
| `TodoWrite` (task tracking) | `update_plan` |
| `Skill` tool (invoke a skill) | Skills load natively — just follow the instructions |
| `Read`, `Write`, `Edit` (files) | Use your native file tools |
| `Bash` (run commands) | Use your native shell tools |

## Subagent dispatch requires multi-agent support

Add to your Codex config (`~/.codex/config.toml`):

```toml
[features]
multi_agent = true
```

This enables `spawn_agent`, `wait_agent`, and `close_agent` for skills like `dispatching-parallel-agents` and `subagent-driven-development`.

Legacy note: Codex builds before `rust-v0.115.0` exposed spawned-agent
waiting as `wait`. Current Codex uses `wait_agent` for spawned agents. The
`wait` name now belongs to code-mode `exec/wait`, which resumes a yielded exec
cell by `cell_id`; it is not the spawned-agent result tool.

## Environment Detection

Skills that create worktrees or finish branches should detect their
environment with read-only git commands before proceeding:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

- `GIT_DIR != GIT_COMMON` → already in a linked worktree (skip creation)
- `BRANCH` empty → detached HEAD (cannot branch/push/PR from sandbox)

See `using-git-worktrees` Step 0 and `finishing-a-development-branch`
Step 1 for how each skill uses these signals.

## Codex App Finishing

When the sandbox blocks branch/push operations (detached HEAD in an
externally managed worktree), the agent commits all work and informs
the user to use the App's native controls:

- **"Create branch"** — names the branch, then commit/push/PR via App UI
- **"Hand off to local"** — transfers work to the user's local checkout

The agent can still run tests, stage files, and output suggested branch
names, commit messages, and PR descriptions for the user to copy.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Configuração

*   Verifique se o arquivo `~/.codex/config.toml` existe e se a chave `multi_agent` está definida como `true`.
*   Se o arquivo não existir, crie-o e adicione a chave `multi_agent` com valor `true`.

### Erros de Execução

*   Se ocorrer um erro durante a execução de um skill, verifique os logs para identificar a causa do erro.
*   Se o erro for relacionado à falta de permissões, verifique se o usuário tem as permissões necessárias para executar o skill.

### Edge Cases

*   **Detached HEAD**: se o sandbox estiver em um estado de detached HEAD, o agente não poderá criar branches ou fazer push. Nesse caso, o agente deve informar o usuário para usar os controles nativos do App.
*   **Worktree vinculado**: se o sandbox estiver em um worktree vinculado, o agente não deve criar um novo worktree. Em vez disso, o agente deve usar o worktree existente.
*   **Falta de recursos**: se o sandbox não tiver recursos suficientes (por exemplo, memória ou CPU) para executar um skill, o agente deve informar o usuário e solicitar que ele aloque mais recursos.

### Tratamento de Exceções

*   **Try-except**: use blocos try-except para capturar e tratar exceções que ocorram durante a execução de um skill.
*   **Logging**: use logs para registrar erros e exceções, para que possam ser analisados e resolvidos posteriormente.

Exemplo de tratamento de exceções:
```python
try:
    # Executar o skill
    spawn_agent()
except Exception as e:
    # Registrar o erro no log
    logging.error(f"Erro ao executar o skill: {e}")
    # Informar o usuário sobre o erro
    print(f"Erro ao executar o skill: {e}")
