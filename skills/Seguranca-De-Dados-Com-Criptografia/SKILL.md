---
name: Segurança de Dados com Criptografia
description: Esta habilidade apresenta as principais técnicas de criptografia para proteger dados sensíveis
---

## Objetivo
O objetivo desta habilidade é apresentar as principais técnicas de criptografia para proteger dados sensíveis, garantindo a confidencialidade, integridade e autenticidade das informações.

## Pré-requisitos
Antes de começar, é necessário ter conhecimento básico em:
* Conceitos de criptografia
* Protocolos de segurança de dados
* Linguagens de programação (preferencialmente Python)

## Passo a Passo Técnico / Exemplos de Código
### Introdução à Criptografia
A criptografia é a prática de proteger a confidencialidade, integridade e autenticidade de dados por meio de técnicas matemáticas. Existem dois tipos principais de criptografia:
* Criptografia Simétrica: utiliza a mesma chave para criptografar e descriptografar os dados.
* Criptografia Assimétrica: utiliza uma chave pública para criptografar e uma chave privada para descriptografar os dados.

### Exemplo de Criptografia Simétrica em Python
```python
from cryptography.fernet import Fernet

# Gera uma chave simétrica
chave = Fernet.generate_key()

# Cria um objeto Fernet
cipher_suite = Fernet(chave)

# Texto a ser criptografado
texto = "Este é um texto secreto"

# Criptografa o texto
texto_criptografado = cipher_suite.encrypt(texto.encode())

# Descriptografa o texto
texto_descriptografado = cipher_suite.decrypt(texto_criptografado).decode()

print("Texto Original:", texto)
print("Texto Criptografado:", texto_criptografado)
print("Texto Descriptografado:", texto_descriptografado)
```

### Exemplo de Criptografia Assimétrica em Python
```python
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Gera uma chave assimétrica
chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Gera uma chave pública
chave_publica = chave_privada.public_key()

# Texto a ser criptografado
texto = "Este é um texto secreto"

# Criptografa o texto
texto_criptografado = chave_publica.encrypt(
    texto.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Descriptografa o texto
texto_descriptografado = chave_privada.decrypt(
    texto_criptografado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
).decode()

print("Texto Original:", texto)
print("Texto Criptografado:", texto_criptografado)
print("Texto Descriptografado:", texto_descriptografado)
```

## Validação
Para validar a implementação da criptografia, é necessário testar a confidencialidade, integridade e autenticidade dos dados. Isso pode ser feito por meio de testes automatizados e manuais, garantindo que os dados sejam protegidos corretamente e que as chaves sejam gerenciadas de forma segura. Além disso, é importante realizar auditorias regulares para garantir a conformidade com as políticas de segurança de dados.

## ⚠️ Tratamento de Exceções e Edge Cases
É fundamental tratar exceções e edge cases para garantir a robustez e segurança da implementação da criptografia. Alguns exemplos incluem:
* **Chave inválida**: tratar exceções quando a chave é inválida ou não pode ser gerada.
* **Texto vazio**: tratar exceções quando o texto a ser criptografado é vazio.
* **Tamanho da chave**: tratar exceções quando o tamanho da chave é inválido.
* **Algoritmo de criptografia**: tratar exceções quando o algoritmo de criptografia é inválido ou não suportado.
* **Erros de descriptografia**: tratar exceções quando ocorrem erros durante a descriptografia, como chaves inválidas ou texto corrompido.

Exemplo de tratamento de exceções em Python:
```python
try:
    # Gera uma chave simétrica
    chave = Fernet.generate_key()
except Exception as e:
    print("Erro ao gerar chave:", e)

try:
    # Criptografa o texto
    texto_criptografado = cipher_suite.encrypt(texto.encode())
except Exception as e:
    print("Erro ao criptografar texto:", e)

try:
    # Descriptografa o texto
    texto_descriptografado = cipher_suite.decrypt(texto_criptografado).decode()
except Exception as e:
    print("Erro ao descriptografar texto:", e)
```
