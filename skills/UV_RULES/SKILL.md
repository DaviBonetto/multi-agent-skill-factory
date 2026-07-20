# UV Rules
=====================================

Use estas regras para scripts Python neste repositório:

1. **Use PEP 723 inline dependencies** em cada script executável:
   ```python
   # /// script
   # requires-python = ">=3.10"
   # dependencies = ["requests"]
   # ///
   ```
   Certifique-se de que as dependências sejam especificadas corretamente e que o Python tenha a versão mínima necessária.

2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
   Isso garante que as dependências sejam carregadas corretamente e que o ambiente seja configurado de acordo com as regras do repositório.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Em caso de necessidade de instalação manual, considere adicionar uma explicação clara sobre por que isso é necessário.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se houver necessidade de ativar um ambiente virtual, considere usar `uv` para gerenciar o ambiente.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a segurança do ambiente de desenvolvimento.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de seguir as diretrizes específicas para trabalhos do Hugging Face para garantir a compatibilidade e a segurança.

⚠️ Tratamento de Exceções e Edge Cases
----------------------------------------

- **Tratamento de Erros**: Certifique-se de que todos os scripts Python incluem tratamento de erros adequado para lidar com exceções inesperadas. Isso pode incluir try-except blocks para capturar e lidar com erros de forma elegante.
- **Dependências Desatualizadas**: Verifique regularmente as dependências para garantir que elas estejam atualizadas e seguras. Dependências desatualizadas podem introduzir vulnerabilidades de segurança.
- **Ambientes Virtuais**: Ao trabalhar com ambientes virtuais, certifique-se de que eles sejam devidamente configurados e ativados quando necessário. Isso ajuda a prevenir conflitos de dependências e garantir a consistência do ambiente.
- **Comandos de Instalação**: Ao fornecer exemplos de instalação, considere incluir opções para lidar com situações de erro, como a instalação falhando devido a permissões inadequadas.
- **Segurança**: Sempre priorize a segurança ao trabalhar com scripts e dependências. Isso inclui verificar a autenticidade das dependências e evitar o uso de dependências não seguras ou desatualizadas.
- **Testes**: Implemente testes para seus scripts para garantir que eles funcionem como esperado em diferentes ambientes e cenários. Isso ajuda a identificar e corrigir problemas antes que eles afetem os usuários.