# UV rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Lembre-se de que as dependências devem ser especificadas corretamente para evitar erros de importação.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas corretamente e que o ambiente seja configurado adequadamente.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Certifique-se de que as dependências sejam gerenciadas pelo `uv` para evitar conflitos de versão.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência no ambiente de execução e evita problemas de configuração.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o ambiente seja atualizado adequadamente.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso é crucial para garantir que os trabalhos sejam executados no ambiente correto e com as dependências necessárias.

⚠️ Tratamento de Exceções e Edge Cases
### Erros de Dependência
- **Dependências não encontradas**: Certifique-se de que as dependências estejam corretamente especificadas no script e que o `uv` esteja configurado para resolvê-las.
- **Conflitos de Versão**: Use o `uv` para gerenciar as dependências e evitar conflitos de versão. Se um conflito ocorrer, revise as dependências e ajuste-as conforme necessário.

### Erros de Execução
- **Erros de Syntax**: Verifique se o script Python está correto e se não há erros de syntax. O `uv run` pode ajudar a identificar esses erros.
- **Erros de Execução**: Se o script falhar durante a execução, verifique os logs para identificar a causa raiz do problema. Isso pode incluir erros de dependência, problemas de configuração ou bugs no código.

### Segurança
- **Uso de Dependências**: Certifique-se de que as dependências sejam provenientes de fontes confiáveis e estejam atualizadas para evitar vulnerabilidades de segurança.
- **Execução de Scripts**: Tenha cuidado ao executar scripts de fontes desconhecidas, pois eles podem conter código malicioso. Use o `uv run` para garantir que os scripts sejam executados em um ambiente controlado.