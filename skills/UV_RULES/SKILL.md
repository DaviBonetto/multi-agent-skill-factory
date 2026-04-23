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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python utilizada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, forneça instruções claras sobre como instalá-la manualmente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o script exigir um ambiente virtual específico, certifique-se de que as instruções sejam claras e fáceis de seguir.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o script seja executado no ambiente adequado.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as dependências sejam compatíveis com o ambiente de trabalho e que o script seja executado corretamente.

## ⚠️ Tratamento de Exceções e Edge Cases
### Dependências não encontradas
Se uma dependência não for encontrada, certifique-se de que ela esteja listada no arquivo `dependencies` e que a versão do Python seja compatível.
```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
```
Se a dependência ainda não for encontrada, verifique se o arquivo `requirements.txt` está atualizado e se as dependências estão instaladas corretamente.

### Erros de execução
Se ocorrer um erro durante a execução do script, certifique-se de que as dependências estejam instaladas corretamente e que o script esteja sendo executado no ambiente adequado.
```bash
uv run scripts/my_script.py --help
```
Se o erro persistir, verifique o log de erros para identificar a causa raiz do problema.

### Ambientes virtuais
Se o script exigir um ambiente virtual específico, certifique-se de que as instruções sejam claras e fáceis de seguir.
```bash
uv pip install ...
```
Se o ambiente virtual não for encontrado, verifique se o arquivo `requirements.txt` está atualizado e se as dependências estão instaladas corretamente.

### Compatibilidade com o Python
Certifique-se de que a versão do Python seja compatível com as dependências e com o script.
```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
```
Se a versão do Python não for compatível, atualize a versão do Python ou as dependências para garantir a compatibilidade.