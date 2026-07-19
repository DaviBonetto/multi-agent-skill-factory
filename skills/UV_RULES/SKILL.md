# UV Rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique a versão do Python**: Antes de executar scripts, certifique-se de que a versão do Python instalada atende aos requisitos especificados em `requires-python`.
- **Dependências não instaladas**: Se uma dependência especificada em `dependencies` não estiver instalada, `uv run` deve falhar com uma mensagem de erro clara, indicando a dependência faltante.
- **Comandos inválidos**: Se um comando `uv` for inválido ou não encontrado, o sistema deve retornar uma mensagem de erro útil, sugerindo comandos válidos ou ações corretivas.

### Edge Cases
- **Multiplos ambientes**: Em casos onde múltiplos ambientes virtuais estão configurados, certifique-se de que `uv run` use o ambiente correto com base nas dependências especificadas.
- **Conflitos de versão**: Se houver conflitos de versão entre dependências, o sistema deve detectar e relatar esses conflitos, sugerindo versões compatíveis ou ações para resolução.
- **Execução em ambientes restritos**: Em ambientes com restrições de segurança, como falta de acesso a internet, `uv run` deve ser capaz de funcionar com dependências pré-instaladas, sem tentar acessar repositórios remotos.