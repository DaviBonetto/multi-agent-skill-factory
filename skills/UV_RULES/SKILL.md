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
   Certifique-se de que as dependências sejam especificadas corretamente para evitar erros de importação.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se uma instalação manual for necessária, use `uv pip install ...` em vez de `pip install`.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se um ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que o script seja executado no contexto correto e com as dependências necessárias.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Dependência
- **Dependências não encontradas**: Se uma dependência especificada não for encontrada, o `uv run` falhará. Certifique-se de que todas as dependências sejam corretamente listadas e estejam disponíveis.
- **Versões incompatíveis de Python**: Se o script exigir uma versão específica do Python que não está instalada, o `uv run` falhará. Certifique-se de que a versão do Python necessária esteja instalada e configurada corretamente.

### Erros de Execução
- **Parâmetros inválidos**: Se o script for executado com parâmetros inválidos, ele pode falhar ou produzir resultados inesperados. Certifique-se de que os parâmetros sejam validados e tratados corretamente.
- **Erros de runtime**: Se ocorrer um erro durante a execução do script, ele pode ser necessário lidar com exceções para fornecer feedback útil ao usuário e evitar que o programa termine abruptamente.

### Segurança
- **Injeção de dependências**: Certifique-se de que as dependências sejam especificadas de forma segura para evitar a injeção de dependências maliciosas.
- **Execução de scripts não confiáveis**: Tenha cuidado ao executar scripts de fontes não confiáveis, pois eles podem conter código malicioso. Sempre verifique a origem e a integridade dos scripts antes de executá-los.