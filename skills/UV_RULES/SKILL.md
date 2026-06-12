# UV rules
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
   Se houver uma necessidade de instalação manual, certifique-se de que isso esteja claro na documentação e que haja uma boa razão para isso.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter o ambiente de execução consistente e evita problemas de configuração.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja configurado de forma consistente.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que os trabalhos sejam executados no ambiente correto e com as dependências necessárias.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------
* **Tratamento de erros**: Certifique-se de que os scripts tratam erros de forma apropriada, utilizando blocos try-except para capturar e lidar com exceções.
* **Edge cases**: Considere os casos de bordo, como entrada inválida, falta de dependências ou problemas de permissão, e certifique-se de que os scripts sejam robustos o suficiente para lidar com esses casos.
* **Dependências não encontradas**: Se uma dependência não for encontrada, o script deve fornecer uma mensagem de erro clara e útil, indicando a dependência que está faltando e como ela pode ser instalada.
* **Problemas de permissão**: Se o script precisar de permissões específicas para executar, certifique-se de que essas permissões sejam configuradas corretamente e que o script forneça uma mensagem de erro clara se as permissões forem insuficientes.
* **Compatibilidade com diferentes versões do Python**: Certifique-se de que os scripts sejam compatíveis com diferentes versões do Python, utilizando recursos e bibliotecas que sejam suportados pelas versões mais comuns do Python.