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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python utilizada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se uma instalação manual for necessária, use `uv pip install ...` em vez de `pip install -r requirements.txt`.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja mantido consistente.

6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações do Hugging Face estejam corretas e que o trabalho seja executado no ambiente correto.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: certifique-se de que todos os scripts tenham tratamento de erros adequado para lidar com exceções inesperadas.
   Use `try`-`except` para capturar erros e fornecer mensagens de erro úteis para os usuários.
* **Edge cases**: considere os casos de bordo para cada script, como entrada inválida ou dependências ausentes.
   Certifique-se de que os scripts sejam robustos o suficiente para lidar com esses casos e forneçam mensagens de erro úteis quando necessário.
* **Segurança**: certifique-se de que todos os scripts sejam seguros e não contenham vulnerabilidades conhecidas.
   Use dependências atualizadas e siga as melhores práticas de segurança para Python.
* **Testes**: certifique-se de que todos os scripts sejam testados adequadamente para garantir que funcionem corretamente em diferentes ambientes e configurações.
   Use frameworks de teste como `unittest` ou `pytest` para escrever testes unitários e de integração para os scripts.