---
name: executing-plans
description: Use quando você tem um plano de implementação escrito para executar em uma sessão separada com pontos de verificação de revisão
---

# Executando Planos

## Visão Geral

Carregue o plano, revise criticamente, execute todas as tarefas e informe quando concluído.

**Anuncie no início:** "Estou usando a habilidade de executar planos para implementar este plano."

**Nota:** Informe ao seu parceiro humano que Superpowers funciona muito melhor com acesso a subagentes. A qualidade do seu trabalho será significativamente melhor se executado em uma plataforma com suporte a subagentes (Claude Code, Codex CLI, Codex App, Copilot CLI e Gemini CLI são qualificados; consulte as referências de ferramentas por plataforma em `../using-superpowers/references/`). Se os subagentes estiverem disponíveis, use superpowers:subagent-driven-development em vez desta habilidade.

## O Processo

### Etapa 1: Carregar e Revisar Plano
1. Leia o arquivo do plano
2. Revise criticamente - identifique quaisquer dúvidas ou preocupações sobre o plano
3. Se houver preocupações: Levante-as com seu parceiro humano antes de começar
4. Se não houver preocupações: Crie tarefas para os itens do plano e prossiga

### Etapa 2: Executar Tarefas

Para cada tarefa:
1. Marque como em andamento
2. Siga cada etapa exatamente (o plano tem etapas de tamanho reduzido)
3. Execute verificações como especificado
4. Marque como concluída

### Etapa 3: Concluir Desenvolvimento

Depois que todas as tarefas forem concluídas e verificadas:
- Anuncie: "Estou usando a habilidade de concluir um branch de desenvolvimento para concluir este trabalho."
- **HABILIDADE SUB-REQUERIDA:** Use superpowers:finishing-a-development-branch
- Siga essa habilidade para verificar testes, apresentar opções, executar escolha

## Quando Parar e Pedir Ajuda

**PARE de executar imediatamente quando:**
- Encontrar um bloqueador (dependência ausente, teste falha, instrução não clara)
- O plano tem lacunas críticas que impedem o início
- Você não entender uma instrução
- Verificação falha repetidamente

**Peça esclarecimento em vez de adivinhar.**

## Quando Revisitar Etapas Anteriores

**Retorne à Revisão (Etapa 1) quando:**
- Parceiro atualiza o plano com base em seu feedback
- Abordagem fundamental precisa ser reavaliada

**Não force a passagem de bloqueadores** - pare e peça.

## Lembre-se
- Revise o plano criticamente primeiro
- Siga as etapas do plano exatamente
- Não pule verificações
- Faça referência a habilidades quando o plano disser para
- Pare quando bloqueado, não adivinhe
- Nunca inicie a implementação no branch main/master sem consentimento explícito do usuário

## Integração

**Habilidades de fluxo de trabalho necessárias:**
- **superpowers:using-git-worktrees** - Garante um espaço de trabalho isolado (cria um ou verifica se existe)
- **superpowers:writing-plans** - Cria o plano que esta habilidade executa
- **superpowers:finishing-a-development-branch** - Conclui o desenvolvimento após todas as tarefas

⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erros de Leitura do Plano:** Se houver um erro ao ler o arquivo do plano, anuncie o erro e peça ajuda.
- **Erros de Execução de Tarefas:** Se houver um erro ao executar uma tarefa, anuncie o erro e peça ajuda.
- **Erros de Verificação:** Se houver um erro ao executar uma verificação, anuncie o erro e peça ajuda.

### Edge Cases
- **Plano Vazio:** Se o plano estiver vazio, anuncie que o plano está vazio e peça ajuda.
- **Tarefa Inválida:** Se uma tarefa for inválida, anuncie que a tarefa é inválida e peça ajuda.
- **Dependência Ausente:** Se uma dependência for ausente, anuncie que a dependência está ausente e peça ajuda.

### Segurança
- **Validação de Entradas:** Valide todas as entradas para garantir que sejam seguras e válidas.
- **Prevenção de Injeção de Comandos:** Previna a injeção de comandos ao executar tarefas e verificações.
- **Uso de Subagentes:** Se os subagentes estiverem disponíveis, use superpowers:subagent-driven-development em vez desta habilidade para garantir a segurança e a qualidade do trabalho.