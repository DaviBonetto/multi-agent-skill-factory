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
----------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts Python incluam tratamento de erros adequados para lidar com exceções inesperadas.
* Use `try-except` blocks para capturar e lidar com erros específicos, como erros de rede ou erros de arquivo.
* Registre os erros de forma apropriada para facilitar a depuração e o monitoramento.

### Edge Cases

* **Versões de Python incompatíveis**: Certifique-se de que os scripts sejam compatíveis com as versões de Python especificadas no arquivo `requires-python`.
* **Dependências faltantes**: Verifique se as dependências especificadas no arquivo `dependencies` estão instaladas e atualizadas antes de executar os scripts.
* **Ambientes de execução**: Certifique-se de que os scripts sejam executados no ambiente correto, seja com `uv run` ou `hf jobs uv run`, dependendo do caso de uso.
* **Parâmetros de linha de comando**: Verifique se os parâmetros de linha de comando são válidos e consistentes com as expectativas do script.
* **Limitações de recursos**: Considere as limitações de recursos, como memória e processamento, ao executar scripts que possam ser intensivos em termos de recursos.

### Segurança

* **Validação de entrada**: Certifique-se de que todos os dados de entrada sejam validados e sanitizados para prevenir ataques de injeção de código ou outros tipos de ataques.
* **Autenticação e autorização**: Implemente autenticação e autorização adequadas para scripts que acessam recursos sensíveis ou executam ações críticas.
* **Criptografia**: Use criptografia adequada para proteger dados sensíveis em trânsito ou em repouso.
* **Atualizações de segurança**: Mantenha os scripts e dependências atualizados com as últimas patches de segurança e correções de vulnerabilidades.