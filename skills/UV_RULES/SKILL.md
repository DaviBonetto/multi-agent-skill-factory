# UV rules
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
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Verifique a versão do Python**: Antes de executar scripts, certifique-se de que a versão do Python instalada atende aos requisitos especificados em `requires-python`.
- **Trate exceções de dependência**: Se uma dependência especificada não estiver instalada, o script deve lidar com essa exceção e fornecer orientações claras sobre como instalar a dependência faltante.
- **Manipule erros de execução**: Os scripts devem capturar e relatar erros de execução de forma clara, ajudando os usuários a identificar e resolver problemas.

### Edge Cases
- **Compatibilidade com diferentes ambientes**: Os scripts devem ser testados em diferentes ambientes (por exemplo, Windows, Linux, macOS) para garantir compatibilidade e funcionamento correto.
- **Limitações de recursos**: Considere limitações de recursos (como memória ou largura de banda) que possam afetar a execução dos scripts e forneça orientações sobre como lidar com esses cenários.
- **Entradas inválidas ou faltantes**: Os scripts devem validar as entradas do usuário e lidar com entradas inválidas ou faltantes de forma robusta, fornecendo feedback útil ao usuário.

### Segurança
- **Validação de entrada**: Valide todas as entradas do usuário para prevenir injeção de comandos ou outros ataques.
- **Uso de dependências seguras**: Certifique-se de que todas as dependências sejam obtidas de fontes seguras e confiáveis.
- **Manipulação de dados sensíveis**: Se os scripts manipulam dados sensíveis, implemente medidas de segurança apropriadas, como criptografia, para proteger esses dados.