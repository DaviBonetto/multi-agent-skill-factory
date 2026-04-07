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
### Exceções
- Verificar se o código lida corretamente com exceções, como erros de sintaxe, erros de tipo, ou exceções de runtime.
- Verificar se o código tem tratamento de exceções personalizadas para situações específicas.
- Verificar se o código segue as melhores práticas para lidar com exceções, como não ignorar exceções silenciosamente.

### Edge Cases
- Verificar se o código lida corretamente com casos de bordo, como:
  - Valores nulos ou vazios.
  - Valores extremos (muito grandes ou muito pequenos).
  - Valores inválidos ou inconsistentes.
- Verificar se o código tem testes adequados para cobrir esses casos de bordo.
- Verificar se o código é robusto o suficiente para lidar com esses casos de bordo sem falhar ou produzir resultados inconsistentes.

### Segurança
- Verificar se o código segue as melhores práticas de segurança, como:
  - Validar entrada de usuário.
  - Proteger contra injeção de SQL ou cross-site scripting (XSS).
  - Usar criptografia adequada para proteger dados sensíveis.
- Verificar se o código tem vulnerabilidades conhecidas ou desatualizações de bibliotecas ou frameworks.
- Verificar se o código é compatível com as políticas de segurança da organização.