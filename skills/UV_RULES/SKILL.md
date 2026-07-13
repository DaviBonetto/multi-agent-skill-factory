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
   Em caso de necessidade, forneça instruções claras sobre como proceder.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência e evitar problemas de ambiente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a integridade do ambiente do projeto.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que os trabalhos sejam executados corretamente no ambiente Hugging Face.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as dependências**: Antes de executar um script, verifique se todas as dependências necessárias estão instaladas e atualizadas.
- **Trate exceções**: Use blocos try-except para capturar e tratar exceções que possam ocorrer durante a execução do script.
- **Forneça mensagens de erro claras**: Certifique-se de que as mensagens de erro sejam claras e úteis para o usuário, indicando o que deu errado e como corrigir.

### Edge Cases
- **Versões do Python**: Certifique-se de que o script seja compatível com diferentes versões do Python, especialmente se o script for executado em ambientes com versões diferentes.
- **Ambientes virtuais**: Considere a possibilidade de o script ser executado em ambientes virtuais e certifique-se de que ele funcione corretamente nesses casos.
- **Dependências conflitantes**: Verifique se há dependências conflitantes entre os pacotes utilizados no script e forneça soluções para esses conflitos, se necessário.

### Segurança
- **Use fontes confiáveis**: Certifique-se de que as dependências sejam baixadas de fontes confiáveis para evitar riscos de segurança.
- **Mantenha as dependências atualizadas**: Mantenha as dependências atualizadas para garantir que você tenha as últimas correções de segurança.
- **Use autenticação**: Use autenticação adequada quando necessário, especialmente ao lidar com dados sensíveis ou ao executar scripts em ambientes remotos.