# Claude Code Tool Mapping

Skills speak in actions ("dispatch a subagent", "create a todo", "read a file"). On Claude Code these resolve to the tools below.

## Tools

| Action skills request | Claude Code tool |
|----------------------|------------------|
| Read a file | `Read` |
| Create a new file | `Write` |
| Edit a file | `Edit` |
| Run a shell command | `Bash` |
| Search file contents | `Grep` |
| Find files by name | `Glob` |
| Fetch a URL | `WebFetch` |
| Search the web | `WebSearch` |
| Invoke a skill | `Skill` |
| Dispatch a subagent (`Subagent (general-purpose):` template) | `Agent` (older releases named this `Task`) |
| Multiple parallel dispatches | Multiple `Agent` calls in one response |
| Task tracking ("create a todo", "mark complete") | `TaskCreate`, `TaskUpdate`, `TaskList`, `TaskGet`; `TodoWrite` in `claude -p` / Agent SDK unless `CLAUDE_CODE_ENABLE_TASKS=1` is set |
| Background-process / subagent lifecycle (read output, cancel) | `TaskOutput`, `TaskStop` — these are distinct from the todo tools above and apply to running shells, agents, and remote sessions |

## Instructions file

When a skill mentions "your instructions file", on Claude Code this is **`CLAUDE.md`**. Claude Code walks up the directory tree from the current working directory and concatenates every `CLAUDE.md` and `CLAUDE.local.md` it finds along the way. Standard locations:

| Scope | Location |
|-------|----------|
| Project (team-shared) | `./CLAUDE.md` or `./.claude/CLAUDE.md` |
| User global | `~/.claude/CLAUDE.md` |
| Local-private (gitignored) | `./CLAUDE.local.md` |
| Managed policy (org-wide) | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux/WSL), `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) |

CLAUDE.md files can pull in additional content with `@path/to/file` imports (relative or absolute, max five hops deep). Subdirectory `CLAUDE.md` files are also discovered automatically and loaded on-demand when Claude Code reads files in those subdirectories.

Claude Code does **not** read `AGENTS.md` directly. If a project already maintains `AGENTS.md` for other agents, import it from `CLAUDE.md` so both runtimes share the same instructions:

```markdown
@AGENTS.md

## Claude Code

(Claude-Code-specific instructions go here.)
```

For path-scoped rules and larger-project organization, see `.claude/rules/` (rules can be scoped to specific files via `paths` frontmatter and load on demand).

## Personal skills directory

User-level skills live at **`~/.claude/skills/`**. Each skill is a subdirectory containing a `SKILL.md` (with `name` and `description` frontmatter) plus any supporting files. Claude Code does not currently recognize the cross-runtime `~/.agents/skills/` path that Codex, Copilot CLI, and Gemini CLI read; if you're relying on cross-runtime support in the future, verify against the [official skills docs](https://code.claude.com/docs/en/skills).

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Arquivo

*   Se o arquivo `CLAUDE.md` não for encontrado, Claude Code irá procurar por ele em locais padrão.
*   Se o arquivo `CLAUDE.md` for encontrado, mas estiver vazio ou corrompido, Claude Code irá ignorá-lo e continuar com a execução.
*   Se o arquivo `CLAUDE.md` contiver imports inválidos, Claude Code irá lançar um erro e parar a execução.

### Erros de Rede

*   Se houver um erro de conexão ao tentar fetchar uma URL, Claude Code irá lançar um erro e parar a execução.
*   Se o servidor não responder, Claude Code irá aguardar por um tempo determinado antes de lançar um erro.

### Erros de Permissão

*   Se o usuário não tiver permissão para ler ou escrever em um arquivo, Claude Code irá lançar um erro e parar a execução.
*   Se o usuário não tiver permissão para executar um comando, Claude Code irá lançar um erro e parar a execução.

### Outros Erros

*   Se ocorrer um erro inesperado, Claude Code irá lançar um erro e parar a execução.
*   Se o usuário fornecer um input inválido, Claude Code irá lançar um erro e parar a execução.

### Edge Cases

*   Se o usuário tentar criar um arquivo com um nome inválido, Claude Code irá lançar um erro e parar a execução.
*   Se o usuário tentar ler um arquivo que não existe, Claude Code irá lançar um erro e parar a execução.
*   Se o usuário tentar executar um comando que não existe, Claude Code irá lançar um erro e parar a execução.
