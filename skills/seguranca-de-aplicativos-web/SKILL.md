---
name: Segurança de Aplicativos Web
description: Ensina técnicas e ferramentas para proteger aplicativos web contra ataques comuns
---

## Objetivo
O objetivo deste guia é fornecer conhecimentos e habilidades necessárias para proteger aplicativos web contra ataques comuns, incluindo injeção de SQL e cross-site scripting, visando garantir a segurança e a integridade dos dados.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimentos básicos em:
* Desenvolvimento web
* Linguagens de programação como Python, Java ou C#
* Bases de dados relacionais
* Conceitos de segurança de rede

## Passo a Passo Técnico / Exemplos de Código
### Injeção de SQL
A injeção de SQL é um tipo de ataque que ocorre quando um atacante insere código SQL malicioso em um aplicativo web, visando acessar ou modificar dados sensíveis. Para prevenir isso:
* Use prepared statements com parâmetros nomeados
* Valide e sanitize todas as entradas de usuário
* Use um ORM (Object-Relational Mapping) para abstrair a interação com o banco de dados

Exemplo de código em Python:
```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

# Prepared statement com parâmetro nomeado
query = "SELECT * FROM usuarios WHERE nome = :nome"
cursor.execute(query, {'nome': 'João'})

# Fetch dos resultados
resultados = cursor.fetchall()
```

### Cross-Site Scripting (XSS)
O XSS é um tipo de ataque que ocorre quando um atacante insere código JavaScript malicioso em um aplicativo web, visando roubar dados sensíveis ou realizar ações maliciosas. Para prevenir isso:
* Use um framework de template que escape automaticamente as saídas
* Valide e sanitize todas as entradas de usuário
* Use um Content Security Policy (CSP) para definir quais fontes de conteúdo são permitidas

Exemplo de código em HTML:
```html
<!-- Escape automático de saídas com Jinja2 -->
<p>{{ nome | escape }}</p>
```

## Validação
Para validar a segurança do aplicativo web, é necessário realizar testes de penetração e auditorias de segurança regulares. Além disso, é importante manter o aplicativo e suas dependências atualizados com os últimos patches de segurança.

## ⚠️ Tratamento de Exceções e Edge Cases
Além das medidas de segurança mencionadas anteriormente, é importante considerar os seguintes casos de bordo e exceções:
* **Injeção de SQL com caracteres especiais**: Use um mecanismo de escape de caracteres para evitar que caracteres especiais sejam interpretados como código SQL.
* **XSS com código JavaScript malicioso**: Use um mecanismo de detecção de código malicioso para evitar que código JavaScript malicioso seja executado.
* **Erros de conexão com o banco de dados**: Implemente um mecanismo de retry e timeout para lidar com erros de conexão com o banco de dados.
* **Erros de validação de entrada**: Implemente um mecanismo de validação de entrada para evitar que entradas inválidas sejam processadas.
* **Ataques de força bruta**: Implemente um mecanismo de limitação de tentativas de login para evitar ataques de força bruta.

Exemplo de código em Python para tratamento de exceções:
```python
try:
    # Código que pode gerar exceção
    cursor.execute(query, {'nome': 'João'})
except sqlite3.Error as e:
    # Tratamento de exceção
    print(f"Erro: {e}")
```

Exemplo de código em Python para limitação de tentativas de login:
```python
import time

# Limite de tentativas de login
limite_tentativas = 5

# Tempo de espera entre tentativas
tempo_espera = 30

# Contador de tentativas
tentativas = 0

while tentativas < limite_tentativas:
    # Código que pode gerar exceção
    try:
        # Tenta realizar o login
        login()
        break
    except Exception as e:
        # Tratamento de exceção
        print(f"Erro: {e}")
        tentativas += 1
        time.sleep(tempo_espera)
```
