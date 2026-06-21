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
   Isso garante que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório**, a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não pode ser resolvida por `uv run`, considere adicionar uma exceção explícita.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações do Hugging Face estejam corretas e que o workload seja executado no ambiente adequado.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: Certifique-se de que todos os scripts tenham tratamento de erros adequado, incluindo try-except blocks e logging de erros.
* **Dependências conflitantes**: Se houver dependências conflitantes, considere usar ambientes virtuais separados ou especificar versões explícitas das dependências.
* **Problemas de permissão**: Se houver problemas de permissão, certifique-se de que o script tenha as permissões necessárias para executar e que o usuário tenha as permissões necessárias para executar o script.
* **Edge cases**: Considere edge cases, como entrada inválida, falta de recursos ou condições de rede, e certifique-se de que o script possa lidar com esses casos de forma robusta.
* **Testes**: Certifique-se de que todos os scripts sejam testados adequadamente, incluindo testes unitários e de integração, para garantir que eles funcionem corretamente em diferentes ambientes e condições.