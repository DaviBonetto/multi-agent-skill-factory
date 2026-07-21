# UV rules
## Introdução
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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver dependências que não podem ser instaladas automaticamente, especifique-as explicitamente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   O uso de `uv run` garante que o ambiente seja ativado corretamente.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja atualizado.

6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.
   Isso garante que os trabalhos sejam executados corretamente e que as dependências sejam carregadas.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as dependências**: antes de executar um script, verifique se as dependências estão instaladas e se a versão do Python é compatível.
- **Trate exceções**: use blocos try-except para tratar exceções que possam ocorrer durante a execução do script.
- **Registre erros**: registre os erros que ocorrem durante a execução do script para que possam ser analisados e corrigidos.

### Edge Cases
- **Versões do Python**: certifique-se de que o script seja compatível com diferentes versões do Python.
- **Ambientes**: certifique-se de que o script seja executado corretamente em diferentes ambientes (por exemplo, Linux, Windows, macOS).
- **Dependências**: certifique-se de que as dependências sejam instaladas corretamente e que o script seja executado com as dependências corretas.

### Segurança
- **Verifique as permissões**: certifique-se de que o script tenha as permissões necessárias para executar as ações necessárias.
- **Use criptografia**: use criptografia para proteger os dados sensíveis.
- **Evite injeção de código**: evite a injeção de código malicioso nos scripts.