# Code Quality Reviewer Prompt Template

Use this template when dispatching a code quality reviewer subagent.

**Purpose:** Verify implementation is well-built (clean, tested, maintainable)

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

**In addition to standard code quality concerns, the reviewer should check:**
- Does each file have one clear responsibility with a well-defined interface?
- Are units decomposed so they can be understood and tested independently?
- Is the implementation following the file structure from the plan?
- Did this implementation create new files that are already large, or significantly grow existing files? (Don't flag pre-existing file sizes — focus on what this change contributed.)

**Code reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment

 Tratamento de Exceções e Edge Cases
- Verificar se o código lida corretamente com exceções e erros, incluindo:
  - Tratamento de erros de entrada e saída
  - Manipulação de exceções personalizadas
  - Uso de blocos try-catch para evitar crashes inesperados
- Verificar se o código considera casos de bordo, incluindo:
  - Entradas inválidas ou malformadas
  - Condições de limite (por exemplo, arrays vazios, valores nulos)
  - Comportamento em diferentes ambientes e configurações
- Verificar se o código segue as melhores práticas de segurança, incluindo:
  - Validação de entrada de usuário
  - Proteção contra injeção de código
  - Uso de criptografia e autenticação adequadas

**Segurança**
- Verificar se o código segue as políticas de segurança da empresa
- Verificar se o código utiliza bibliotecas e frameworks seguras e atualizadas
- Verificar se o código armazena dados sensíveis de forma segura

**Code reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment, incluindo:
- Relatório de segurança
- Relatório de tratamento de exceções e edge cases
- Recomendações para melhorias de segurança e código