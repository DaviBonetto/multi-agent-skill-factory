---
name: Análise de Dados com Pandas e Python
description: Esta habilidade ensina como utilizar a biblioteca Pandas para analisar e manipular dados em Python, incluindo importação de dados, limpeza e transformação.
---

## Objetivo
O objetivo desta habilidade é capacitar o usuário a utilizar a biblioteca Pandas para analisar e manipular dados em Python, incluindo importação de dados, limpeza e transformação, de forma eficiente e prática.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento básico em Python e ter a biblioteca Pandas instalada. Além disso, é recomendado ter um ambiente de desenvolvimento configurado, como o Jupyter Notebook ou o PyCharm.

## Passo a Passo Técnico / Exemplos de Código
### Importação de Dados
A importação de dados é o primeiro passo para começar a analisar e manipular dados. A biblioteca Pandas oferece várias opções para importar dados, incluindo arquivos CSV, Excel e JSON.
```python
import pandas as pd

# Importando dados de um arquivo CSV
try:
    df = pd.read_csv('dados.csv')
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
except pd.errors.EmptyDataError:
    print("Arquivo vazio. Verifique se o arquivo contém dados.")
except pd.errors.ParserError:
    print("Erro ao parsear o arquivo. Verifique se o arquivo está no formato correto.")

# Importando dados de um arquivo Excel
try:
    df = pd.read_excel('dados.xlsx')
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
except ValueError:
    print("Erro ao ler o arquivo Excel. Verifique se o arquivo está no formato correto.")

# Importando dados de um arquivo JSON
try:
    df = pd.read_json('dados.json')
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
except ValueError:
    print("Erro ao ler o arquivo JSON. Verifique se o arquivo está no formato correto.")
```

### Limpeza e Transformação de Dados
Após importar os dados, é necessário limpar e transformar os dados para que eles estejam prontos para análise. Isso pode incluir remover linhas vazias, converter tipos de dados e renomear colunas.
```python
# Removendo linhas vazias
try:
    df = df.dropna()
except TypeError:
    print("Erro ao remover linhas vazias. Verifique se o dataframe está vazio.")

# Convertendo tipo de dados
try:
    df['coluna'] = pd.to_numeric(df['coluna'])
except ValueError:
    print("Erro ao converter tipo de dados. Verifique se a coluna contém valores numéricos.")

# Renomeando colunas
try:
    df = df.rename(columns={'coluna_antiga': 'coluna_nova'})
except KeyError:
    print("Erro ao renomear colunas. Verifique se a coluna existe no dataframe.")
```

### Análise de Dados
Com os dados limpos e transformados, é possível começar a analisar os dados. A biblioteca Pandas oferece várias opções para analisar dados, incluindo agrupamento, filtragem e ordenação.
```python
# Agrupando dados
try:
    df_grupo = df.groupby('coluna').sum()
except KeyError:
    print("Erro ao agrupar dados. Verifique se a coluna existe no dataframe.")

# Filtrando dados
try:
    df_filtro = df[df['coluna'] > 10]
except KeyError:
    print("Erro ao filtrar dados. Verifique se a coluna existe no dataframe.")

# Ordenando dados
try:
    df_ordenado = df.sort_values(by='coluna')
except KeyError:
    print("Erro ao ordenar dados. Verifique se a coluna existe no dataframe.")
```

## Validação
Para validar os resultados, é importante verificar se os dados estão corretos e se as operações realizadas estão produzindo os resultados esperados. Isso pode incluir verificar se os dados estão dentro do intervalo esperado, se as operações de agrupamento e filtragem estão corretas e se as ordenações estão sendo realizadas corretamente.
```python
# Verificando se os dados estão dentro do intervalo esperado
print(df.describe())

# Verificando se as operações de agrupamento estão corretas
print(df_grupo)

# Verificando se as ordenações estão sendo realizadas corretamente
print(df_ordenado)
```

## ⚠️ Tratamento de Exceções e Edge Cases
É importante tratar as exceções e edge cases que podem ocorrer durante a análise de dados. Isso inclui:
* Tratar erros de arquivo, como arquivos não encontrados ou arquivos vazios.
* Tratar erros de tipo de dados, como tentar converter uma coluna para um tipo de dados incorreto.
* Tratar erros de operações, como tentar realizar uma operação em uma coluna que não existe.
* Tratar erros de memória, como tentar carregar um arquivo muito grande na memória.
```python
# Exemplo de tratamento de exceção
try:
    # Código que pode gerar uma exceção
    df = pd.read_csv('dados.csv')
except Exception as e:
    # Tratamento da exceção
    print(f"Erro: {e}")
```
