# Gemini CLI Tool Mapping

Skills use Claude Code tool names. When you encounter these in a skill, use your platform equivalent:

| Skill references | Gemini CLI equivalent |
|-----------------|----------------------|
| `Read` (file reading) | `read_file` |
| `Write` (file creation) | `write_file` |
| `Edit` (file editing) | `replace` |
| `Bash` (run commands) | `run_shell_command` |
| `Grep` (search file content) | `grep_search` |
| `Glob` (search files by name) | `glob` |
| `TodoWrite` (task tracking) | `write_todos` |
| `Skill` tool (invoke a skill) | `activate_skill` |
| `WebSearch` | `google_web_search` |
| `WebFetch` | `web_fetch` |
| `Task` tool (dispatch subagent) | No equivalent — Gemini CLI does not support subagents |

## No subagent support

Gemini CLI has no equivalent to Claude Code's `Task` tool. Skills that rely on subagent dispatch (`subagent-driven-development`, `dispatching-parallel-agents`) will fall back to single-session execution via `executing-plans`.

## Additional Gemini CLI tools

These tools are available in Gemini CLI but have no Claude Code equivalent:

| Tool | Purpose |
|------|---------|
| `list_directory` | List files and subdirectories |
| `save_memory` | Persist facts to GEMINI.md across sessions |
| `ask_user` | Request structured input from the user |
| `tracker_create_task` | Rich task management (create, update, list, visualize) |
| `enter_plan_mode` / `exit_plan_mode` | Switch to read-only research mode before making changes |

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de sintaxe

*   Verifique se os comandos estão corretamente formatados e se os parâmetros estão sendo passados corretamente.
*   Trate erros de sintaxe como exceções e forneça mensagens de erro claras e concisas.

### Erros de permissão

*   Verifique se o usuário tem as permissões necessárias para executar os comandos.
*   Trate erros de permissão como exceções e forneça mensagens de erro claras e concisas.

### Erros de arquivo

*   Verifique se os arquivos existem e se podem ser lidos ou escritos.
*   Trate erros de arquivo como exceções e forneça mensagens de erro claras e concisas.

### Edge cases

*   Verifique se os comandos funcionam corretamente com entradas inválidas ou edge cases.
*   Trate edge cases como exceções e forneça mensagens de erro claras e concisas.

### Exemplos de tratamento de exceções

```markdown
try:
    # Código que pode gerar exceção
    read_file("arquivo.txt")
except FileNotFoundError:
    # Tratamento de exceção
    print("Arquivo não encontrado")
except PermissionError:
    # Tratamento de exceção
    print("Permissão negada")
```

### Segurança

*   Verifique se os comandos estão sendo executados de forma segura e se os dados estão sendo tratados corretamente.
*   Use criptografia e autenticação para proteger os dados e os comandos.

### Exemplos de segurança

```markdown
import hashlib

# Criptografia de senha
senha = "minha_senha"
senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

# Autenticação
if senha_criptografada == "senha_criptografada_armazenada":
    # Acesso concedido
    print("Acesso concedido")
else:
    # Acesso negado
    print("Acesso negado")
