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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python especificada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
   Em caso de necessidade de instalação manual, certifique-se de que o processo esteja bem documentado e que os usuários sejam alertados sobre possíveis riscos.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se um ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências sejam compatíveis com o Hugging Face Jobs.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: Certifique-se de que todos os scripts tenham mecanismos de tratamento de erros adequados para lidar com exceções inesperadas. Isso pode incluir try-except blocks e logging de erros.
* **Dependências não encontradas**: Em caso de dependências não encontradas, o script deve fornecer uma mensagem de erro clara e instruções sobre como resolver o problema.
* **Versões incompatíveis do Python**: Se um script exigir uma versão específica do Python, certifique-se de que o usuário seja notificado se a versão instalada for incompatível.
* **Ambientes virtuais**: Se um script exigir um ambiente virtual específico, certifique-se de que o usuário seja instruído sobre como ativá-lo e usá-lo corretamente.
* **Segurança**: Certifique-se de que todos os scripts sigam as melhores práticas de segurança, incluindo a validação de entradas e a proteção contra injeção de código malicioso.
* **Testes**: Certifique-se de que todos os scripts sejam testados adequadamente antes de serem commitados, incluindo testes de unidade, integração e edge cases.