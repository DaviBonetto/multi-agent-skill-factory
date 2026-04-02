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
  - Tratamento de erros de sintaxe e semântica
  - Manipulação de dados inválidos ou inconsistentes
  - Lidar com condições de bordo, como valores nulos ou vazios
  - Implementação de mecanismos de retry ou fallback para operações que podem falhar
- Verificar se o código é robusto o suficiente para lidar com diferentes cenários de entrada e saída, incluindo:
  - Dados malformados ou corrompidos
  - Condições de concorrência ou paralelismo
  - Limitações de recursos, como memória ou processamento
- Verificar se o código segue as melhores práticas de segurança, incluindo:
  - Validar e sanitizar entradas de usuário
  - Proteger contra injeção de código ou ataques de cross-site scripting (XSS)
  - Implementar autenticação e autorização adequadas
  - Criptografar dados sensíveis em trânsito e em repouso

**Exemplos de Edge Cases:**
- Lidar com datas e horários em diferentes fusos horários
- Manipular números decimais com precisão variável
- Tratar de strings com caracteres especiais ou não ASCII
- Lidar com arquivos ou streams de dados corrompidos ou truncados

**Recomendações:**
- Utilizar bibliotecas e frameworks de teste para garantir a cobertura de código e a robustez
- Implementar logging e monitoramento para detectar e diagnosticar problemas
- Realizar revisões de código regulares para garantir a qualidade e a segurança do código
- Manter a documentação atualizada e acessível para todos os membros da equipe