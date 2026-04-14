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
- Verifique se o código lida corretamente com exceções e erros, incluindo:
  - Tratamento de erros de entrada e saída
  - Manipulação de exceções de forma apropriada
  - Uso de mecanismos de logging para registrar erros e exceções
- Verifique se o código considera casos de bordo, incluindo:
  - Valores de entrada inválidos ou inconsistentes
  - Condições de erro ou exceção não esperadas
  - Comportamento em casos de limite ou extremos (por exemplo, valores muito grandes ou muito pequenos)
- Verifique se o código é robusto o suficiente para lidar com:
  - Condições de concorrência ou paralelismo
  - Problemas de desempenho ou escalabilidade
  - Questões de segurança, como injeção de código ou vazamento de dados

**Segurança**
- Verifique se o código segue as melhores práticas de segurança, incluindo:
  - Uso de criptografia adequada para proteger dados sensíveis
  - Validação e sanitização de entrada de usuário
  - Uso de mecanismos de autenticação e autorização adequados
- Verifique se o código está livre de vulnerabilidades conhecidas, incluindo:
  - Vulnerabilidades de injeção de código
  - Vulnerabilidades de cross-site scripting (XSS)
  - Vulnerabilidades de cross-site request forgery (CSRF)