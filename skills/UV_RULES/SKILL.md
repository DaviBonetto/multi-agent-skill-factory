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
   Certifique-se de que as dependências estejam atualizadas e sejam compatíveis com a versão do Python utilizada.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e o ambiente seja configurado de acordo com as regras do repositório.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Em caso de necessidade de instalação manual, considere adicionar uma explicação clara sobre por que essa abordagem é necessária.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência no uso do ambiente virtual e evita problemas de configuração.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas de forma consistente com as regras do repositório.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Essa abordagem padroniza a execução de trabalhos e facilita a gestão de dependências e ambientes.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as versões**: Antes de executar scripts, certifique-se de que as versões do Python e das dependências estão de acordo com as especificações do projeto.
- **Trate exceções**: Implemente tratamento de exceções para lidar com erros inesperados, como falhas de rede ou problemas de permissão.
- **Registre erros**: Registre erros significativos para facilitar a depuração e a resolução de problemas.

### Edge Cases
- **Compatibilidade de Versão**: Considere a compatibilidade de versão ao trabalhar com diferentes ambientes e dependências.
- **Ambientes Virtuais**: Esteja ciente das implicações de usar ambientes virtuais e como eles afetam a execução dos scripts.
- **Dependências Conflitantes**: Verifique regularmente as dependências para evitar conflitos entre diferentes versões de bibliotecas ou frameworks.

### Segurança
- **Atualize Dependências**: Mantenha as dependências atualizadas para garantir que você tenha as últimas correções de segurança.
- **Use Fontes Confiáveis**: Certifique-se de que as dependências sejam baixadas de fontes confiáveis para evitar malware ou código mal-intencionado.
- **Verifique Permissões**: Revise as permissões dos scripts e dependências para garantir que elas não concedam acesso indevido a recursos sensíveis.