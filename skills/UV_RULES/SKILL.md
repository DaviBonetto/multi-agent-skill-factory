# UV rules
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
- **Verifique a versão do Python**: Certifique-se de que a versão do Python utilizada atende aos requisitos especificados em `requires-python`.
- **Dependências não encontradas**: Se uma dependência especificada em `dependencies` não for encontrada, o script deve falhar com uma mensagem de erro clara indicando a dependência faltante.
- **Erros de execução**: Se ocorrer um erro durante a execução do script, o erro deve ser tratado e uma mensagem de erro útil deve ser exibida para o usuário.

### Edge Cases
- **Scripts com múltiplas dependências**: Se um script tiver múltiplas dependências, certifique-se de que todas sejam instaladas e configuradas corretamente antes da execução do script.
- **Ambientes virtuais**: Se o script for executado em um ambiente virtual, certifique-se de que as dependências sejam instaladas dentro desse ambiente e não no sistema global.
- **Comandos personalizados**: Se o script exigir comandos personalizados para instalação ou configuração, certifique-se de que esses comandos sejam claros e bem documentados para os usuários.
- **Compatibilidade com diferentes sistemas operacionais**: Se o script for projetado para ser executado em diferentes sistemas operacionais, certifique-se de que as dependências e os comandos sejam compatíveis com cada sistema operacional suportado.