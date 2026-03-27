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
- Verificar se o código lida corretamente com exceções e erros, incluindo:
  - Tratamento de erros de entrada e saída
  - Manipulação de exceções para evitar crashes inesperados
  - Uso de mecanismos de logging para registrar eventos importantes
- Verificar se o código é robusto o suficiente para lidar com:
  - Entradas inválidas ou malformadas
  - Condições de bordo, como valores limite ou extremos
  - Casos de uso não previstos ou imprevisíveis
- Verificar se o código segue as melhores práticas de segurança, incluindo:
  - Validaçaõ de entrada de usuário
  - Proteção contra injeção de código
  - Uso de criptografia para proteger dados sensíveis
- Verificar se o código é escalável e pode lidar com:
  - Grandes volumes de dados
  - Alta carga de trabalho
  - Condições de rede adversas

**Segurança**
- Verificar se o código segue as políticas de segurança da empresa
- Verificar se o código usa bibliotecas e dependências seguras e atualizadas
- Verificar se o código tem mecanismos de autenticação e autorização adequados
- Verificar se o código protege contra ataques comuns, como SQL Injection e Cross-Site Scripting (XSS)