# UV rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e estejam atualizadas para evitar problemas de compatibilidade.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve requerer instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, certifique-se de documentar claramente o motivo e as etapas necessárias.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o script precisar de um ambiente virtual específico, use `uv run` com a opção `--venv` para especificar o ambiente.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o script seja executado no ambiente adequado.

6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências sejam especificadas corretamente e que o script seja executado no ambiente adequado.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: Certifique-se de que os scripts tratam erros e exceções corretamente. Use `try`-`except` para capturar erros e fornecer mensagens de erro claras e úteis.
* **Dependências não encontradas**: Se uma dependência não for encontrada, certifique-se de que o script forneça uma mensagem de erro clara e útil. Use `uv run` com a opção `--dependencies` para especificar as dependências necessárias.
* **Ambientes virtuais**: Se um script precisar de um ambiente virtual específico, use `uv run` com a opção `--venv` para especificar o ambiente. Certifique-se de que o ambiente virtual seja criado e ativado corretamente.
* **Compatibilidade**: Certifique-se de que os scripts sejam compatíveis com diferentes versões do Python e de dependências. Use `requires-python` para especificar a versão mínima do Python necessária.
* **Segurança**: Certifique-se de que os scripts sejam seguros e não contenham vulnerabilidades conhecidas. Use `uv run` com a opção `--security` para verificar a segurança do script.