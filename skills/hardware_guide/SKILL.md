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