# Code Quality Reviewer Prompt Template
## Purpose
Verify implementation is well-built (clean, tested, maintainable)

**Only dispatch after spec compliance review passes.**

```
Task tool (superpowers:code-reviewer):
  Use template at requesting-code-review/code-reviewer.md

  WHAT_WAS_IMPLEMENTED: [from implementer's report]
  PLAN_OR_REQUIREMENTS: Task N from [plan-file]
  BASE_SHA: [commit before task]
  HEAD_SHA: [current commit]
  DESCRIPTION: [task summary]
```
## In addition to standard code quality concerns, the reviewer should check:
- Does each file have one clear responsibility with a well-defined interface?
- Are units decomposed so they can be understood and tested independently?
- Is the implementation following the file structure from the plan?
- Did this implementation create new files that are already large, or significantly grow existing files? (Don't flag pre-existing file sizes — focus on what this change contributed.)

## Code Reviewer Returns
- Strengths
- Issues (Critical/Important/Minor)
- Assessment

## ⚠️ Tratamento de Exceções e Edge Cases
- Verificar se o código lida corretamente com exceções e erros, incluindo:
  - Tratamento de erros de entrada e saída
  - Manipulação de exceções de forma apropriada
  - Uso de mecanismos de retry e fallback quando necessário
- Verificar se o código considera casos de bordo, incluindo:
  - Valores nulos ou vazios
  - Valores extremos ou inválidos
  - Comportamento em diferentes ambientes e configurações
- Verificar se o código segue as melhores práticas de segurança, incluindo:
  - Validação de entrada de usuário
  - Proteção contra injeção de código
  - Uso de criptografia quando necessário
- Verificar se o código é robusto o suficiente para lidar com:
  - Condições de concorrência
  - Falhas de rede ou de armazenamento
  - Outros tipos de falhas ou exceções que possam ocorrer durante a execução

## Segurança
- Verificar se o código segue as políticas de segurança da empresa
- Verificar se o código usa bibliotecas e dependências seguras e atualizadas
- Verificar se o código lida corretamente com informações sensíveis, como senhas e chaves de criptografia