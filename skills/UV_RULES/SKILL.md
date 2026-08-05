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
   Certifique-se de que as dependências sejam especificadas corretamente e estejam de acordo com as políticas de segurança do projeto.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas e executadas corretamente dentro do ambiente gerenciado pelo `uv`.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
   Se houver uma necessidade legítima para instalação manual, considere adicionar uma explicação clara sobre por que isso é necessário e como proceder.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente para executar os scripts.
   Se o ambiente virtual for necessário, certifique-se de que o `uv` esteja configurado para usá-lo automaticamente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências específicas do Hugging Face estejam corretas e de acordo com as diretrizes do projeto.

⚠️ Tratamento de Exceções e Edge Cases
---------------------------------------

### Tratamento de Erros

*   Certifique-se de que todos os scripts tenham mecanismos de tratamento de erros adequados para lidar com exceções inesperadas.
*   Use `try-except` blocks para capturar e lidar com erros específicos, como erros de rede ou erros de dependência.
*   Forneça mensagens de erro claras e úteis para ajudar os usuários a diagnosticar e resolver problemas.

### Edge Cases

*   **Dependências conflitantes**: Certifique-se de que as dependências especificadas não entrem em conflito entre si ou com as dependências do projeto.
*   **Versões incompatíveis do Python**: Verifique se os scripts são compatíveis com as versões do Python especificadas e se há necessidade de ajustes para garantir a compatibilidade.
*   **Ambientes de desenvolvimento**: Considere diferentes ambientes de desenvolvimento e certifique-se de que os scripts sejam executados corretamente em cada um deles, incluindo, mas não limitado a, Windows, macOS e Linux.
*   **Limitações de recursos**: Tenha em mente as limitações de recursos (como memória e CPU) e otimize os scripts para executar eficientemente em diferentes configurações de hardware.

Ao seguir essas diretrizes e considerar os casos de bordo e o tratamento de erros, você pode garantir que os scripts sejam robustos, seguros e fáceis de usar.