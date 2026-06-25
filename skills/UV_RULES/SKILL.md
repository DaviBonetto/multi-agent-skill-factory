# UV Rules
=====================================================

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
6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
------------------------------------------------

*   **Tratamento de dependências não instaladas**: Certifique-se de que todas as dependências necessárias estejam instaladas antes de executar os scripts. Se uma dependência estiver faltando, o script deve falhar com uma mensagem de erro clara.
*   **Tratamento de erros de sintaxe**: Se um script contiver erros de sintaxe, o `uv run` deve falhar e exibir uma mensagem de erro útil.
*   **Tratamento de erros de execução**: Se um script falhar durante a execução, o `uv run` deve capturar a exceção e exibir uma mensagem de erro clara.
*   **Edge case: scripts com permissões insuficientes**: Se um script precisar de permissões específicas para executar, certifique-se de que o `uv run` forneça uma mensagem de erro clara se as permissões forem insuficientes.
*   **Edge case: scripts com dependências circulares**: Se um script depender de outro script que, por sua vez, depende do primeiro script, o `uv run` deve detectar a dependência circular e falhar com uma mensagem de erro clara.
*   **Segurança**: Certifique-se de que os scripts não contenham vulnerabilidades de segurança conhecidas. Use ferramentas de análise de segurança para identificar e corrigir quaisquer problemas de segurança.