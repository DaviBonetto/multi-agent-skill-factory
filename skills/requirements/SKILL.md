# requirements.txt for Spaces
=====================================
## What's preinstalled (do not list)
## What to list
## Pinning torch
## Torch-family side-car drift
## Prebuilt CUDA wheels — the Blackwell wheels dataset
## Per-package status
## Pattern
## When you need a wheel that's not in the dataset
## Reading a CUDA wheel filename
## Don't pin `xformers`
## Don't pin `spaces`
## Specifically about Python version
## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros de Importação
### Edge Cases de Versão
### Segurança
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