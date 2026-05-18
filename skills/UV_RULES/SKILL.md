# UV Rules
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
   Isso garante que as dependências sejam carregadas corretamente e que o ambiente seja configurado adequadamente.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma exceção, certifique-se de documentar claramente o motivo e as etapas necessárias.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o ambiente não for ativado corretamente, verifique se o `uv run` está sendo executado corretamente e se as dependências estão sendo carregadas.

5. **Se um exemplo de instalação manual for necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Certifique-se de que as dependências sejam instaladas corretamente e que o ambiente seja configurado adequadamente.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que as cargas de trabalho sejam executadas corretamente e que as dependências sejam carregadas adequadamente.

⚠️ Tratamento de Exceções e Edge Cases
### Erros Comuns
* **Dependências não encontradas**: se as dependências não forem encontradas, verifique se elas estão corretamente especificadas no arquivo de configuração e se o `uv run` está sendo executado corretamente.
* **Versão do Python incorreta**: se a versão do Python for incorreta, verifique se a versão mínima necessária está especificada corretamente no arquivo de configuração e se o `uv run` está sendo executado corretamente.
* **Ambiente não ativado**: se o ambiente não for ativado corretamente, verifique se o `uv run` está sendo executado corretamente e se as dependências estão sendo carregadas.

### Edge Cases
* **Uso de múltiplas versões do Python**: se múltiplas versões do Python forem necessárias, certifique-se de que as dependências sejam especificadas corretamente para cada versão e que o `uv run` seja executado corretamente para cada versão.
* **Uso de ambientes virtuais**: se ambientes virtuais forem necessários, certifique-se de que eles sejam criados e ativados corretamente e que as dependências sejam instaladas corretamente dentro deles.
* **Uso de dependências não padrão**: se dependências não padrão forem necessárias, certifique-se de que elas sejam especificadas corretamente no arquivo de configuração e que o `uv run` seja executado corretamente.