---
name: Análise de Dados com Pandas
description: Ensina como realizar análises de dados com a biblioteca Pandas em Python
---

## Objetivo
O objetivo deste guia é fornecer uma introdução prática à análise de dados utilizando a biblioteca Pandas em Python. Ao final, você será capaz de realizar análises básicas de dados, incluindo manipulação, filtragem e visualização de dados.

## Pré-requisitos
Para seguir este guia, você deve ter:
- Conhecimento básico de Python
- Python instalado em seu computador (recomendado Python 3.x)
- Biblioteca Pandas instalada (`pip install pandas`)
- Um editor de texto ou IDE (como PyCharm, VSCode, etc.)

## Passo a Passo Técnico / Exemplos de Código
### Instalação da Biblioteca Pandas
Se você ainda não instalou a biblioteca Pandas, pode fazê-lo executando o seguinte comando no terminal:
```bash
pip install pandas
```
Caso você encontre algum problema durante a instalação, verifique se o Python está corretamente instalado e se o `pip` está atualizado.

### Importando a Biblioteca Pandas
Para começar a usar a biblioteca Pandas, você precisa importá-la em seu script Python:
```python
import pandas as pd
```
Certifique-se de que a biblioteca foi importada corretamente, pois erros de importação podem afetar o restante do código.

### Criando um DataFrame
Um DataFrame é uma estrutura de dados bidimensional com colunas de tipos potencialmente diferentes. Você pode criar um DataFrame a partir de um dicionário:
```python
dados = {'Nome': ['João', 'Maria', 'Pedro'],
         'Idade': [25, 31, 42]}
df = pd.DataFrame(dados)
print(df)
```
Se o dicionário estiver vazio ou não for um dicionário, o Pandas lançará um erro. Certifique-se de que os dados estão no formato correto antes de criar o DataFrame.

### Manipulando Dados
Você pode manipular os dados do DataFrame de várias maneiras, como filtrar linhas ou selecionar colunas específicas:
```python
# Filtrar linhas onde a idade é maior que 30
df_filtrado = df[df['Idade'] > 30]
print(df_filtrado)

# Selecionar apenas a coluna 'Nome'
nomes = df['Nome']
print(nomes)
```
Se a coluna especificada não existir no DataFrame, o Pandas lançará um erro. Sempre verifique a existência da coluna antes de tentar acessá-la.

## Validação
Para validar o conhecimento adquirido, tente realizar as seguintes tarefas:
- Criar um DataFrame com informações sobre filmes (título, gênero, ano de lançamento)
- Filtrar os filmes lançados após 2010
- Calcular a média de idade dos atores em um conjunto de dados que inclui o nome do ator e sua idade

Ao completar essas tarefas, você terá demonstrado uma compreensão básica da análise de dados com Pandas e estará pronto para avançar para conceitos mais complexos.

## ⚠️ Tratamento de Exceções e Edge Cases
Ao trabalhar com o Pandas, é importante considerar os casos de bordo e exceções que podem ocorrer. Aqui estão algumas dicas para lidar com esses casos:
- **Dados faltantes**: O Pandas pode lidar com dados faltantes, mas é importante identificar e tratar esses dados corretamente. Use o método `isnull()` para detectar dados faltantes e o método `dropna()` para remover linhas com dados faltantes.
- **Tipos de dados inconsistentes**: Certifique-se de que os dados estejam no tipo correto antes de realizar operações. Use o método `dtypes` para verificar os tipos de dados das colunas.
- **Erros de importação**: Se ocorrer um erro durante a importação da biblioteca Pandas, verifique se o Python está corretamente instalado e se o `pip` está atualizado.
- **Erros de criação de DataFrame**: Se ocorrer um erro durante a criação de um DataFrame, verifique se os dados estão no formato correto e se o dicionário não está vazio.

Exemplo de como tratar dados faltantes:
```python
# Criar um DataFrame com dados faltantes
dados = {'Nome': ['João', 'Maria', None],
         'Idade': [25, 31, 42]}
df = pd.DataFrame(dados)

# Detectar dados faltantes
print(df.isnull())

# Remover linhas com dados faltantes
df_limpo = df.dropna()
print(df_limpo)
```
Lembre-se de que o tratamento de exceções e casos de bordo é fundamental para garantir a robustez e a confiabilidade do seu código. Sempre considere os possíveis erros e exceções que podem ocorrer e trate-os corretamente.