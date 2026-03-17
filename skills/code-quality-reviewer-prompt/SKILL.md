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
### Tratamento de Exceções
- Verificar se o código lida corretamente com exceções, como erros de sintaxe, erros de tipo, erros de runtime, etc.
- Verificar se o código tem mecanismos de tratamento de exceções adequados, como try-catch blocks, para evitar que o programa crash ou entre em um estado inconsistente.
- Verificar se o código registra corretamente as exceções, para que possam ser analisadas e resolvidas posteriormente.

### Edge Cases
- Verificar se o código lida corretamente com casos de bordo, como entradas inválidas, condições de limite, etc.
- Verificar se o código tem testes adequados para cobrir esses casos de bordo.
- Verificar se o código é robusto o suficiente para lidar com diferentes tipos de entrada e saída, incluindo dados inválidos ou inconsistentes.

### Segurança
- Verificar se o código segue as melhores práticas de segurança, como validação de entrada, sanitização de saída, etc.
- Verificar se o código usa bibliotecas e frameworks seguros e atualizados.
- Verificar se o código tem mecanismos de autenticação e autorização adequados, para evitar acessos não autorizados.