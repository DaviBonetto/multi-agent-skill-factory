---
name: Análise de Dados com Python e Pandas
description: Esta skill aborda a análise de dados utilizando Python e a biblioteca Pandas, ensinando como manipular, visualizar e extrair insights de conjuntos de dados.
---

## Objetivo
O objetivo desta skill é capacitar os participantes a realizar análise de dados utilizando Python e a biblioteca Pandas, permitindo que eles possam manipular, visualizar e extrair insights de conjuntos de dados de forma eficaz.

## Pré-requisitos
Para participar desta skill, é necessário ter conhecimento básico em programação Python e experiência com manipulação de dados. Além disso, é recomendado ter instalado o Python e a biblioteca Pandas em seu ambiente de desenvolvimento.

## Passo a Passo Técnico / Exemplos de Código
### Instalação da Biblioteca Pandas
Para começar a utilizar a biblioteca Pandas, é necessário instalá-la em seu ambiente de desenvolvimento. Isso pode ser feito utilizando o pip:
```bash
pip install pandas
```
### Importação da Biblioteca Pandas
Após a instalação, é possível importar a biblioteca Pandas em seu script Python:
```python
import pandas as pd
```
### Carregamento de Dados
A biblioteca Pandas permite carregar dados de diversas fontes, incluindo arquivos CSV e Excel. Por exemplo, para carregar um arquivo CSV:
```python
df = pd.read_csv('dados.csv')
```
### Manipulação de Dados
A biblioteca Pandas fornece diversas funções para manipular dados, incluindo filtragem, agrupamento e ordenação. Por exemplo, para filtrar os dados com base em uma condição:
```python
df_filtrado = df[df['idade'] > 18]
```
### Visualização de Dados
A biblioteca Pandas pode ser utilizada em conjunto com bibliotecas de visualização, como Matplotlib e Seaborn, para criar gráficos e visualizações. Por exemplo, para criar um gráfico de barras:
```python
import matplotlib.pyplot as plt
df['categoria'].value_counts().plot(kind='bar')
plt.show()
```
## Validação
Para validar os conhecimentos adquiridos, é recomendado realizar exercícios práticos com conjuntos de dados reais, aplicando as técnicas de manipulação, visualização e extração de insights aprendidas durante a skill. Além disso, é importante realizar a documentação e apresentação dos resultados, utilizando ferramentas como Jupyter Notebook e Markdown.

## ⚠️ Tratamento de Exceções e Edge Cases
Durante a análise de dados, é importante considerar os seguintes casos:
* **Arquivos CSV vazios ou corrompidos**: Verificar se o arquivo CSV está vazio ou corrompido antes de tentar carregá-lo.
```python
try:
    df = pd.read_csv('dados.csv')
except pd.errors.EmptyDataError:
    print("Arquivo CSV vazio")
except pd.errors.ParserError:
    print("Arquivo CSV corrompido")
```
* **Colunas com dados faltantes**: Verificar se as colunas contêm dados faltantes e tratar esses dados de acordo com a necessidade.
```python
df.isnull().sum()
df.dropna(inplace=True)
```
* **Tipos de dados inconsistentes**: Verificar se os tipos de dados nas colunas são consistentes e converter os tipos de dados se necessário.
```python
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
```
* **Dados fora do intervalo esperado**: Verificar se os dados estão dentro do intervalo esperado e tratar os dados fora do intervalo de acordo com a necessidade.
```python
df = df[(df['idade'] >= 18) & (df['idade'] <= 100)]
```
* **Erros de visualização**: Verificar se os gráficos e visualizações estão sendo criados corretamente e tratar os erros de visualização de acordo com a necessidade.
```python
try:
    df['categoria'].value_counts().plot(kind='bar')
    plt.show()
except Exception as e:
    print(f"Erro de visualização: {e}")
