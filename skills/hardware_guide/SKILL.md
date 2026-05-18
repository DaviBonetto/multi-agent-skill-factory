# Hardware Selection Guide
...
## Quick Reference
```python
# Model size → Hardware selection
HARDWARE_MAP = {
    "<1B":     "t4-small",
    "1-3B":    "a10g-small",
    "3-7B":    "a10g-large",
    "7-13B":   "a10g-large (LoRA) or a100-large",
    ">13B":    "a100-large (LoRA required)"
}
```
## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Memória
*   **Solução:** Reduzir o tamanho do lote (`batch_size`) ou aumentar a capacidade de memória do hardware.
*   **Exemplo:** Se estiver usando `t4-small` e estourar a memória, considere mudar para `a10g-small` ou reduzir o `batch_size`.
### Erros de Conexão
*   **Solução:** Verificar a estabilidade da conexão de rede e garantir que os serviços necessários estejam disponíveis.
*   **Exemplo:** Se ocorrer um erro de conexão durante o treinamento, verifique a conexão de rede e tente novamente.
### Erros de Dados
*   **Solução:** Verificar a integridade dos dados e garantir que estejam no formato correto.
*   **Exemplo:** Se ocorrer um erro de dados durante o treinamento, verifique a fonte dos dados e corrija qualquer problema de formatação ou consistência.
### Outros Erros
*   **Solução:** Verificar os logs de erro e documentação para identificar a causa raiz do problema e aplicar a solução apropriada.
*   **Exemplo:** Se ocorrer um erro desconhecido, verifique os logs de erro e a documentação do framework ou biblioteca utilizada para encontrar a solução.
Ao tratar exceções e edge cases, é crucial manter um registro detalhado dos erros e soluções aplicadas para facilitar a depuração e melhoria contínua do processo de treinamento.
[WARNINGS]
- Seja rigoroso. A skill deve estar pronta para um ambiente de produção (Senior level).
- Status deve ser "PASS" se for adequado, ou "FAIL" caso o markdown falhe em ser direto, coeso ou exiba código com falhas notórias.
- Se for FAIL, a propriedade 'fixed_markdown' deve conter a versão corrigida (se for possível corrigir facilmente). Caso não consiga, devolva a string vazia ou o markdown da forma que conseguiu salvar.
- Se for PASS, repita o markdown original em 'fixed_markdown'.
- RETORNE APENAS JSON. Nenhuma palavra a mais.
[RETURN]
Retorne API JSON com o schema exato:
{
   "status": "PASS" ou "FAIL",
   "reasoning": "Breve justificativa",
   "fixed_markdown": "... conteudo final stringified ..."
}