# UV Rules
=====================================

Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e que o Python tenha a versão mínima necessária.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser resolvida automaticamente, considere adicionar uma explicação sobre como instalá-la manualmente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas no ambiente correto.

6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente correto.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: certifique-se de que os scripts tratam erros e exceções adequadamente. Use `try`-`except` para capturar erros e forneça mensagens de erro claras e úteis.
* **Dependências não resolvidas**: se uma dependência não puder ser resolvida, forneça uma mensagem de erro clara e instruções sobre como instalá-la manualmente.
* **Versões incompatíveis do Python**: se o script exigir uma versão específica do Python, certifique-se de que o `requires-python` seja definido corretamente e que o script seja executado na versão correta do Python.
* **Ambientes virtuais**: se o script exigir um ambiente virtual, certifique-se de que ele seja ativado automaticamente pelo `uv run`.
* **Cargas de trabalho UV do Hugging Face Jobs**: se o script for executado em um ambiente de carga de trabalho UV do Hugging Face Jobs, certifique-se de que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente correto.