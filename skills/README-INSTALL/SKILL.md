# ✅ Skills Master - Instalador Automático
## Como Usar
### Instalação Rápida
No diretório do seu projeto, rode:
```powershell
& "C:\\Users\\Davib\\OneDrive\\\u00c1rea de Trabalho\\Skills Master\\install-skills.ps1"
```
Ou, se estiver em outro diretório:
```powershell
& "C:\\Users\\Davib\\OneDrive\\\u00c1rea de Trabalho\\Skills Master\\install-skills.ps1" -TargetPath "C:\\caminho\\do\\seu\\projeto"
```
### O Que Ele Faz
1. ✅ Cria links simbólicos de `skills/` para `.agent/skills/`
2. ✅ Cria links para `GEMINI.md` e `CLAUDE.md`
3. ✅ Mantém tudo sincronizado automaticamente
### Vantagens
- **Uma únnica fonte**: Edite no Skills Master, aparece em todos os projetos
- **Zero duplicação**: Não copia arquivos
- **Atualização automática**: Mudanças aparecem instantaneamente
- **Reversível**: Basta deletar os links
### Exemplo de Uso
```powershell
# Navegue até seu projeto
cd "C:\\Users\\Davib\\OneDrive\\\u00c1rea de Trabalho\\MeuProjeto"
# Rode o instalador
& "C:\\Users\\Davib\\OneDrive\\\u00c1rea de Trabalho\\Skills Master\\install-skills.ps1"
# Pronto! Agora você tem acesso a todas as skills
```
### Verificação
Após rodar, verifique:
```powershell
ls .agent
```
Você deve ver:
- `skills/` (link simbólico)
- `GEMINI.md` (link simbólico)
- `CLAUDE.md` (link simbólico)
### Desinstalação
Para remover os links:
```powershell
Remove-Item .agent\\skills -Force
Remove-Item .agent\\GEMINI.md -Force
Remove-Item .agent\\CLAUDE.md -Force
```
### Requisitos
- Windows com PowerShell
- Permissões de administrador (para criar symlinks)
### Troubleshooting
**Erro de permissão?**
- Rode o PowerShell como Administrador
**Link já existe?**
- O script pula automaticamente
- Para recriar, delete o link existente primeiro
**Skills Master não encontrado?**
- Verifique o caminho em `$SkillsMasterPath` no script
### ⚠️ Tratamento de Exceções e Edge Cases
#### Erros de Permissão
- **Causa**: Falta de permissões de administrador para criar links simbólicos.
- **Solução**: Rode o PowerShell como Administrador.
#### Links Simbólicos Existente
- **Causa**: O link simbólico já existe no diretório de destino.
- **Solução**: Delete o link existente antes de executar o script novamente.
#### Caminho Inválido
- **Causa**: O caminho para o Skills Master ou o diretório de destino é inválido.
- **Solução**: Verifique os caminhos e corrija-os antes de executar o script.
#### Sistema Operacional Incompatível
- **Causa**: O script é projetado para rodar em Windows com PowerShell.
- **Solução**: Utilize um sistema operacional compatível ou adapte o script para o seu sistema operacional.
#### Falha na Criação de Links
- **Causa**: Erros durante a criação dos links simbólicos.
- **Solução**: Verifique as permissões e o caminho de destino. Se o problema persistir, tente criar os links manualmente.
#### Problemas de Sincronização
- **Causa**: Falhas na sincronização automática devido a problemas de permissão ou caminho inválido.
- **Solução**: Verifique as permissões e os caminhos. Certifique-se de que o Skills Master esteja configurado corretamente.
Essas são as principais exceções e edge cases que podem ocorrer durante a utilização do instalador automático do Skills Master. Se você encontrar problemas não listados aqui, por favor, verifique o log de erros e tente solucionar o problema com base nas informações fornecidas.