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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python especificada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser resolvida por `uv run`, considere adicionar uma exceção explícita.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o script exigir um ambiente virtual específico, certifique-se de que ele seja criado e ativado automaticamente por `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências específicas do Hugging Face sejam respeitadas e aplicadas corretamente.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

### Erros de Dependência

* Se uma dependência não puder ser resolvida, verifique se a versão do Python é compatível e se a dependência está disponível no repositório.
* Se a dependência for específica do projeto, considere adicionar uma exceção explícita ou atualizar a versão da dependência.

### Erros de Execução

* Se um script falhar durante a execução, verifique os logs para identificar a causa raiz do problema.
* Se o erro for devido a uma dependência não resolvida, atualize a dependência ou adicione uma exceção explícita.

### Edge Cases

* Se um script precisar ser executado em um ambiente específico (por exemplo, um ambiente de teste), certifique-se de que o ambiente seja criado e configurado corretamente antes da execução.
* Se um script precisar acessar recursos externos (por exemplo, uma API), certifique-se de que as credenciais e configurações sejam seguras e respeitem as políticas de segurança do projeto.

### Segurança

* Certifique-se de que todos os scripts sigam as políticas de segurança do projeto e respeitem as melhores práticas de segurança.
* Se um script precisar lidar com dados sensíveis, certifique-se de que os dados sejam protegidos e respeitem as regulamentações de privacidade aplicáveis.