# UV Rules
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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver dependências que não possam ser instaladas via `uv run`, forneça uma explicação clara sobre por que a instalação manual é necessária.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o script exigir um ambiente virtual específico, use `uv run` com a opção `--env` para especificar o ambiente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências e o ambiente estejam configurados corretamente para o workload.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: Certifique-se de que os scripts lidem com erros de forma apropriada, como exceções de dependências não encontradas ou erros de execução.
* **Edge cases**: Considere casos de bordo, como entradas inválidas, falta de permissões ou recursos insuficientes, e forneça tratamento adequado para esses casos.
* **Compatibilidade**: Verifique a compatibilidade dos scripts com diferentes versões do Python e dependências para garantir que eles funcionem como esperado em diferentes ambientes.
* **Segurança**: Certifique-se de que os scripts não contenham vulnerabilidades de segurança, como injeção de comandos ou exposição de dados sensíveis.
* **Testes**: Forneça testes adequados para os scripts para garantir que eles funcionem corretamente e lidem com erros de forma apropriada.