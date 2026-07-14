# UV Regras
Use estas regras para scripts Python neste repositório:

1. **Use dependências inline PEP 723** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/meu_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique a versão do Python**: Antes de executar scripts, certifique-se de que a versão do Python instalada atende aos requisitos especificados em `requires-python`.
- **Dependências não encontradas**: Se uma dependência especificada em `dependencies` não for encontrada, o script deve falhar explicitamente com uma mensagem de erro clara, indicando a dependência faltante.
- **Execução de scripts**: Ao executar scripts com `uv run`, certifique-se de que o ambiente esteja configurado corretamente para evitar erros de execução.

### Edge Cases
- **Ambientes Virtuais**: Em ambientes virtuais, certifique-se de que `uv run` esteja usando o ambiente virtual correto. Se o script depender de um ambiente virtual específico, documente claramente como configurá-lo.
- **Requisitos de Sistema**: Se um script exigir recursos ou configurações de sistema específicas (como permissões especiais), documente esses requisitos explicitamente e forneça instruções sobre como satisfazê-los.
- **Compatibilidade entre Versões**: Teste scripts em diferentes versões do Python e documente quaisquer incompatibilidades conhecidas ou limitações devido a mudanças entre versões.