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
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as versões do Python**: Certifique-se de que a versão do Python utilizada seja compatível com as dependências especificadas.
- **Trate exceções de importação**: Implemente tratamento de exceções para lidar com falhas de importação de dependências.
- **Manipule erros de execução**: Use blocos try-except para capturar e lidar com erros durante a execução dos scripts.

### Edge Cases
- **Dependências circulares**: Evite dependências circulares entre scripts e bibliotecas. Se necessário, reestruture o código para evitar essas dependências.
- **Conflitos de versão**: Verifique regularmente as versões das dependências para evitar conflitos de versão entre diferentes scripts ou bibliotecas.
- **Ambientes de desenvolvimento e produção**: Certifique-se de que as configurações e dependências sejam adequadas tanto para ambientes de desenvolvimento quanto de produção, evitando assim problemas de compatibilidade.