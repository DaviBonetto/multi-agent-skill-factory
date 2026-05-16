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
6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique a versão do Python**: Antes de executar scripts, certifique-se de que a versão do Python instalada atende aos requisitos especificados em `requires-python`.
- **Trate exceções de dependência**: Se uma dependência especificada em `dependencies` não for encontrada, o script deve lançar uma exceção clara e útil para o usuário.
- **Manipule erros de execução**: Se um script falhar durante a execução, certifique-se de que o erro seja tratado e uma mensagem de erro útil seja exibida para o usuário.

### Edge Cases
- **Scripts com múltiplas dependências**: Se um script tiver múltiplas dependências, certifique-se de que todas sejam especificadas corretamente em `dependencies` e que o script possa lidar com diferentes versões dessas dependências.
- **Uso de ambientes virtuais**: Embora `uv run` deva ser suficiente, considere como o script se comportará se um usuário estiver usando um ambiente virtual e como isso afetará as dependências e a execução do script.
- **Compatibilidade com diferentes sistemas operacionais**: Se o script for projetado para ser executado em diferentes sistemas operacionais, certifique-se de que as dependências e a lógica do script sejam compatíveis com esses sistemas.