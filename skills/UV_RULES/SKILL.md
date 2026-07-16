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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python especificada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Em casos onde a instalação manual for necessária, certifique-se de fornecer instruções claras e seguras.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência e a segurança no ambiente de execução.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a evitar conflitos de dependências e a manter o ambiente limpo.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de seguir as diretrizes específicas para o Hugging Face Jobs para garantir a compatibilidade e a segurança.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as dependências**: Antes de executar um script, certifique-se de que todas as dependências necessárias estejam instaladas e atualizadas.
- **Trate exceções**: Use blocos try-except para capturar e tratar exceções que possam ocorrer durante a execução do script, fornecendo mensagens de erro claras e úteis.
- **Log de erros**: Implemente um sistema de log de erros para registrar problemas que ocorram durante a execução, ajudando na depuração e resolução de problemas.

### Edge Cases
- **Versões do Python**: Certifique-se de que o script seja compatível com diferentes versões do Python, especialmente se o script for executado em ambientes com versões variadas.
- **Conflitos de dependências**: Antecipe e trate possíveis conflitos de dependências, especialmente quando usar `uv pip install` ou `uv add`.
- **Ambientes virtuais**: Se o script exigir um ambiente virtual específico, forneça instruções claras sobre como configurá-lo e usá-lo com `uv run`.
- **Segurança**: Sempre considere a segurança ao executar scripts, especialmente quando lidar com dados sensíveis ou executar comandos que possam afetar o sistema. Use práticas de segurança recomendadas, como validação de entrada e saída, e evite o uso de comandos perigosos.