---
name: Visualização de Dados com Tableau e Power BI
description: Esta skill ensina como criar visualizações de dados interativas utilizando ferramentas como Tableau e Power BI
---

## Objetivo
O objetivo desta skill é capacitar os alunos a criar visualizações de dados interativas utilizando ferramentas como Tableau e Power BI, incluindo a conexão a fontes de dados e a criação de relatórios. Com isso, os alunos poderão tomar decisões informadas com base em dados precisos e atualizados.

## Pré-requisitos
Para iniciar esta skill, é necessário ter conhecimento básico em:
* Conceitos de dados e análise de dados
* Ferramentas de visualização de dados (não é necessário conhecimento prévio em Tableau ou Power BI)
* Conhecimento básico em informática e habilidades para aprender novas ferramentas

## Passo a Passo Técnico / Exemplos de Código
### Conexão a Fontes de Dados
1. **Tableau**: Para conectar o Tableau a uma fonte de dados, siga os passos abaixo:
   * Abra o Tableau e clique em "Conectar a Dados"
   * Selecione a fonte de dados desejada (por exemplo, Excel, SQL Server, etc.)
   * Insira as credenciais de acesso e configure as opções de conexão
2. **Power BI**: Para conectar o Power BI a uma fonte de dados, siga os passos abaixo:
   * Abra o Power BI e clique em "Obter Dados"
   * Selecione a fonte de dados desejada (por exemplo, Excel, SQL Server, etc.)
   * Insira as credenciais de acesso e configure as opções de conexão

### Criação de Relatórios
1. **Tableau**: Para criar um relatório no Tableau, siga os passos abaixo:
   * Crie um novo projeto e selecione a fonte de dados conectada
   * Arraste e solte os campos desejados para o relatório
   * Configure as opções de visualização e formatação
2. **Power BI**: Para criar um relatório no Power BI, siga os passos abaixo:
   * Crie um novo projeto e selecione a fonte de dados conectada
   * Arraste e solte os campos desejados para o relatório
   * Configure as opções de visualização e formatação

Exemplo de código em DAX (Power BI):
```dax
Medida = SUM('Tabela'[Valor])
```
Este código cria uma medida que soma os valores da coluna "Valor" da tabela "Tabela".

## Validação
Para validar os conhecimentos adquiridos, é necessário criar um relatório que inclua:
* Conexão a uma fonte de dados
* Criação de visualizações interativas (gráficos, tabelas, etc.)
* Uso de medidas e dimensões para analisar os dados
* Formatação e personalização do relatório

## ⚠️ Tratamento de Exceções e Edge Cases
Durante a criação de relatórios, é importante considerar os seguintes casos:
* **Fontes de dados indisponíveis**: Verifique se a fonte de dados está disponível e se as credenciais de acesso estão corretas.
* **Dados inconsistentes**: Verifique se os dados estão consistentes e se não há erros de digitação ou formatação.
* **Limitações de desempenho**: Verifique se o relatório está otimizado para evitar problemas de desempenho.
* **Segurança**: Verifique se as credenciais de acesso estão seguras e se os dados estão protegidos contra acessos não autorizados.
* **Erros de sintaxe**: Verifique se o código em DAX ou outras linguagens está correto e não contém erros de sintaxe.
* **Problemas de compatibilidade**: Verifique se o relatório está compatível com diferentes versões do Tableau ou Power BI.

Com a conclusão desta skill, os alunos estarão capacitados a criar visualizações de dados interativas utilizando ferramentas como Tableau e Power BI, e poderão aplicar esses conhecimentos em projetos reais, considerando os casos de exceção e edge cases.