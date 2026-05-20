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
### Tratamento de Erros de Memória
*   Verifique se o modelo está muito grande para a memória disponível.
*   Use LoRA/PEFT para reduzir o uso de memória.
*   Reduza o tamanho do lote (batch size) para evitar erros de memória.
### Tratamento de Erros de Conexão
*   Verifique a conexão de rede e certifique-se de que o servidor está acessível.
*   Use mecanismos de retry para lidar com erros de conexão temporários.
### Tratamento de Erros de Dados
*   Verifique a integridade dos dados antes de iniciar o treinamento.
*   Use técnicas de pré-processamento de dados para lidar com dados faltantes ou inconsistentes.
### Tratamento de Erros de Hardware
*   Verifique o status do hardware antes de iniciar o treinamento.
*   Use mecanismos de failover para lidar com falhas de hardware.
### Exemplos de Código para Tratamento de Exceções
```python
try:
    # Código que pode gerar exceção
    model = load_model("modelo.pt")
except Exception as e:
    # Tratamento de exceção
    print(f"Erro ao carregar modelo: {e}")
    # Ação alternativa, como carregar um modelo padrão
    model = load_model("modelo_padrao.pt")
```
