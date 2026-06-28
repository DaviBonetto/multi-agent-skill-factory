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
   uv run scripts/my_script.py --help
   ```
3. **Não documente `pip install -r requirements.txt` para scripts do repositório** a menos que haja um motivo específico de fallback. O uso normal não deve exigir instalação manual.
4. **Não instrua os usuários a `source .venv/bin/activate` para scripts de habilidade.** `uv run` deve ser suficiente.
5. **Se um exemplo de instalação manual for realmente necessário, use `uv pip install ...`**, não `uv add`, a menos que você esteja editando intencionalmente um ambiente gerenciado pelo projeto.
6. **Para Hugging Face Jobs UV workloads, use `hf jobs uv run ...`**.

## Tratamento de Exceções e Edge Cases
----------------------------------------

### Tratamento de Erros

* Certifique-se de que todos os scripts Python incluam tratamento de erros adequado para lidar com exceções inesperadas.
* Use blocos `try-except` para capturar e lidar com erros específicos, como erros de rede ou erros de arquivo.
* Registre os erros de forma apropriada para facilitar a depuração e o monitoramento.

### Edge Cases

* Considere os casos de bordo para cada script, como:
 + Entradas inválidas ou malformadas.
 + Condições de limite, como tamanhos de arquivo muito grandes ou muito pequenos.
 + Condições de erro, como falta de permissão ou recursos insuficientes.
* Desenvolva testes para cobrir esses casos de bordo e garantir que os scripts se comportem como esperado.

### Segurança

* Certifique-se de que todos os scripts Python sigam as práticas de segurança recomendadas, como:
 + Validar e sanitizar entradas de usuário.
 + Usar autenticação e autorização adequadas para proteger recursos sensíveis.
 + Manter os pacotes e dependências atualizados para evitar vulnerabilidades de segurança conhecidas.
* Use ferramentas de análise de segurança para identificar e corrigir vulnerabilidades potenciais nos scripts.