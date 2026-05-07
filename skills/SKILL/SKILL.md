---
name: executing-plans
description: Use quando você tem um plano de implementação escrito para executar em uma sessão separada com pontos de verificação de revisão
---

# Executing Plans

## Overview

Carregue o plano, revise criticamente, execute todas as tarefas e informe quando concluído.

**Anuncie no início:** "Estou usando a habilidade de execução de planos para implementar este plano."

**Nota:** Informe seu parceiro humano de que o Superpowers funciona muito melhor com acesso a subagentes. A qualidade do seu trabalho será significativamente maior se executado em uma plataforma com suporte a subagentes (como Claude Code ou Codex). Se os subagentes estiverem disponíveis, use superpowers:subagent-driven-development em vez desta habilidade.

## O Processo

### Step 1: Carregar e Revisar Plano
1. Leia o arquivo do plano
2. Revise criticamente - identifique quaisquer dúvidas ou preocupações sobre o plano
3. Se houver preocupações: Levante-as com seu parceiro humano antes de começar
4. Se não houver preocupações: Crie TodoWrite e prossiga

### Step 2: Executar Tarefas

Para cada tarefa:
1. Marque como em_progress
2. Siga cada etapa exatamente (plano tem etapas pequenas)
3. Execute verificações como especificado
4. Marque como concluída

### Step 3: Concluir Desenvolvimento

Depois que todas as tarefas forem concluídas e verificadas:
- Anuncie: "Estou usando a habilidade de finalizar um ramo de desenvolvimento para concluir este trabalho."
- **HABILIDADE SUB-REQUERIDA:** Use superpowers:finishing-a-development-branch
- Siga essa habilidade para verificar testes, apresentar opções, executar escolha

## Quando Parar e Pedir Ajuda

**PARE de executar imediatamente quando:**
- Encontrar um bloqueador (dependência ausente, teste falha, instrução não clara)
- Plano tem lacunas críticas que impedem o início
- Você não entender uma instrução
- Verificação falha repetidamente

**Peça esclarecimento em vez de adivinhar.**

## Quando Revisitar Etapas Anteriores

**Retorne à Revisão (Etapa 1) quando:**
- Parceiro atualiza o plano com base em seu feedback
- Abordagem fundamental precisa ser re pensada

**Não force através de bloqueadores** - pare e peça.

## Lembre-se
- Revise o plano criticamente primeiro
- Siga as etapas do plano exatamente
- Não pule verificações
- Faça referência a habilidades quando o plano disser para
- Pare quando bloqueado, não adivinhe
- Nunca inicie a implementação no ramo principal sem consentimento explícito do usuário

## Integração

**Habilidades de fluxo de trabalho necessárias:**
- **superpowers:using-git-worktrees** - Garante um espaço de trabalho isolado (cria um ou verifica se existe)
- **superpowers:writing-plans** - Cria o plano que esta habilidade executa
- **superpowers:finishing-a-development-branch** - Conclui o desenvolvimento após todas as tarefas

⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erros de sintaxe no plano:** Se o plano contiver erros de sintaxe, a execução deve ser interrompida e um erro deve ser relatado ao usuário.
- **Falhas de verificação:** Se uma verificação falhar, a tarefa deve ser marcada como não concluída e um erro deve ser relatado ao usuário.
- **Dependências ausentes:** Se uma dependência necessária estiver ausente, a execução deve ser interrompida e um erro deve ser relatado ao usuário.

### Edge Cases
- **Planos vazios:** Se o plano estiver vazio, a execução deve ser interrompida e um erro deve ser relatado ao usuário.
- **Tarefas duplicadas:** Se houver tarefas duplicadas no plano, a execução deve ignorar as tarefas duplicadas e continuar com as tarefas únicas.
- **Instruções não claras:** Se uma instrução no plano não for clara, a execução deve ser interrompida e um erro deve ser relatado ao usuário.
