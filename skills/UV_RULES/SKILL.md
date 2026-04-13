# UV Rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Lembre-se de que as dependências devem ser especificadas corretamente para evitar erros de importação.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma necessidade legítima para documentar a instalação manual, certifique-se de explicar claramente o motivo e os passos necessários.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   A ativação manual do ambiente virtual pode levar a problemas de configuração e inconsistências.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de seguir as diretrizes específicas para o uso de Hugging Face com UV para evitar problemas de compatibilidade.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Dependência
- **Erro de versão de Python**: Se o script exigir uma versão específica do Python e o usuário tiver uma versão incompatível, um erro será lançado. Nesse caso, o usuário deve ser instruído a atualizar ou mudar a versão do Python.
- **Dependências faltantes**: Se uma dependência especificada não for encontrada, o script falhará. Certifique-se de que todas as dependências sejam listadas corretamente e estejam disponíveis.

### Erros de Execução
- **Parâmetros inválidos**: Se o script exigir parâmetros específicos e eles não forem fornecidos corretamente, o script deve lidar com isso de forma elegante, fornecendo mensagens de erro claras e úteis.
- **Erros de runtime**: Qualquer erro que ocorra durante a execução do script deve ser tratado e reportado de forma que o usuário possa entender o que deu errado e como possivelmente corrigir.

### Segurança
- **Validação de entrada**: Todos os dados de entrada devem ser validados para prevenir injeção de código malicioso ou outros ataques.
- **Uso de recursos**: O script deve ser projetado para usar recursos de forma eficiente, evitando vazamentos de memória ou outros problemas de desempenho que possam ser explorados.

Ao seguir estas diretrizes e considerar os casos de bordo e tratamento de erros, os scripts Python podem ser mais robustos, seguros e fáceis de usar.