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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente apropriado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve requerer instalação manual.
   Se houver uma dependência que não possa ser instalada via `uv run`, considere adicionar uma exceção com justificativa clara.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se um ambiente virtual for necessário, certifique-se de que ele seja ativado automaticamente pelo `uv run`.

5. **Se um exemplo de instalação manual for verdadeiramente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança das dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências sejam compatíveis com o ambiente de trabalho do Hugging Face.

## ⚠️ Tratamento de Exceções e Edge Cases
### Dependências Conflitantes
- **Tratamento de conflitos de versão**: Se duas ou mais dependências requerem versões diferentes da mesma biblioteca, use `uv run` com a opção `--dependency` para especificar a versão correta.
- **Resolução de dependências**: Se uma dependência não puder ser resolvida, verifique se a versão do Python é compatível e se a dependência está disponível no repositório.

### Erros de Execução
- **Tratamento de erros de execução**: Se um script falhar durante a execução, verifique os logs para identificar a causa raiz. Use `uv run` com a opção `--verbose` para obter mais informações.
- **Dependências não instaladas**: Se uma dependência não estiver instalada, use `uv pip install` para instalá-la antes de executar o script novamente.

### Segurança
- **Validação de entrada**: Certifique-se de que todos os dados de entrada sejam validados e sanitizados para evitar ataques de injeção ou cross-site scripting (XSS).
- **Uso de bibliotecas seguras**: Use apenas bibliotecas e dependências que sejam conhecidas por serem seguras e mantidas atualizadas.
- **Autenticação e autorização**: Implemente mecanismos de autenticação e autorização adequados para proteger os scripts e os dados sensíveis.

Ao seguir estas regras e considerar os casos de bordo e tratamento de erros, você pode garantir que seus scripts Python sejam executados de forma segura e confiável.