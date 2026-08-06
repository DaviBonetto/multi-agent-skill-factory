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
   Em vez disso, use `uv run` para garantir que as dependências sejam gerenciadas corretamente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência e a evitar problemas de ambiente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a segurança e a consistência das dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que os trabalhos sejam executados corretamente e que as dependências sejam gerenciadas de forma adequada.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as versões do Python e das dependências**: antes de executar um script, certifique-se de que a versão do Python e das dependências estejam atualizadas e sejam compatíveis.
- **Trate exceções**: use blocos try-except para tratar exceções que possam ocorrer durante a execução do script, como erros de dependência ou problemas de ambiente.
- **Forneça mensagens de erro claras**: certifique-se de que as mensagens de erro sejam claras e úteis para ajudar os usuários a diagnosticar e resolver problemas.

### Edge Cases
- **Execução em ambientes diferentes**: considere como o script se comportará em diferentes ambientes, como Windows, macOS ou Linux.
- **Dependências conflitantes**: verifique se as dependências especificadas podem causar conflitos com outras dependências ou bibliotecas.
- **Problemas de permissão**: considere como o script lidará com problemas de permissão, como falta de acesso a arquivos ou diretórios.
- **Limitações de recursos**: considere como o script se comportará em ambientes com recursos limitados, como memória ou processamento insuficientes.

Ao seguir essas regras e considerar os casos de bordo e tratamento de erros, você pode garantir que seus scripts sejam robustos, seguros e fáceis de usar.