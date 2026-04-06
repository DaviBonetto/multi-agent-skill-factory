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
- Verificar se o código lida corretamente com exceções e erros, como:
  - Tratamento de erros de entrada e saída
  - Lidar com condições de erro inesperadas
  - Uso de mecanismos de retry e fallback quando necessário
- Verificar se o código considera casos de bordo, como:
  - Valores nulos ou vazios
  - Valores extremos ou fora do intervalo esperado
  - Condições de concorrência e paralelismo
- Verificar se o código segue as melhores práticas de segurança, como:
  - Validar e sanitizar entradas de usuário
  - Proteger contra injeção de código e ataques de cross-site scripting (XSS)
  - Utilizar criptografia e autenticação adequadas quando necessário

**Segurança**
- Verificar se o código segue as políticas de segurança da empresa
- Verificar se o código utiliza bibliotecas e dependências seguras e atualizadas
- Verificar se o código lida corretamente com dados sensíveis, como informações de autenticação e criptografia

**Code reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment, incluindo:
- Relatório de segurança e tratamento de exceções
- Recomendações para melhorias de segurança e tratamento de exceções