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
  - Manipulação de exceções de forma apropriada
  - Uso de mecanismos de retry e timeout quando necessário
- Verificar se o código é robusto o suficiente para lidar com:
  - Entradas inválidas ou malformadas
  - Condições de bordo, como valores nulos ou vazios
  - Casos de uso não comuns ou inesperados
- Verificar se o código segue as melhores práticas de segurança, incluindo:
  - Validação de entrada de usuário
  - Proteção contra injeção de código
  - Uso de criptografia quando necessário
- Verificar se o código é escalável e performático, incluindo:
  - Uso eficiente de recursos
  - Minimização de operações de E/S
  - Uso de técnicas de caching e memoização quando necessário

**Exemplos de Casos de Uso**
- Implementação de um novo recurso que requer a integração com um serviço externo
- Refatoração de um código legado para melhorar a manutenibilidade e a performance
- Desenvolvimento de um novo módulo que requer a interação com outros módulos existentes

**Melhores Práticas**
- Seguir as diretrizes de codificação estabelecidas pela equipe
- Manter a documentação atualizada e clara
- Realizar testes unitários e de integração para garantir a qualidade do código