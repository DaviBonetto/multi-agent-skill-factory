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
- **superpowers:using-git-worktrees** - REQUIRED: Set up isolated workspace before starting
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:finishing-a-development-branch** - Complete development after all tasks

## ⚠️ Tratamento de Exceções e Edge Cases

### Casos de Exceção
- **Plano inválido**: Se o plano for inválido ou não puder ser carregado, pare a execução e solicite ajuda.
- **Tarefas conflitantes**: Se duas ou mais tarefas no plano forem conflitantes, pare a execução e solicite ajuda.
- **Dependências ausentes**: Se dependências necessárias para a execução do plano estiverem ausentes, pare a execução e solicite ajuda.
- **Erros de verificação**: Se as verificações especificadas no plano falharem repetidamente, pare a execução e solicite ajuda.

### Edge Cases
- **Planos muito grandes**: Se o plano for muito grande, considere dividi-lo em planos menores e mais gerenciáveis.
- **Tarefas muito complexas**: Se as tarefas no plano forem muito complexas, considere dividi-las em tarefas menores e mais gerenciáveis.
- **Conflitos de versão**: Se houver conflitos de versão entre as dependências necessárias para a execução do plano, pare a execução e solicite ajuda.

### Tratamento de Erros
- **Logs de erro**: Mantenha logs de erro detalhados para ajudar a identificar e resolver problemas.
- **Notificação de erros**: Notifique o parceiro humano sobre erros e solicite ajuda quando necessário.
- **Recuperação de erros**: Tente recuperar de erros sempre que possível, mas não force a execução se houver um bloqueio.