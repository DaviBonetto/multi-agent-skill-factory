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
   Certifique-se de que as dependências sejam especificadas corretamente e que o Python tenha a versão mínima requerida.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, forneça uma explicação clara sobre por que a instalação manual é necessária.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   O uso de `uv run` garante que o ambiente seja ativado corretamente sem a necessidade de comandos adicionais.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar problemas de dependência.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que o comando esteja correto e que as dependências sejam carregadas corretamente.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Dependência
- **Dependência não encontrada**: Se uma dependência especificada não for encontrada, o script deve falhar com uma mensagem de erro clara indicando a dependência que não foi encontrada.
- **Versão incompatível do Python**: Se o script for executado com uma versão do Python incompatível, o script deve falhar com uma mensagem de erro clara indicando a versão mínima requerida do Python.

### Erros de Execução
- **Parâmetros inválidos**: Se o script for executado com parâmetros inválidos, o script deve falhar com uma mensagem de erro clara indicando os parâmetros válidos.
- **Erros de runtime**: Se ocorrer um erro durante a execução do script, o script deve capturar o erro e fornecer uma mensagem de erro clara indicando o que deu errado.

### Segurança
- **Validação de entrada**: O script deve validar todas as entradas para garantir que sejam seguras e não contenham código malicioso.
- **Uso de bibliotecas seguras**: O script deve usar apenas bibliotecas seguras e atualizadas para evitar vulnerabilidades de segurança.

### Edge Cases
- **Execução em ambientes diferentes**: O script deve ser capaz de ser executado em diferentes ambientes, como Linux, Windows e macOS, sem problemas.
- **Limites de recursos**: O script deve ser capaz de lidar com limites de recursos, como memória e CPU, sem falhar.