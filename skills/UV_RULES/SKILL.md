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
   Isso garante que as dependências sejam carregadas corretamente e que o script seja executado no ambiente correto.

3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico para isso. O uso normal não deve exigir instalação manual.
   Se uma instalação manual for necessária, use `uv pip install ...` em vez de `pip install -r requirements.txt`.

4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
   Se o usuário precisar ativar um ambiente virtual, use `uv run` com a opção `--venv` para especificar o ambiente virtual.

5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
   Isso garante que as dependências sejam instaladas corretamente e que o script seja executado no ambiente correto.

6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.
   Isso garante que o script seja executado no ambiente correto e com as dependências necessárias.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
* Certifique-se de que os scripts lidem com erros e exceções de forma apropriada.
* Use `try`-`except` para capturar erros e fornecer mensagens de erro úteis.
* Registre os erros para que possam ser analisados e resolvidos.

### Edge Cases
* Certifique-se de que os scripts lidem com casos de bordo, como:
 + Entradas inválidas ou malformadas.
 + Dependências ausentes ou desatualizadas.
 + Ambientes de execução não suportados.
* Forneça mensagens de erro claras e úteis para ajudar os usuários a resolver problemas.

### Segurança
* Certifique-se de que os scripts sigam as práticas de segurança recomendadas, como:
 + Validar entradas de usuário para evitar injeção de código.
 + Usar criptografia para proteger dados sensíveis.
 + Manter as dependências atualizadas para evitar vulnerabilidades de segurança.
* Use ferramentas de análise de segurança para identificar e corrigir vulnerabilidades.