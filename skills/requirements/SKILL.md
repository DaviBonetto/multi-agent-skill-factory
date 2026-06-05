# requirements.txt for Spaces
=====================================
...
Exemplo de tratamento de exceções:
```python
try:
    import torch
except ImportError:
    print("Erro de importação do torch")
    # Tratar o erro de importação
```
Exemplo de tratamento de problemas de ABI:
```python
try:
    import torch
    torch.cuda.get_device_name(0)
except RuntimeError:
    print("Erro de ABI")
    # Tratar o erro de ABI
```
