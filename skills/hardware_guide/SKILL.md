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
*   **Solução:** Reduzir o tamanho do lote, aumentar a acumulação de gradientes, habilitar o checkpoint de gradientes ou usar precisão mista.
*   **Exemplo:**
    ```python
per_device_train_batch_size=1
gradient_accumulation_steps=8
gradient_checkpointing=True
bf16=True
```
### Erros de Conexão
*   **Solução:** Verificar a conexão de rede, reiniciar o job ou aumentar o tempo de espera.
*   **Exemplo:**
    ```python
timeout=3600  # 1 hora
```
### Erros de Dados
*   **Solução:** Verificar a integridade dos dados, corrigir erros de formatação ou aumentar a tolerância a erros.
*   **Exemplo:**
    ```python
data_validation=True
error_tolerance=0.1
```
### Outros Erros
*   **Solução:** Verificar os logs de erro, reiniciar o job ou aumentar a capacidade de processamento.
*   **Exemplo:**
    ```python
log_level="DEBUG"
max_retries=3
```
Ao tratar exceções e edge cases, é fundamental monitorar os logs de erro, ajustar os parâmetros de treinamento e otimizar a configuração de hardware para garantir a estabilidade e a eficiência do treinamento de modelos.
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