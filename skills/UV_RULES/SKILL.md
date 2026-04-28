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
   uv run scripts/meu_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo de fallback específico. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para trabalhos UV do Hugging Face, use `hf jobs uv run ...`**.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erros de Dependência**: Certifique-se de que todas as dependências sejam especificadas corretamente no arquivo de configuração do script. Em caso de erros de dependência, verifique se as versões estão corretas e se as dependências estão instaladas.
- **Erros de Execução**: Se um script falhar durante a execução, verifique os logs para identificar a causa raiz do problema. Isso pode incluir erros de sintaxe, problemas de permissão ou falhas de rede.
- **Erros de Ambiente**: Certifique-se de que o ambiente esteja configurado corretamente antes de executar os scripts. Isso inclui a versão do Python e a presença de dependências necessárias.

### Edge Cases
- **Compatibilidade de Versão**: Certifique-se de que os scripts sejam compatíveis com diferentes versões do Python e de dependências. Isso pode ser alcançado especificando faixas de versão para as dependências.
- **Problemas de Permissão**: Em ambientes com restrições de permissão, certifique-se de que os scripts tenham as permissões necessárias para executar. Isso pode incluir a execução de comandos com privilégios elevados ou a configuração de permissões de arquivo.
- **Limitações de Recursos**: Em ambientes com recursos limitados (como memória ou CPU), otimize os scripts para usar recursos de forma eficiente. Isso pode incluir a otimização de algoritmos ou a utilização de técnicas de processamento em lotes.

### Segurança
- **Validação de Entrada**: Sempre valide as entradas dos usuários para evitar injeção de comandos ou outros ataques de segurança.
- **Uso de Dependências Seguras**: Certifique-se de que todas as dependências sejam obtidas de fontes seguras e confiáveis.
- **Manuseio de Dados Sensíveis**: Se os scripts lidam com dados sensíveis, certifique-se de que eles sejam manuseados de forma segura, usando técnicas como criptografia e anonimização.