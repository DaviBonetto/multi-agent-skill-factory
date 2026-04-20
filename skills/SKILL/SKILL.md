---
name: executing-plans
description: Use quando você tem um plano de implementação escrito para executar em uma sessão separada com pontos de verificação de revisão
---

# Executando Planos

## Visão Geral

Carregue o plano, revise criticamente, execute todas as tarefas e informe quando concluído.

**Anuncie no início:** "Estou usando a habilidade de executar planos para implementar este plano."

**Nota:** Informe ao seu parceiro humano que Superpowers funciona muito melhor com acesso a subagentes. A qualidade do seu trabalho será significativamente maior se executado em uma plataforma com suporte a subagentes (como Claude Code ou Codex). Se subagentes estiverem disponíveis, use superpowers:subagent-driven-development em vez desta habilidade.

## O Processo

### Etapa 1: Carregar e Revisar Plano
1. Leia o arquivo do plano
2. Revise criticamente - identifique quaisquer dúvidas ou preocupações sobre o plano
3. Se houver preocupações: Levante-as com seu parceiro humano antes de começar
4. Se não houver preocupações: Crie TodoWrite e prossiga

### Etapa 2: Executar Tarefas

Para cada tarefa:
1. Marque como em_progresso
2. Siga cada etapa exatamente (plano tem etapas pequenas)
3. Execute verificações como especificado
4. Marque como concluída

### Etapa 3: Concluir Desenvolvimento

Depois que todas as tarefas forem concluídas e verificadas:
- Anuncie: "Estou usando a habilidade de concluir um ramo de desenvolvimento para concluir este trabalho."
- **HABILIDADE SUB-REQUERIDA:** Use superpowers:finishing-a-development-branch
- Siga essa habilidade para verificar testes, apresentar opções, executar escolha

## Quando Parar e Pedir Ajuda

**PARE de executar imediatamente quando:**
- Encontrar um bloqueador (dependência faltando, teste falha, instrução não clara)
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
- Faça referência a habilidades quando o plano disser para fazer
- Pare quando bloqueado, não adivinhe
- Nunca inicie a implementação no ramo principal sem consentimento explícito do usuário

## Integração

**Habilidades de fluxo de trabalho necessárias:**
- **superpowers:using-git-worktrees** - OBRIGATÓRIO: Configure o espaço de trabalho isolado antes de começar
- **superpowers:writing-plans** - Cria o plano que esta habilidade executa
- **superpowers:finishing-a-development-branch** - Conclua o desenvolvimento após todas as tarefas

⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erro de Carregamento do Plano:** Se o arquivo do plano não for encontrado ou não puder ser carregado, informe o erro e peça ajuda.
- **Erro de Execução de Tarefas:** Se uma tarefa não puder ser executada devido a um erro, informe o erro e peça ajuda.
- **Erro de Verificação:** Se uma verificação falhar, informe o erro e peça ajuda.

### Edge Cases
- **Plano Vazio:** Se o plano estiver vazio, informe que o plano está vazio e peça ajuda.
- **Tarefa sem Etapas:** Se uma tarefa não tiver etapas, informe que a tarefa não tem etapas e peça ajuda.
- **Verificação sem Especificação:** Se uma verificação não tiver especificação, informe que a verificação não tem especificação e peça ajuda.

### Segurança
- **Validação de Entradas:** Valide todas as entradas para garantir que sejam válidas e seguras.
- **Controle de Acesso:** Garanta que o acesso ao plano e às tarefas seja controlado e seguro.
- **Registro de Atividades:** Registre todas as atividades para garantir a auditoria e a segurança.
