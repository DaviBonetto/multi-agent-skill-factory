# UV rules
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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, certifique-se de documentar o motivo e a solução alternativa.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar ativar um ambiente virtual, certifique-se de que isso seja feito automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja mantido consistente.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências e o ambiente sejam configurados corretamente para o workload.

⚠️ Tratamento de Exceções e Edge Cases
------------------------------------

* **Tratamento de erros**: Certifique-se de que os scripts lidem com erros de forma adequada, como exceções de dependências não instaladas ou erros de execução.
* **Edge cases**: Considere casos de bordo, como:
 + Dependências conflitantes: como lidar com dependências que têm versões incompatíveis.
 + Ambientes virtuais: como lidar com ambientes virtuais que não estão ativados corretamente.
 + Permissões de arquivo: como lidar com permissões de arquivo que impedem a execução do script.
 + Limitações de recursos: como lidar com limitações de recursos, como memória ou CPU, que afetam a execução do script.
* **Testes**: Certifique-se de que os scripts sejam testados adequadamente para garantir que funcionem corretamente em diferentes ambientes e cenários.
* **Documentação**: Certifique-se de que a documentação seja clara e concisa, e forneça informações suficientes para que os usuários possam executar os scripts corretamente.