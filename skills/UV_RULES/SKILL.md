# UV Rules
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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente apropriado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se houver dependências que não possam ser instaladas via `uv run`, forneça instruções claras sobre como instalá-las manualmente.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que as cargas de trabalho sejam executadas no ambiente correto e com as dependências necessárias.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros Comuns
- **Dependências não instaladas**: Se uma dependência não estiver instalada, o script falhará. Certifique-se de que todas as dependências estejam listadas no bloco de dependências do script.
- **Versão incompatível do Python**: Se a versão do Python for incompatível com as dependências, o script pode falhar. Verifique a versão do Python antes de executar o script.
- **Ambiente virtual não ativado**: Se o ambiente virtual não estiver ativado, as dependências podem não ser carregadas corretamente. Certifique-se de que o ambiente virtual esteja ativado antes de executar o script.

### Edge Cases
- **Scripts com dependências circulares**: Se dois ou mais scripts tiverem dependências circulares, pode haver problemas de instalação. Nesse caso, é necessário reestruturar as dependências para evitar ciclos.
- **Scripts com dependências opcionais**: Se um script tiver dependências opcionais, é importante documentar claramente como instalá-las e como o script se comportará sem elas.
- **Execução de scripts em ambientes restritos**: Em ambientes com restrições de segurança, como ambientes de produção, é importante testar os scripts antes de executá-los para garantir que eles funcionem corretamente e não causem problemas de segurança.

### Melhores Práticas
- **Teste os scripts regularmente**: Teste os scripts regularmente para garantir que eles funcionem corretamente e não causem problemas de segurança.
- **Documente as dependências**: Documente claramente as dependências de cada script, incluindo as versões necessárias e como instalá-las.
- **Use ambientes virtuais**: Use ambientes virtuais para isolar as dependências de cada script e evitar conflitos.