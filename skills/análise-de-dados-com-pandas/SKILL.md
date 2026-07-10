---
name: Análise de Dados com Pandas e NumPy
description: Manipulação e análise de dados utilizando as bibliotecas Pandas e NumPy
---

## Objetivo
O objetivo desta habilidade é capacitar o usuário a manipular e analisar dados utilizando as bibliotecas Pandas e NumPy, incluindo a criação de gráficos e estatísticas descritivas. Com isso, o usuário poderá extrair insights valiosos de conjuntos de dados e tomar decisões informadas.

## Pré-requisitos
Para utilizar esta habilidade, é necessário ter conhecimento básico em Python e experiência em trabalhar com dados. Além disso, é recomendado ter instalado as bibliotecas Pandas e NumPy em seu ambiente de desenvolvimento.

## Passo a Passo Técnico / Exemplos de Código
### Instalação das Bibliotecas
Para instalar as bibliotecas Pandas e NumPy, execute o seguinte comando no seu terminal:
```bash
pip install pandas numpy
```
### Importação das Bibliotecas
Para utilizar as bibliotecas, é necessário importá-las no seu script Python:
```python
import pandas as pd
import numpy as np
```
### Criação de um DataFrame
Um DataFrame é uma estrutura de dados bidimensional que pode ser utilizada para armazenar e manipular dados. Para criar um DataFrame, utilize a seguinte sintaxe:
```python
data = {'Nome': ['João', 'Maria', 'Pedro'], 
        'Idade': [25, 31, 42]}
df = pd.DataFrame(data)
```
### Criação de Gráficos
Para criar gráficos, é possível utilizar a biblioteca Matplotlib em conjunto com o Pandas. Aqui está um exemplo de como criar um gráfico de barras:
```python
import matplotlib.pyplot as plt

df['Idade'].plot(kind='bar')
plt.title('Idade dos Indivíduos')
plt.xlabel('Nome')
plt.ylabel('Idade')
plt.show()
```
### Estatísticas Descritivas
Para calcular estatísticas descritivas, como média, mediana e desvio padrão, utilize a seguinte sintaxe:
```python
print(df['Idade'].mean())
print(df['Idade'].median())
print(df['Idade'].std())
```

## Validação
Para validar a habilidade, é necessário testar os exemplos de código e verificar se os resultados estão corretos. Além disso, é recomendado criar seus próprios exemplos e testar as funcionalidades das bibliotecas Pandas e NumPy. Com isso, você poderá garantir que está utilizando as bibliotecas de forma eficaz e extrair insights valiosos de seus conjuntos de dados.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros de Instalação
Se ocorrer um erro durante a instalação das bibliotecas, verifique se o pip está atualizado e se o comando foi executado corretamente.
```bash
pip install --upgrade pip
pip install pandas numpy
```
### Tratamento de Erros de Importação
Se ocorrer um erro durante a importação das bibliotecas, verifique se as bibliotecas foram instaladas corretamente e se o nome da biblioteca está correto.
```python
try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Erro ao importar as bibliotecas. Verifique a instalação.")
```
### Tratamento de Erros de Criação de DataFrame
Se ocorrer um erro durante a criação de um DataFrame, verifique se os dados estão no formato correto e se as colunas estão sendo criadas corretamente.
```python
try:
    data = {'Nome': ['João', 'Maria', 'Pedro'], 
            'Idade': [25, 31, 42]}
    df = pd.DataFrame(data)
except ValueError:
    print("Erro ao criar o DataFrame. Verifique os dados.")
```
### Tratamento de Erros de Criação de Gráficos
Se ocorrer um erro durante a criação de um gráfico, verifique se a biblioteca Matplotlib está instalada e se o código está correto.
```python
try:
    import matplotlib.pyplot as plt
    df['Idade'].plot(kind='bar')
    plt.title('Idade dos Indivíduos')
    plt.xlabel('Nome')
    plt.ylabel('Idade')
    plt.show()
except ImportError:
    print("Erro ao importar a biblioteca Matplotlib. Verifique a instalação.")
```
### Tratamento de Erros de Estatísticas Descritivas
Se ocorrer um erro durante o cálculo de estatísticas descritivas, verifique se os dados estão no formato correto e se as funções estão sendo utilizadas corretamente.
```python
try:
    print(df['Idade'].mean())
    print(df['Idade'].median())
    print(df['Idade'].std())
except TypeError:
    print("Erro ao calcular as estatísticas descritivas. Verifique os dados.")
```
