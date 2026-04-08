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
2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/meu_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
------------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts Python usem blocos `try-except` para capturar e tratar exceções, garantindo que o programa não termine abruptamente em caso de erros.
* Use `logging` para registrar erros e exceções, permitindo que os desenvolvedores diagnosticem problemas mais facilmente.

### Edge Cases

* **Versões de Python**: Certifique-se de que os scripts sejam compatíveis com diferentes versões do Python, especialmente se o projeto suportar várias versões.
* **Ambientes Virtuais**: Tenha cuidado ao usar ambientes virtuais, pois eles podem afetar a forma como os scripts são executados e as dependências são resolvidas.
* **Sistemas Operacionais**: Considere as diferenças entre sistemas operacionais, como Windows, macOS e Linux, que podem afetar a execução dos scripts.
* **Dependências**: Verifique se as dependências especificadas estão corretas e se são compatíveis com as versões do Python e do sistema operacional utilizados.

### Segurança

* **Validação de Entrada**: Sempre valide as entradas dos usuários para evitar ataques de injeção de código ou outros tipos de ataques mal-intencionados.
* **Uso de Bibliotecas Seguras**: Certifique-se de que as bibliotecas e dependências utilizadas sejam seguras e atualizadas, evitando vulnerabilidades conhecidas.
* **Criptografia**: Use criptografia adequada para proteger dados sensíveis, como senhas e chaves de API.