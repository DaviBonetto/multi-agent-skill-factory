---
name: verification-before-completion
description: Use quando está prestes a afirmar que o trabalho está completo, corrigido ou passando, antes de comprometer ou criar PRs - exige a execução de comandos de verificação e confirmação de saída antes de fazer qualquer afirmação de sucesso; evidências antes de afirmações sempre
---

# Verificação Antes da Conclusão

## Visão Geral

Afirmar que o trabalho está completo sem verificação é desonestidade, não eficiência.

**Princípio fundamental:** Evidências antes de afirmações, sempre.

**Violar a letra desta regra é violar o espírito da regra.**

## A Lei de Ferro

```
NENHUMA AFIRMAÇÃO DE CONCLUSÃO SEM EVIDÊNCIAS DE VERIFICAÇÃO ATUALIZADAS
```

Se você não executou o comando de verificação nesta mensagem, não pode afirmar que passa.

## A Função de Porta

```
ANTES de afirmar qualquer status ou expressar satisfação:

1. IDENTIFICAR: Qual comando prova esta afirmação?
2. EXECUTAR: Execute o comando COMPLETO (atualizado, completo)
3. LER: Saída completa, verificar código de saída, contar falhas
4. VERIFICAR: A saída confirma a afirmação?
   - Se NÃO: Afirmar status real com evidências
   - Se SIM: Afirmar com evidências
5. APENAS ENTÃO: Fazer a afirmação

Pular qualquer etapa = mentir, não verificar
```

## Falhas Comuns

| Afirmação | Requer | Não é Suficiente |
|-----------|--------|------------------|
| Testes passam | Saída do comando de teste: 0 falhas | Execução anterior, "deve passar" |
| Linter limpo | Saída do linter: 0 erros | Verificação parcial, extrapolação |
| Build bem-sucedido | Comando de build: saída 0 | Linter passa, logs parecem bons |
| Bug corrigido | Teste do sintoma original: passa | Código alterado, supostamente corrigido |
| Teste de regressão funciona | Ciclo vermelho-verde verificado | Teste passa uma vez |
| Agente concluído | Diferença do VCS mostra alterações | Agente relata "sucesso" |
| Requisitos atendidos | Checklist linha por linha | Testes passam |

## Sinais de Alerta - PARAR

- Usar "deve", "provavelmente", "parece"
- Expressar satisfação antes da verificação ("Ótimo!", "Perfeito!", "Concluído!", etc.)
- Prestes a comprometer/push/PR sem verificação
- Confiar em relatórios de sucesso do agente
- Depender de verificação parcial
- Pensar "apenas desta vez"
- Cansado e querendo terminar o trabalho
- **QUALQUER palavra que implique sucesso sem ter executado a verificação**

## Prevenção de Racionalização

| Desculpa | Realidade |
|-----------|-----------|
| "Deve funcionar agora" | EXECUTAR a verificação |
| "Estou confiante" | Confiança ≠ evidência |
| "Apenas desta vez" | Nenhuma exceção |
| "Linter passou" | Linter ≠ compilador |
| "Agente disse sucesso" | Verificar independentemente |
| "Estou cansado" | Cansaço ≠ desculpa |
| "Verificação parcial é suficiente" | Verificação parcial não prova nada |
| "Palavras diferentes, então a regra não se aplica" | Espírito sobre a letra |

## Padrões Chave

**Testes:**
```
 [Executar comando de teste] [Ver: 34/34 passa] "Todos os testes passam"
 "Deve passar agora" / "Parece correto"
```

**Testes de regressão (TDD Vermelho-Verde):**
```
 Escrever → Executar (passa) → Reverter correção → Executar (DEVE FALHAR) → Restaurar → Executar (passa)
 "Eu escrevi um teste de regressão" (sem verificação vermelho-verde)
```

**Build:**
```
 [Executar build] [Ver: saída 0] "Build passa"
 "Linter passou" (linter não verifica compilação)
```

**Requisitos:**
```
 Re ler plano → Criar checklist → Verificar cada → Relatar lacunas ou conclusão
 "Testes passam, fase concluída"
```

**Delegação de agente:**
```
 Agente relata sucesso → Verificar diferença do VCS → Verificar alterações → Relatar estado real
 Confiar no relatório do agente
```

## Por Que Isso Importa

De 24 memórias de falha:
- seu parceiro humano disse "Não acredito em você" - confiança quebrada
- Funções indefinidas enviadas - iriam falhar
- Requisitos ausentes enviados - recursos incompletos
- Tempo gasto em conclusão falsa → redirecionar → reexecutar
- Viola: "Honestidade é um valor fundamental. Se você mentir, será substituído."

## Quando Aplicar

**SEMPRE antes:**
- QUALQUER variação de afirmações de sucesso/conclusão
- QUALQUER expressão de satisfação
- QUALQUER afirmação positiva sobre o estado do trabalho
- Comprometimento, criação de PR, conclusão de tarefa
- Mover para a próxima tarefa
- Delegar a agentes

**Regra se aplica a:**
- Frases exatas
- Paráfrases e sinônimos
- Implicações de sucesso
- QUALQUER comunicação sugerindo conclusão/correção

## A Linha de Fundo

**Nenhum atalho para verificação.**

Execute o comando. Leia a saída. ENTÃO afirme o resultado.

Isso é não negociável.

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções de Verificação

- **Falha de Verificação:** Se a verificação falhar devido a um problema técnico (como falta de recursos ou erro de sistema), é necessário relatar o problema e não afirmar a conclusão.
- **Exceções de Segurança:** Se a verificação envolver dados sensíveis ou questões de segurança, é crucial garantir que os dados sejam tratados de acordo com as políticas de segurança e que as exceções sejam lidadas de maneira a minimizar riscos.

### Edge Cases

- **Comandos de Verificação Complexos:** Em casos onde os comandos de verificação são complexos ou dependem de múltiplos fatores, é importante garantir que todos os aspectos sejam considerados e que a verificação seja feita de forma abrangente.
- **Dependências Externas:** Se a verificação depende de serviços ou sistemas externos, é crucial ter um plano para lidar com falhas ou indisponibilidades desses serviços, garantindo que a verificação não seja comprometida.
- **Limitações de Recursos:** Em situações onde os recursos (como tempo, memória, etc.) são limitados, é necessário priorizar a verificação e garantir que os aspectos críticos sejam abordados, mesmo que não seja possível executar a verificação completa.

### Documentação de Exceções e Edge Cases

- **Registro de Incidentes:** Manter um registro de incidentes e exceções durante a verificação, incluindo detalhes do que ocorreu, como foi resolvido e quais medidas preventivas foram tomadas.
- **Revisão e Ajuste:** Regularmente revisar e ajustar os processos de verificação e tratamento de exceções com base nas lições aprendidas e nos incidentes registrados, garantindo que a abordagem de verificação permaneça robusta e eficaz.
