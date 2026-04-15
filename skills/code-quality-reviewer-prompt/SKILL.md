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
  - Tratamento de erros de rede e conexão
  - Tratamento de erros de banco de dados
  - Tratamento de erros de segurança, como injeção de SQL ou cross-site scripting (XSS)
- Verificar se o código é robusto o suficiente para lidar com entradas inválidas ou edge cases, como:
  - Entradas vazias ou nulas
  - Entradas com formato inválido
  - Entradas com valores extremos
- Verificar se o código é seguro contra ataques comuns, como:
  - Injeção de código
  - Cross-site request forgery (CSRF)
  - Ataques de negação de serviço (DoS)
- Verificar se o código segue as melhores práticas de segurança, como:
  - Uso de criptografia adequada
  - Uso de autenticação e autorização adequadas
  - Uso de logs e monitoramento adequados

**Segurança**
- Verificar se o código segue as políticas de segurança da empresa
- Verificar se o código é compatível com as regulamentações de segurança aplicáveis
- Verificar se o código é seguro contra ataques de segurança conhecidos

**Code reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment, incluindo:
- Relatório de segurança
- Relatório de tratamento de exceções e edge cases
- Recomendações para melhorias de segurança e robustez