---
name: Inteligência Artificial em Sistemas de Recomendação
description: Ensina a criar sistemas de recomendação utilizando algoritmos de aprendizado de máquina como Collaborative Filtering e Content-Based Filtering
---

## Objetivo
O objetivo deste guia é ensinar como criar sistemas de recomendação utilizando algoritmos de aprendizado de máquina como Collaborative Filtering e Content-Based Filtering. Com isso, você será capaz de desenvolver soluções que forneçam recomendações personalizadas para os usuários com base em seus interesses e comportamentos.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento em:
* Programação em Python
* Bibliotecas de aprendizado de máquina como Scikit-learn e TensorFlow
* Conceitos básicos de estatística e álgebra linear
* Experiência com sistemas de recomendação é desejável, mas não obrigatória

## Passo a Passo Técnico / Exemplos de Código
### Collaborative Filtering
O Collaborative Filtering é um algoritmo que se baseia na ideia de que os usuários com interesses semelhantes tendem a ter comportamentos semelhantes. Para implementar o Collaborative Filtering, você pode seguir os seguintes passos:
1. Coletar dados de rating de itens por usuários
2. Construir uma matriz de rating de usuários x itens
3. Calcular a similaridade entre usuários utilizando medidas como a correlação de Pearson ou a distância de Jaccard
4. Prever as ratings de itens para um usuário com base nas ratings de usuários semelhantes

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Exemplo de matriz de rating de usuários x itens
rating_matrix = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4]
])

# Calcular a similaridade entre usuários
similarity_matrix = cosine_similarity(rating_matrix)

# Prever as ratings de itens para um usuário
def predict_rating(user_id, item_id):
    try:
        similar_users = np.argsort(-similarity_matrix[user_id])[:10]
        ratings = rating_matrix[similar_users, item_id]
        return np.mean(ratings)
    except IndexError:
        return 0  # Retornar uma rating padrão caso o usuário ou item não exista

print(predict_rating(0, 3))
```

### Content-Based Filtering
O Content-Based Filtering é um algoritmo que se baseia na ideia de que os itens com características semelhantes tendem a ser gostados por usuários com interesses semelhantes. Para implementar o Content-Based Filtering, você pode seguir os seguintes passos:
1. Coletar dados de características de itens
2. Construir um modelo de representação de itens utilizando técnicas como a redução de dimensionalidade ou a aprendizagem de representações
3. Calcular a similaridade entre itens com base nas características
4. Prever as ratings de itens para um usuário com base nas características dos itens

```python
import pandas as pd
from sklearn.decomposition import PCA

# Exemplo de dados de características de itens
item_features = pd.DataFrame({
    'item_id': [1, 2, 3, 4],
    'feature1': [0.5, 0.2, 0.1, 0.8],
    'feature2': [0.3, 0.6, 0.4, 0.2]
})

# Reduzir a dimensionalidade das características utilizando PCA
pca = PCA(n_components=2)
item_features_pca = pca.fit_transform(item_features.drop('item_id', axis=1))

# Calcular a similaridade entre itens
def calculate_similarity(item_id1, item_id2):
    try:
        item1_features = item_features_pca[item_id1]
        item2_features = item_features_pca[item_id2]
        return np.dot(item1_features, item2_features) / (np.linalg.norm(item1_features) * np.linalg.norm(item2_features))
    except IndexError:
        return 0  # Retornar uma similaridade padrão caso o item não exista

print(calculate_similarity(0, 1))
```

## Validação
Para validar o desempenho do sistema de recomendação, você pode utilizar métricas como:
* Precisão
* Recobro
* F1-score
* Mean Average Precision (MAP)
* Normalized Discounted Cumulative Gain (NDCG)

```python
from sklearn.metrics import precision_score, recall_score, f1_score

# Exemplo de avaliação do desempenho do sistema de recomendação
predicted_ratings = [5, 3, 1, 4]
actual_ratings = [5, 3, 1, 4]

precision = precision_score(actual_ratings, predicted_ratings, average='macro')
recall = recall_score(actual_ratings, predicted_ratings, average='macro')
f1 = f1_score(actual_ratings, predicted_ratings, average='macro')

print(f'Precisão: {precision:.4f}')
print(f'Recobro: {recall:.4f}')
print(f'F1-score: {f1:.4f}')
```

## ⚠️ Tratamento de Exceções e Edge Cases
Para garantir a robustez do sistema de recomendação, é importante tratar exceções e edge cases, como:
* **Usuários ou itens não existentes**: Retornar uma rating padrão ou uma mensagem de erro.
* **Matriz de rating esparsa**: Utilizar técnicas de preenchimento de lacunas, como a média ou a mediana.
* **Características de itens faltantes**: Utilizar técnicas de imputação de dados, como a média ou a mediana.
* **Similaridade entre usuários ou itens muito baixa**: Utilizar um threshold para determinar se a similaridade é significativa.

Exemplos de tratamento de exceções e edge cases:
```python
def predict_rating(user_id, item_id):
    try:
        # ...
    except IndexError:
        return 0  # Retornar uma rating padrão caso o usuário ou item não exista

def calculate_similarity(item_id1, item_id2):
    try:
        # ...
    except IndexError:
        return 0  # Retornar uma similaridade padrão caso o item não exista
```
