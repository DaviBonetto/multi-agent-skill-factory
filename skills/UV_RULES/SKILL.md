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
2. **Execute scripts com `uv run`**, não `python ...`:
   ```bash
   uv run scripts/my_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para cargas de trabalho UV do Hugging Face Jobs, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique as versões do Python**: Certifique-se de que a versão do Python especificada nas dependências inline seja compatível com a versão do Python instalada no ambiente de execução.
- **Trate exceções de dependência**: Implemente tratamento de exceções para lidar com situações em que as dependências especificadas não podem ser resolvidas ou instaladas.
- **Manipule erros de execução**: Implemente mecanismos para capturar e relatar erros que ocorrem durante a execução dos scripts, fornecendo informações úteis para depuração.

### Edge Cases
- **Ambientes de Desenvolvimento e Produção**: Considere as diferenças entre ambientes de desenvolvimento e produção, garantindo que as dependências e configurações sejam apropriadas para cada caso.
- **Compatibilidade entre Versões**: Verifique a compatibilidade entre diferentes versões de dependências e bibliotecas, especialmente quando há atualizações ou mudanças significativas.
- **Restrições de Segurança**: Implemente restrições de segurança adequadas, como validação de entrada e saída, para prevenir vulnerabilidades nos scripts.

## Conclusão
Ao seguir estas regras e considerar os tratamentos de exceções e edge cases, você pode garantir que seus scripts Python sejam robustos, seguros e fáceis de manter. Lembre-se de sempre testar seus scripts em diferentes ambientes e cenários para garantir a compatibilidade e a confiabilidade.