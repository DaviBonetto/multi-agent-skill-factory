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
   Isso garante que as dependências sejam gerenciadas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver uma dependência que não possa ser gerenciada por `uv`, considere adicionar uma exceção claramente documentada.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar de um ambiente virtual, `uv` deve ser capaz de gerenciá-lo automaticamente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações de ambiente e dependências estejam corretas para o workload específico.

## ⚠️ Tratamento de Exceções e Edge Cases
### Dependências Incompatíveis
- **Caso de erro:** Uma dependência especificada não é compatível com a versão do Python utilizada.
- **Tratamento:** Verifique a documentação da dependência para saber quais versões do Python são suportadas e ajuste a especificação de dependência conforme necessário.

### Ambientes Virtuais
- **Caso de erro:** O usuário tem um ambiente virtual ativado que interfere com o funcionamento de `uv run`.
- **Tratamento:** Instrua o usuário a desativar o ambiente virtual antes de executar `uv run`, ou use `uv` para gerenciar o ambiente virtual.

### Erros de Execução
- **Caso de erro:** Um script falha durante a execução devido a uma exceção não capturada.
- **Tratamento:** Revise o código do script para identificar a causa da exceção e adicione tratamento de exceção apropriado para lidar com erros esperados.

### Segurança
- **Caso de erro:** Um script tenta acessar recursos sensíveis sem as devidas permissões.
- **Tratamento:** Verifique as permissões do script e do usuário executando o script, e ajuste as permissões ou o código do script conforme necessário para garantir a segurança.

### Compatibilidade de Versão
- **Caso de erro:** Um script não é compatível com a versão atual de `uv` ou outras dependências.
- **Tratamento:** Verifique a documentação de `uv` e das dependências para saber quais versões são suportadas e atualize o script ou as dependências conforme necessário.