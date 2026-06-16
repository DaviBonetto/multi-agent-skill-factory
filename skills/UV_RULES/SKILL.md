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
2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para trabalhos UV do Hugging Face Jobs, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
------------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts tenham tratamento de erros adequado para lidar com exceções inesperadas.
* Use `try`-`except` para capturar e lidar com erros específicos, como erros de rede ou erros de arquivo.
* Registre os erros de forma apropriada para facilitar a depuração.

### Edge Cases

* **Versões de Python**: Certifique-se de que os scripts sejam compatíveis com as versões de Python especificadas no `requires-python`.
* **Dependências**: Verifique se as dependências especificadas no `dependencies` estão instaladas e atualizadas.
* **Ambientes**: Certifique-se de que os scripts sejam executados no ambiente correto, seja com `uv run` ou `hf jobs uv run ...`.
* **Parâmetros**: Verifique se os parâmetros passados para os scripts sejam válidos e estejam dentro dos limites esperados.

### Segurança

* **Validação de Entrada**: Certifique-se de que todos os dados de entrada sejam validados e sanitizados para prevenir ataques de injeção de código.
* **Autenticação**: Verifique se os scripts exigem autenticação adequada para acessar recursos sensíveis.
* **Criptografia**: Use criptografia adequada para proteger dados sensíveis, como senhas ou chaves de API.