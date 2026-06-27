# UV rules
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
   Isso garante que as dependências sejam resolvidas corretamente e que o script seja executado no ambiente adequado.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
   Em caso de necessidade de instalação manual, considere adicionar uma explicação clara sobre por que isso é necessário.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se houver necessidade de ativar um ambiente virtual, certifique-se de que isso esteja claro na documentação e que haja uma boa razão para isso.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso ajuda a manter a consistência e a evitar conflitos de dependências.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Certifique-se de que as configurações e dependências específicas do Hugging Face estejam corretas e documentadas.

⚠️ Tratamento de Exceções e Edge Cases
### Erros Comuns
- **Dependências não resolvidas**: Certifique-se de que todas as dependências estejam listadas corretamente no bloco de dependências inline.
- **Versões incompatíveis do Python**: Verifique se a versão do Python especificada é compatível com as dependências e o script.
- **Ambientes virtuais**: Se o uso de ambientes virtuais for necessário, documente claramente como ativá-los e use `uv pip install` para instalar dependências dentro do ambiente virtual.
- **Conflitos de dependências**: Ao usar `uv add` ou `uv pip install`, verifique se as dependências adicionadas não entram em conflito com as dependências existentes.
- **Execução de scripts**: Sempre use `uv run` para executar scripts, garantindo que as dependências sejam resolvidas corretamente e o script seja executado no ambiente adequado.

### Edge Cases
- **Scripts com dependências específicas de sistema**: Para scripts que requerem dependências específicas do sistema operacional, considere adicionar instruções para diferentes plataformas.
- **Uso de bibliotecas não padrão**: Se o script usar bibliotecas ou frameworks não padrão, certifique-se de documentar claramente como instalá-los e configurá-los.
- **Limitações de recursos**: Se o script tiver requisitos específicos de recursos (como memória ou CPU), documente essas necessidades para que os usuários possam planejar a execução do script adequadamente.