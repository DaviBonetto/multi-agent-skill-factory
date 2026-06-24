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
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
------------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts Python tenham um bloco `try-except` para capturar e lidar com exceções inesperadas.
* Use `logging` para registrar erros e exceções para facilitar a depuração.
* Em caso de erros, forneça mensagens de erro claras e úteis para ajudar os usuários a resolver o problema.

### Edge Cases

* **Versões do Python**: Certifique-se de que os scripts sejam compatíveis com as versões do Python especificadas no arquivo `requires-python`.
* **Dependências**: Verifique se as dependências especificadas no arquivo `dependencies` estão instaladas e atualizadas.
* **Ambientes**: Certifique-se de que os scripts sejam executados no ambiente correto (por exemplo, `uv run` em vez de `python ...`).
* **Entrada de Usuário**: Valide a entrada de usuário para evitar erros ou comportamentos inesperados.
* **Limitações de Recursos**: Considere as limitações de recursos (por exemplo, memória, CPU) ao executar scripts em ambientes de produção.

### Exemplos de Tratamento de Exceções

```python
import logging

try:
    # Código que pode gerar uma exceção
    import requests
    resposta = requests.get('https://example.com')
    resposta.raise_for_status()
except requests.RequestException as e:
    logging.error(f"Erro ao fazer requisição: {e}")
    print("Erro ao fazer requisição. Verifique a conexão de rede.")
except Exception as e:
    logging.error(f"Erro inesperado: {e}")
    print("Erro inesperado. Verifique o log para mais informações.")
```
