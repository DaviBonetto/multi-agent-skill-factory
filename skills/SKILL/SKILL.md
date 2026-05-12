---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
---

# Verification Before Completion

## Overview

Claiming work is complete without verification is dishonesty, not efficiency.

**Core principle:** Evidence before claims, always.

**Violating the letter of this rule is violating the spirit of this rule.**

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes.

## The Gate Function

```
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying
```

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test command output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check, extrapolation |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Test original symptom: passes | Code changed, assumed fixed |
| Regression test works | Red-green cycle verified | Test passes once |
| Agent completed | VCS diff shows changes | Agent reports "success" |
| Requirements met | Line-by-line checklist | Tests passing |

## Red Flags - STOP

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Perfect!", "Done!", etc.)
- About to commit/push/PR without verification
- Trusting agent success reports
- Relying on partial verification
- Thinking "just this once"
- Tired and wanting work over
- **ANY wording implying success without having run verification**

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence ≠ evidence |
| "Just this once" | No exceptions |
| "Linter passed" | Linter ≠ compiler |
| "Agent said success" | Verify independently |
| "I'm tired" | Exhaustion ≠ excuse |
| "Partial check is enough" | Partial proves nothing |
| "Different words so rule doesn't apply" | Spirit over letter |

## Key Patterns

**Tests:**
```
 [Run test command] [See: 34/34 pass] "All tests pass"
 "Should pass now" / "Looks correct"
```

**Regression tests (TDD Red-Green):**
```
 Write → Run (pass) → Revert fix → Run (MUST FAIL) → Restore → Run (pass)
 "I've written a regression test" (without red-green verification)
```

**Build:**
```
 [Run build] [See: exit 0] "Build passes"
 "Linter passed" (linter doesn't check compilation)
```

**Requirements:**
```
 Re-read plan → Create checklist → Verify each → Report gaps or completion
 "Tests pass, phase complete"
```

**Agent delegation:**
```
 Agent reports success → Check VCS diff → Verify changes → Report actual state
 Trust agent report
```

## Why This Matters

From 24 failure memories:
- your human partner said "I don't believe you" - trust broken
- Undefined functions shipped - would crash
- Missing requirements shipped - incomplete features
- Time wasted on false completion → redirect → rework
- Violates: "Honesty is a core value. If you lie, you'll be replaced."

## When To Apply

**ALWAYS before:**
- ANY variation of success/completion claims
- ANY expression of satisfaction
- ANY positive statement about work state
- Committing, PR creation, task completion
- Moving to next task
- Delegating to agents

**Rule applies to:**
- Exact phrases
- Paraphrases and synonyms
- Implications of success
- ANY communication suggesting completion/correctness

## The Bottom Line

**No shortcuts for verification.**

Run the command. Read the output. THEN claim the result.

This is non-negotiable.

## ⚠️ Tratamento de Exceções e Edge Cases

Além dos casos comuns e padrões apresentados, é importante considerar os seguintes cenários de exceção e edge cases:

- **Erros de sintaxe ou execução**: Se o comando de verificação falhar devido a erros de sintaxe ou execução, não se deve afirmar que o trabalho está completo. Em vez disso, os erros devem ser corrigidos e o comando reexecutado.
- **Saídas inconsistentes**: Se a saída do comando de verificação for inconsistente ou ambígua, não se deve fazer afirmações sobre o estado do trabalho. Em vez disso, a saída deve ser analisada cuidadosamente e, se necessário, o comando deve ser reexecutado ou modificado para obter resultados claros.
- **Comandos de verificação longos ou complexos**: Se o comando de verificação for longo ou complexo, é importante garantir que todos os passos sejam executados corretamente e que a saída seja analisada cuidadosamente. Não se deve simplificar ou omitir passos para acelerar o processo.
- **Dependências ou requisitos não atendidos**: Se o comando de verificação depender de requisitos ou dependências específicas, é importante garantir que esses requisitos sejam atendidos antes de executar o comando. Não se deve afirmar que o trabalho está completo se os requisitos não forem atendidos.
- **Comandos de verificação que falham devido a limitações do sistema**: Se o comando de verificação falhar devido a limitações do sistema, como falta de recursos ou problemas de conectividade, não se deve afirmar que o trabalho está completo. Em vez disso, os problemas do sistema devem ser resolvidos e o comando reexecutado.

Ao considerar esses cenários de exceção e edge cases, é possível garantir que o processo de verificação seja robusto e confiável, e que as afirmações sobre o estado do trabalho sejam precisas e honestas.