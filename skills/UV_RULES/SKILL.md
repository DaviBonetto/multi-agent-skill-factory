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
6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique a versão do Python**: Certifique-se de que a versão do Python especificada nas dependências inline esteja instalada e seja compatível com o script.
- **Trate exceções de dependência**: Implemente tratamento de exceções para lidar com situações em que as dependências não podem ser resolvidas ou instaladas.
- **Manipule erros de execução**: Use try-except para capturar e tratar erros que ocorrem durante a execução do script.

### Edge Cases
- **Scripts com múltiplas dependências**: Se um script tiver várias dependências, certifique-se de que elas sejam todas especificadas corretamente nas dependências inline e que não haja conflitos de versão.
- **Uso de ambientes virtuais**: Se um script exigir um ambiente virtual específico, use `uv pip install` para instalar dependências dentro desse ambiente e evite o uso de `source .venv/bin/activate`.
- **Compatibilidade com diferentes sistemas operacionais**: Teste os scripts em diferentes sistemas operacionais para garantir que eles sejam compatíveis e funcionem como esperado.

### Segurança
- **Validação de entrada**: Sempre valide as entradas do usuário para prevenir ataques de injeção de código ou outros tipos de ataques mal-intencionados.
- **Uso de bibliotecas seguras**: Certifique-se de que as bibliotecas utilizadas sejam seguras e atualizadas, evitando assim vulnerabilidades conhecidas.
- **Proteção de dados sensíveis**: Se o script lidar com dados sensíveis, implemente medidas de proteção adequadas, como criptografia, para garantir a segurança desses dados.