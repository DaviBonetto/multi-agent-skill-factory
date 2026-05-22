---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (such as Claude Code or Codex). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** - Ensures isolated workspace (creates one or verifies existing)
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:finishing-a-development-branch** - Complete development after all tasks

## ⚠️ Tratamento de Exceções e Edge Cases

### Casos de Erro Comuns
- **Planos mal formatados:** Se o plano não estiver no formato esperado, pare a execução e solicite ajuda.
- **Dependências faltantes:** Se uma dependência necessária para a execução do plano estiver faltando, pare a execução e informe o parceiro humano.
- **Erros de sintaxe:** Se ocorrerem erros de sintaxe durante a execução do plano, pare a execução e solicite ajuda.
- **Verificações falhas:** Se as verificações especificadas no plano falharem repetidamente, pare a execução e solicite ajuda.

### Edge Cases
- **Planos muito grandes:** Se o plano for muito grande, considere dividi-lo em partes menores e mais gerenciáveis.
- **Planos com muitas dependências:** Se o plano tiver muitas dependências, certifique-se de que todas elas estejam disponíveis antes de iniciar a execução.
- **Planos com instruções ambíguas:** Se o plano contiver instruções ambíguas, solicite esclarecimentos antes de prosseguir.

### Tratamento de Exceções
- **Log de erros:** Mantenha um log de erros para registrar qualquer problema que ocorra durante a execução do plano.
- **Notificação de erros:** Notifique o parceiro humano sobre qualquer erro que ocorra durante a execução do plano.
- **Recuperação de erros:** Se possível, tente recuperar de erros e continuar a execução do plano. Se não for possível, pare a execução e solicite ajuda.
