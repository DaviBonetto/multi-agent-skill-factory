# UV Rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e estejam atualizadas para evitar problemas de compatibilidade.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, considere adicionar uma exceção explícita.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar ativar um ambiente virtual, certifique-se de que isso seja feito automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar problemas de dependência.

6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações do Hugging Face estejam corretas e que o script seja compatível com o ambiente de execução.

⚠️ Tratamento de Exceções e Edge Cases
### Erros Comuns
- **Dependências não encontradas**: Certifique-se de que as dependências estejam corretamente especificadas e instaladas.
- **Problemas de compatibilidade de Python**: Verifique se o script está sendo executado com a versão correta do Python.
- **Ambientes virtuais**: Se o script exigir um ambiente virtual específico, certifique-se de que ele seja ativado corretamente.

### Edge Cases
- **Scripts com dependências circulares**: Evite dependências circulares, pois elas podem causar problemas de instalação e execução.
- **Scripts que exigem permissões especiais**: Certifique-se de que os scripts que exigem permissões especiais sejam executados com as devidas permissões e que os usuários sejam informados sobre as implicações de segurança.
- **Scripts que lidam com dados sensíveis**: Certifique-se de que os scripts que lidam com dados sensíveis sejam executados em um ambiente seguro e que os dados sejam tratados de acordo com as políticas de segurança do projeto.

### Melhores Práticas
- **Teste os scripts**: Antes de commitar, teste os scripts para garantir que eles funcionem corretamente e não causem problemas de segurança.
- **Documente os scripts**: Certifique-se de que os scripts sejam bem documentados, incluindo instruções de uso e configuração.
- **Mantenha os scripts atualizados**: Certifique-se de que os scripts sejam mantidos atualizados e compatíveis com as últimas versões das dependências e do Python.