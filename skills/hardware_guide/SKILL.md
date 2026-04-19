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
*   **Solução:** Reduzir o tamanho do lote, aumentar a acumulação de gradientes, habilitar o checkpointing de gradientes ou usar precisão mista.
*   **Exemplo:**
    ```python
per_device_train_batch_size=1
gradient_accumulation_steps=8
gradient_checkpointing=True
bf16=True
```
### Erros de Conexão
*   **Solução:** Verificar a conexão de rede, reiniciar o job ou aumentar o tempo de timeout.
*   **Exemplo:**
    ```python
timeout="4h"
```
### Erros de Dados
*   **Solução:** Verificar a integridade dos dados, corrigir erros de formatação ou aumentar a tolerância a erros.
*   **Exemplo:**
    ```python
data_validation=True
error_tolerance=0.1
```
### Outros Erros
*   **Solução:** Verificar os logs de erro, reiniciar o job ou buscar ajuda adicional.
*   **Exemplo:**
    ```python
logging_level="DEBUG"
```
