# Superpowers for Codex
Guide for using Superpowers with OpenAI Codex via native skill discovery.

## Quick Install

Tell Codex:
```bash
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.codex/INSTALL.md
```

## Manual Installation
### Prerequisites
- OpenAI Codex CLI
- Git
### Steps
1. Clone the repo:
   ```bash
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
```
2. Create the skills symlink:
   ```bash
mkdir -p ~/.agents/skills
ln -s ~/.codex/superpowers/skills ~/.agents/skills/superpowers
```
3. Restart Codex.
4. **For subagent skills** (optional): Skills like `dispatching-parallel-agents` and `subagent-driven-development` require Codex's collab feature. Add to your Codex config:
   ```toml
[features]
collab = true
```
### Windows
Use a junction instead of a symlink (works without Developer Mode):
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
cmd /c mklink /J "$env:USERPROFILE\.agents\skills\superpowers" "$env:USERPROFILE\.codex\superpowers\skills"
```
## How It Works
Codex has native skill discovery — it scans `~/.agents/skills/` at startup, parses SKILL.md frontmatter, and loads skills on demand. Superpowers skills are made visible through a single symlink:
```
~/.agents/skills/superpowers/ → ~/.codex/superpowers/skills/
```
The `using-superpowers` skill is discovered automatically and enforces skill usage discipline — no additional configuration needed.
## Usage
Skills are discovered automatically. Codex activates them when:
- You mention a skill by name (e.g., "use brainstorming")
- The task matches a skill's description
- The `using-superpowers` skill directs Codex to use one
### Personal Skills
Create your own skills in `~/.agents/skills/`:
```bash
mkdir -p ~/.agents/skills/my-skill
```
Create `~/.agents/skills/my-skill/SKILL.md`:
```markdown
---
name: my-skill
description: Use when [condition] - [what it does]
---
# My Skill
[Your skill content here]
```
The `description` field is how Codex decides when to activate a skill automatically — write it as a clear trigger condition.
## Updating
```bash
cd ~/.codex/superpowers && git pull
```
Skills update instantly through the symlink.
## Uninstalling
```bash
rm ~/.agents/skills/superpowers
```
**Windows (PowerShell):**
```powershell
Remove-Item "$env:USERPROFILE\.agents\skills\superpowers"
```
Optionally delete the clone: `rm -rf ~/.codex/superpowers` (Windows: `Remove-Item -Recurse -Force "$env:USERPROFILE\.codex\superpowers"`).
## Troubleshooting
### Skills not showing up
1. Verify the symlink: `ls -la ~/.agents/skills/superpowers`
2. Check skills exist: `ls ~/.codex/superpowers/skills`
3. Restart Codex — skills are discovered at startup
### Windows junction issues
Junctions normally work without special permissions. If creation fails, try running PowerShell as administrator.
## Getting Help
- Report issues: https://github.com/obra/superpowers/issues
- Main documentation: https://github.com/obra/superpowers
## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Permissão
- **Erro ao criar symlink**: Se você encontrar um erro de permissão ao criar o symlink, tente executar o comando com privilégios de administrador.
- **Erro ao acessar diretório**: Se você encontrar um erro de permissão ao acessar o diretório `~/.agents/skills/`, verifique se o diretório existe e se você tem permissão para escrever nele.
### Erros de Configuração
- **Erro ao carregar skills**: Se as skills não estiverem sendo carregadas, verifique se o arquivo `SKILL.md` está correto e se o diretório `~/.agents/skills/` está sendo escaneado corretamente.
- **Erro ao ativar skill**: Se uma skill não estiver sendo ativada, verifique se a descrição da skill está correta e se a condição de ativação está sendo satisfeita.
### Erros de Sistema
- **Erro ao clonar repositório**: Se você encontrar um erro ao clonar o repositório, verifique se o repositório está disponível e se você tem permissão para cloná-lo.
- **Erro ao atualizar skills**: Se você encontrar um erro ao atualizar as skills, verifique se o diretório `~/.codex/superpowers/` está sendo atualizado corretamente.
### Prevenção de Erros
- **Verifique a versão do Codex**: Certifique-se de que você está usando a versão mais recente do Codex.
- **Verifique a configuração do Codex**: Certifique-se de que a configuração do Codex está correta e que as skills estão sendo carregadas corretamente.
- **Teste as skills**: Teste as skills regularmente para garantir que elas estejam funcionando corretamente.