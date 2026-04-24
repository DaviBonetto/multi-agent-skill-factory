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

⚠️ Tratamento de Exceções e Edge Cases
- Verifique se o código lida corretamente com entradas inválidas ou inexperadas.
- Verifique se o código tem tratamento de erros adequado para situações como:
  - Erros de rede
  - Erros de banco de dados
  - Erros de permissão
- Verifique se o código tem mecanismos de segurança para prevenir ataques comuns, como:
  - Injeção de SQL
  - Cross-Site Scripting (XSS)
  - Cross-Site Request Forgery (CSRF)
- Verifique se o código segue as melhores práticas de segurança, como:
  - Uso de criptografia adequada
  - Uso de autenticação e autorização adequadas
  - Uso de validação de entrada de dados
- Verifique se o código tem testes unitários e de integração adequados para garantir a robustez e a segurança do código.