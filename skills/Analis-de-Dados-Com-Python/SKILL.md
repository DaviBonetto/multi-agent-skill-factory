---
name: Análise de Dados com Python
description: Esta habilidade ensina como utilizar a linguagem Python para análise de dados, incluindo manipulação de dados, visualização e aprendizado de máquina.
---

## Objetivo
O objetivo desta habilidade é capacitar os participantes a utilizar a linguagem Python para análise de dados, abordando tópicos como manipulação de dados, visualização e aprendizado de máquina, proporcionando uma base sólida para trabalhos de análise de dados.

## Pré-requisitos
Para aproveitar ao máximo esta habilidade, é recomendado que os participantes tenham:
- Conhecimento básico em programação
- Experiência com a linguagem Python
- Familiaridade com bibliotecas como Pandas, NumPy e Matplotlib

## Passo a Passo Técnico / Exemplos de Código
### Manipulação de Dados
A manipulação de dados é uma etapa crucial na análise. Utilizaremos a biblioteca Pandas para carregar e manipular dados.
```python
import pandas as pd

# Carregar dados
try:
    df = pd.read_csv('dados.csv')
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o caminho do arquivo.")
except pd.errors.EmptyDataError:
    print("Arquivo vazio. Verifique se o arquivo contém dados.")
except pd.errors.ParserError:
    print("Erro ao parsear o arquivo. Verifique o formato do arquivo.")

# Visualizar as primeiras linhas do dataframe
if not df.empty:
    print(df.head())
else:
    print("DataFrame vazio.")
```

### Visualização
A visualização dos dados é essencial para entender as tendências e padrões. Utilizaremos a biblioteca Matplotlib para criar gráficos.
```python
import matplotlib.pyplot as plt

# Criar um gráfico de barras
try:
    plt.bar(df['categoria'], df['valor'])
    plt.xlabel('Categoria')
    plt.ylabel('Valor')
    plt.title('Gráfico de Barras')
    plt.show()
except KeyError:
    print("Coluna não encontrada. Verifique as colunas do DataFrame.")
except TypeError:
    print("Tipo de dado inválido. Verifique o tipo de dado das colunas.")
```

### Aprendizado de Máquina
O aprendizado de máquina permite prever resultados com base em dados históricos. Utilizaremos a biblioteca Scikit-learn para treinar um modelo.
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dividir dados em treino e teste
try:
    X_train, X_test, y_train, y_test = train_test_split(df[['feature1', 'feature2']], df['target'], test_size=0.2, random_state=42)
except ValueError:
    print("Erro ao dividir os dados. Verifique se as colunas existem e se os dados são suficientes.")

# Treinar o modelo
try:
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
except ValueError:
    print("Erro ao treinar o modelo. Verifique se os dados são válidos e se o modelo é adequado.")
```

## Validação
Para validar os resultados, é importante testar o modelo com dados de teste e avaliar seu desempenho utilizando métricas como acurácia, precisão e recall.
```python
from sklearn.metrics import accuracy_score

# Prever resultados com o modelo treinado
try:
    previsoes = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, previsoes)
    print(f'Acurácia: {acuracia:.2f}')
except ValueError:
    print("Erro ao prever os resultados. Verifique se o modelo está treinado e se os dados são válidos.")
```

## ⚠️ Tratamento de Exceções e Edge Cases
É importante tratar as exceções e edge cases para garantir que o código seja robusto e funcione corretamente em diferentes situações. Alguns exemplos de tratamento de exceções e edge cases incluem:
- Verificar se os arquivos existem e se os dados são válidos antes de carregá-los.
- Tratar exceções ao parsear os dados, como erros de formato ou dados vazios.
- Verificar se as colunas existem e se os dados são do tipo correto antes de criar gráficos ou treinar modelos.
- Tratar exceções ao treinar o modelo, como erros de divisão de dados ou modelos inválidos.
- Verificar se os resultados são válidos e se as métricas são calculadas corretamente.
