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
6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
------------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts Python tenham um bloco `try-except` para capturar e lidar com exceções inesperadas.
* Use `logging` para registrar erros e exceções, em vez de apenas imprimir mensagens de erro.
* Considere usar uma biblioteca de tratamento de erros, como `errorhandler`, para ajudar a lidar com exceções.

### Edge Cases

* **Versões de Python**: Certifique-se de que os scripts sejam compatíveis com as versões de Python especificadas no arquivo `requires-python`.
* **Dependências**: Verifique se as dependências especificadas no arquivo `dependencies` estão corretas e atualizadas.
* **Ambientes**: Certifique-se de que os scripts sejam executados em ambientes compatíveis, como Linux, Windows ou macOS.
* **Entrada de Usuário**: Verifique se os scripts lidam corretamente com entrada de usuário inválida ou malformada.
* **Conexões de Rede**: Certifique-se de que os scripts lidem corretamente com falhas de conexão de rede ou timeouts.

### Segurança

* **Validação de Entrada**: Certifique-se de que os scripts validem a entrada de usuário para evitar ataques de injeção de código ou cross-site scripting (XSS).
* **Autenticação**: Verifique se os scripts exigem autenticação adequada para acessar recursos sensíveis.
* **Criptografia**: Certifique-se de que os scripts usem criptografia adequada para proteger dados sensíveis.
* **Atualizações de Segurança**: Mantenha os scripts e dependências atualizados com as últimas atualizações de segurança.