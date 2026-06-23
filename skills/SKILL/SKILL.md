---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (Claude Code, Codex CLI, Codex App, Copilot CLI, and Gemini CLI all qualify; see the per-platform tool refs in `../using-superpowers/references/`). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create todos for the plan items and proceed

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

### Erros de Leitura do Plano
- **Plano não encontrado:** Verifique se o arquivo do plano está no local correto e se o caminho está correto. Se o problema persistir, solicite ajuda ao parceiro humano.
- **Formatação do plano inválida:** Verifique se o plano está no formato esperado. Se o formato estiver incorreto, solicite ao parceiro humano que atualize o plano.

### Erros de Execução de Tarefas
- **Tarefa com dependências não atendidas:** Verifique as dependências necessárias para a tarefa e certifique-se de que elas estão disponíveis. Se as dependências não estiverem disponíveis, solicite ajuda ao parceiro humano.
- **Tarefa com instruções unclear:** Solicite clarificação ao parceiro humano se as instruções da tarefa não estiverem claras.

### Erros de Verificação
- **Verificação falha:** Verifique se a verificação está configurada corretamente e se os critérios de verificação estão sendo atendidos. Se a verificação continuar falhando, solicite ajuda ao parceiro humano.

### Outros Casos
- **Parceiro humano não disponível:** Se o parceiro humano não estiver disponível para esclarecer dúvidas ou fornecer ajuda, aguarde até que ele esteja disponível ou procure ajuda de outro recurso.
- **Plano com gaps críticos:** Se o plano tiver gaps críticos que impedem o progresso, solicite ao parceiro humano que atualize o plano antes de prosseguir.