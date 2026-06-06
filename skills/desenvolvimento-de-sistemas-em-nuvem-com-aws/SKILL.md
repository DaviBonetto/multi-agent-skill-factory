---
name: Desenvolvimento de Sistemas em Nuvem com AWS
description: Esta habilidade ensina como criar sistemas em nuvem escaláveis e seguros utilizando a plataforma AWS
---

## Objetivo
O objetivo desta habilidade é capacitar os desenvolvedores a criar sistemas em nuvem escaláveis e seguros utilizando a plataforma AWS. Isso inclui entender como projetar e implementar arquiteturas de nuvem, utilizar serviços AWS como EC2, S3, RDS e Lambda, e garantir a segurança e escalabilidade dos sistemas.

## Pré-requisitos
Para aproveitar ao máximo esta habilidade, é recomendado que os desenvolvedores tenham:
* Conhecimento básico de programação em linguagens como Java, Python ou C#
* Experiência com desenvolvimento de sistemas distribuídos
* Conhecimento básico de redes e segurança de sistemas
* Conta na AWS com acesso a serviços como EC2, S3, RDS e Lambda

## Passo a Passo Técnico / Exemplos de Código
### Criando uma Instância EC2
1. Acesse o console da AWS e navegue até o serviço EC2.
2. Clique em "Launch Instance" e selecione a imagem do sistema operacional desejada.
3. Configure as configurações de instância, como tipo de instância, grupo de segurança e chave SSH.
4. Clique em "Launch" para criar a instância.

```bash
# Exemplo de comando para criar uma instância EC2 usando o CLI da AWS
aws ec2 run-instances --image-id ami-abc123 --instance-type t2.micro --key-name minha-chave
```

### Criando um Bucket S3
1. Acesse o console da AWS e navegue até o serviço S3.
2. Clique em "Create bucket" e insira o nome do bucket.
3. Configure as configurações de bucket, como região e política de acesso.
4. Clique em "Create bucket" para criar o bucket.

```python
# Exemplo de código em Python para criar um bucket S3 usando a biblioteca Boto3
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='meu-bucket')
```

## Validação
Para validar a habilidade, é recomendado que os desenvolvedores:
* Criem uma instância EC2 e acessem via SSH
* Criem um bucket S3 e façam upload de um arquivo
* Implementem uma aplicação simples utilizando os serviços AWS, como um servidor web ou uma API REST
* Verifiquem a segurança e escalabilidade da aplicação

## ⚠️ Tratamento de Exceções e Edge Cases
Ao trabalhar com a AWS, é importante considerar os seguintes casos de exceção e edge cases:
* **Erros de autenticação**: Verifique se as credenciais de acesso à AWS estão corretas e se o usuário tem permissões suficientes para realizar as ações desejadas.
* **Erros de rede**: Verifique se a conexão de rede está estável e se o tráfego de rede está sendo bloqueado por firewalls ou grupos de segurança.
* **Erros de recursos**: Verifique se os recursos necessários, como instâncias EC2 ou buckets S3, estão disponíveis e se há recursos suficientes para realizar as ações desejadas.
* **Erros de segurança**: Verifique se as políticas de segurança estão configuradas corretamente e se os recursos estão protegidos contra acessos não autorizados.
* **Casos de limite**: Verifique se os limites de recursos, como o número de instâncias EC2 ou o tamanho do bucket S3, estão sendo respeitados.

Exemplos de código para tratamento de exceções:
```python
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

try:
    s3.create_bucket(Bucket='meu-bucket')
except ClientError as e:
    print(f"Erro ao criar bucket: {e.response['Error']['Code']}")
```

```bash
aws ec2 run-instances --image-id ami-abc123 --instance-type t2.micro --key-name minha-chave 2>&1 | grep -q "InvalidInstanceType" && echo "Erro: tipo de instância inválido"
