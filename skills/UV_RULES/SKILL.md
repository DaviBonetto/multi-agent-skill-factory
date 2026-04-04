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
- **Verifique se o Python está instalado**: Antes de executar scripts, certifique-se de que o Python está instalado e configurado corretamente no sistema.
- **Trate erros de dependência**: Se uma dependência especificada não estiver disponível, o script deve lidar com isso de forma elegante, fornecendo mensagens de erro claras e instruções sobre como resolver o problema.
- **Lidar com versões incompatíveis do Python**: Se um script exigir uma versão específica do Python e a versão instalada for incompatível, o script deve informar o usuário sobre a versão necessária e, se possível, fornecer instruções sobre como atualizar ou instalar a versão correta.

### Edge Cases
- **Execução em Ambientes Virtuais**: Certifique-se de que os scripts sejam executados corretamente dentro de ambientes virtuais, lidando com possíveis problemas de isolamento de dependências.
- **Compartilhamento de Scripts**: Se os scripts forem compartilhados entre diferentes projetos ou repositórios, considere a possibilidade de manter uma versão centralizada das dependências e scripts para facilitar a manutenção e atualização.
- **Compatibilidade entre Sistemas Operacionais**: Teste os scripts em diferentes sistemas operacionais para garantir compatibilidade e lidar com quaisquer problemas específicos de plataforma que possam surgir.