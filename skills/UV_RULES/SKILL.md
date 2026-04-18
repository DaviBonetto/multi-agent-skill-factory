# UV Rules
Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e que o Python tenha a versão mínima requerida.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam resolvidas corretamente e que o ambiente seja configurado adequadamente.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Em casos onde a instalação manual é necessária, certifique-se de fornecer instruções claras e evitar erros comuns.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Isso ajuda a manter a consistência e evitar problemas de ambiente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a segurança e evitar problemas de dependência.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de seguir as diretrizes específicas para esses casos para garantir a compatibilidade e a segurança.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Dependência
- **Erro de versão do Python**: Certifique-se de que a versão do Python especificada nas dependências inline seja compatível com a versão instalada no sistema.
- **Dependências faltantes**: Antes de executar um script, verifique se todas as dependências necessárias estão instaladas e atualizadas.

### Erros de Execução
- **Parâmetros incorretos**: Forneça ajuda clara e documentação sobre como usar os scripts, incluindo a lista de parâmetros aceitos e exemplos de uso.
- **Erros de ambiente**: Certifique-se de que o ambiente esteja configurado corretamente antes de executar os scripts, especialmente quando se trata de variáveis de ambiente ou configurações específicas.

### Segurança
- **Dependências vulneráveis**: Mantenha as dependências atualizadas e verifique regularmente por vulnerabilidades conhecidas.
- **Dados sensíveis**: Evite expor dados sensíveis, como chaves de API ou credenciais, diretamente nos scripts ou em arquivos de configuração.
- **Permissões de arquivo**: Certifique-se de que os scripts e arquivos de configuração tenham permissões apropriadas para evitar acessos não autorizados.

Ao seguir essas diretrizes e considerar os casos de bordo e tratamento de erros, você pode garantir que os scripts Python sejam executados de forma segura e confiável.