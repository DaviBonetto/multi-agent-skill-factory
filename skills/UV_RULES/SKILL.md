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
   Lembre-se de que as dependências devem ser especificadas corretamente para evitar erros de compatibilidade.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Certifique-se de que as dependências sejam gerenciadas corretamente pelo `uv run`.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência e evitar erros de ambiente.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e evita conflitos.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso é crucial para garantir a compatibilidade e o funcionamento correto dos trabalhos.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros de dependência**: Certifique-se de que as dependências sejam especificadas corretamente e que haja um plano para lidar com erros de dependência, como versões incompatíveis ou pacotes faltando.
* **Erros de execução**: Implemente tratamento de erros para lidar com erros de execução, como exceções não capturadas ou saídas inesperadas.
* **Edge cases de ambiente**: Considere edge cases de ambiente, como diferentes versões do Python ou ambientes de desenvolvimento versus produção, e certifique-se de que os scripts sejam robustos o suficiente para lidar com essas variações.
* **Segurança**: Sempre considere a segurança ao executar scripts, especialmente quando lidando com dependências externas ou acesso a recursos sensíveis. Use práticas de segurança recomendadas, como validação de entrada e saída, e siga as diretrizes de segurança do projeto.
* **Testes e validação**: Implemente testes e validação para garantir que os scripts sejam executados corretamente e produzam os resultados esperados, mesmo em edge cases ou condições de erro.