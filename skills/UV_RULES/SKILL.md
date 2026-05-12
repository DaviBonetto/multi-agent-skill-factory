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
   Certifique-se de que as dependências sejam especificadas corretamente e que o Python tenha a versão mínima requerida.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não pode ser instalada via `uv run`, forneça instruções claras sobre como instalá-la.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar ativar um ambiente virtual, forneça instruções sobre como fazer isso de forma segura.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja mantido consistente.

6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências sejam especificadas corretamente e que o ambiente seja configurado para o trabalho.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: certifique-se de que os scripts tratam erros de forma adequada, como exceções de dependências não instaladas ou erros de execução.
* **Edge cases**: considere casos de bordo, como:
 + Dependências não instaladas ou desatualizadas.
 + Erros de sintaxe ou execução.
 + Ambientes virtuais não ativados ou configurados incorretamente.
 + Compatibilidade com diferentes versões do Python ou dependências.
* **Segurança**: certifique-se de que os scripts não contenham vulnerabilidades de segurança, como:
 + Injeção de comandos ou SQL.
 + Uso de dependências desatualizadas ou vulneráveis.
 + Acesso não autorizado a recursos ou dados.
* **Testes**: certifique-se de que os scripts sejam testados adequadamente, incluindo testes de unidade, integração e edge cases.
* **Documentação**: certifique-se de que a documentação seja clara e concisa, incluindo instruções sobre como executar os scripts, dependências necessárias e tratamento de erros.