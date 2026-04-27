# UV rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências estejam atualizadas e compatíveis com a versão do Python utilizada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, forneça instruções claras sobre como instalá-la manualmente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar ativar um ambiente virtual, forneça instruções sobre como fazer isso de forma segura.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança das dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações do Hugging Face estejam corretas e que o workload esteja devidamente configurado.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

* **Tratamento de erros**: Certifique-se de que todos os scripts tenham tratamento de erros adequado, incluindo try-except blocks e logging de erros.
* **Edge cases**: Considere os casos de bordo para cada script, como entrada inválida, falta de dependências ou problemas de permissão.
* **Dependências conflitantes**: Se houver dependências conflitantes, forneça instruções sobre como resolvê-las.
* **Problemas de compatibilidade**: Se houver problemas de compatibilidade entre diferentes versões de dependências ou Python, forneça instruções sobre como resolvê-los.
* **Segurança**: Certifique-se de que todos os scripts sigam as práticas de segurança recomendadas, incluindo a validação de entrada e a proteção contra injeção de código.