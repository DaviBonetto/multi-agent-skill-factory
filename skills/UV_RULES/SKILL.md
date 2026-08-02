# UV Rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e estejam de acordo com as políticas de segurança do projeto.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam gerenciadas corretamente e que o ambiente esteja configurado para execução.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
   Em casos de exceção, certifique-se de que o motivo seja claro e que as instruções sejam precisas.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se um ambiente virtual for necessário, use `uv` para gerenciá-lo.

5. **Se um exemplo de instalação manual for verdadeiramente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências específicas do Hugging Face sejam respeitadas.

## ⚠️ Tratamento de Exceções e Edge Cases
### Dependências Conflitantes
- **Verifique as versões de dependências**: Antes de adicionar uma nova dependência, verifique se ela não entra em conflito com as dependências existentes.
- **Use especificadores de versão**: Sempre especifique a versão das dependências para evitar problemas de compatibilidade.

### Erros de Execução
- **Trate erros de execução**: Use blocos try-except para tratar erros de execução e fornecer mensagens de erro significativas.
- **Registre erros**: Registre erros para facilitar o debug e a resolução de problemas.

### Segurança
- **Validação de Entrada**: Valide todas as entradas de usuário para prevenir ataques de injeção e cross-site scripting (XSS).
- **Uso de Bibliotecas Seguras**: Certifique-se de que as bibliotecas utilizadas estejam atualizadas e sejam consideradas seguras.
- **Autenticação e Autorização**: Implemente mecanismos de autenticação e autorização adequados para proteger acessos não autorizados.

### Ambientes de Desenvolvimento
- **Use Ambientes Virtuais**: Use ambientes virtuais para isolar dependências do projeto e evitar poluição do ambiente global.
- **Configure o Ambiente**: Certifique-se de que o ambiente esteja configurado corretamente para o projeto, incluindo variáveis de ambiente e configurações específicas.