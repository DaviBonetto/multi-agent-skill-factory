# UV rules
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
### Tratamento de Erros
- **Verifique a versão do Python**: Certifique-se de que a versão do Python utilizada é compatível com as dependências especificadas.
- **Trate exceções de dependência**: Implemente tratamento de exceções para lidar com situações em que as dependências não podem ser resolvidas ou instaladas.
- **Manipule erros de execução**: Use try-except para capturar e tratar erros que ocorrem durante a execução dos scripts.

### Edge Cases
- **Scripts com dependências circulares**: Tenha cuidado com scripts que dependem de outros scripts que, por sua vez, dependem do primeiro script, criando um ciclo de dependência.
- **Uso de ambientes virtuais**: Certifique-se de que o uso de ambientes virtuais não interfira com a execução dos scripts ou com a resolução de dependências.
- **Compatibilidade entre sistemas operacionais**: Teste os scripts em diferentes sistemas operacionais para garantir compatibilidade e trate quaisquer exceções que possam surgir devido a diferenças entre os sistemas.