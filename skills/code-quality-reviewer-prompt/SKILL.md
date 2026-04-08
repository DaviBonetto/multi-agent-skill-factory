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
- Verifique se o código lida corretamente com exceções, como erros de sintaxe, erros de tipo, erros de rede, etc.
- Certifique-se de que as exceções sejam tratadas de forma apropriada, com mensagens de erro claras e úteis.
- Verifique se o código segue as melhores práticas para tratamento de exceções, como não capturar exceções gerais e sim capturar exceções específicas.

### Edge Cases
- Verifique se o código lida corretamente com casos de bordo, como:
  - Entradas inválidas ou malformadas
  - Valores limite (por exemplo, zero, negativo, muito grande)
  - Casos de erro ou exceção
- Certifique-se de que o código seja robusto o suficiente para lidar com esses casos de bordo sem falhar ou produzir resultados incorretos.
- Verifique se o código segue as melhores práticas para lidar com casos de bordo, como testar explicitamente esses casos e ter um plano de contingência para lidar com erros inesperados.

### Segurança
- Verifique se o código segue as melhores práticas de segurança, como:
  - Validar e sanitizar entradas de usuário
  - Proteger contra injeção de código malicioso
  - Usar criptografia adequada para proteger dados sensíveis
- Certifique-se de que o código seja seguro o suficiente para evitar vulnerabilidades de segurança comuns, como SQL injection, cross-site scripting (XSS), etc.
- Verifique se o código segue as políticas de segurança da empresa e as regulamentações aplicáveis.