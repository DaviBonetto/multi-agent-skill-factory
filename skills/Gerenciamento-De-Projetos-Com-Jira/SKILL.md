---
name: Gerenciamento de Projetos com Jira
description: Esta skill ensina como gerenciar projetos utilizando a ferramenta Jira, incluindo a criação de issues, configuração de workflows e relatórios
---

## Objetivo
O objetivo desta skill é ensinar como gerenciar projetos de forma eficaz utilizando a ferramenta Jira. Ao final desta skill, você será capaz de criar e gerenciar projetos, configurar workflows e gerar relatórios personalizados.

## Pré-requisitos
Para começar a utilizar esta skill, você precisa ter:
* Conhecimento básico de gerenciamento de projetos
* Acesso à ferramenta Jira
* Nível de complexidade: Junior

## Passo a Passo Técnico / Exemplos de Código
### Criando um Projeto
1. Acesse a ferramenta Jira e clique em "Criar Projeto"
2. Selecione o tipo de projeto e preencha as informações necessárias
3. Clique em "Criar" para criar o projeto

### Configurando Workflows
1. Acesse o projeto criado e clique em "Configurações"
2. Selecione "Workflows" e clique em "Criar Workflow"
3. Configure as etapas do workflow e clique em "Salvar"

### Criando Issues
1. Acesse o projeto e clique em "Criar Issue"
2. Selecione o tipo de issue e preencha as informações necessárias
3. Clique em "Criar" para criar a issue

### Exemplo de Código para Integração com Jira
```python
import requests

# Autenticação
username = "seu_usuario"
password = "sua_senha"
url = "https://seu_domínio.atlassian.net/rest/api/2/issue"

# Criação de issue
issue = {
    "fields": {
        "summary": "Exemplo de issue",
        "description": "Esta é uma issue de exemplo",
        "project": {
            "key": "SEU_PROJETO"
        }
    }
}

response = requests.post(url, json=issue, auth=(username, password))

if response.status_code == 201:
    print("Issue criada com sucesso!")
else:
    print("Erro ao criar issue")
```

## Validação
Para validar o conhecimento adquirido, você pode:
* Criar um projeto e configurar um workflow
* Criar issues e atribuí-las a membros da equipe
* Gerar relatórios personalizados para acompanhar o progresso do projeto

## ⚠️ Tratamento de Exceções e Edge Cases
* **Erro de autenticação**: Verifique se as credenciais de acesso estão corretas e se o usuário tem permissão para criar issues e projetos.
* **Projeto não encontrado**: Verifique se o projeto existe e se o usuário tem permissão para acessá-lo.
* **Issue não criada**: Verifique se as informações necessárias para criar a issue estão preenchidas corretamente e se o usuário tem permissão para criar issues.
* **Workflow não configurado**: Verifique se o workflow está configurado corretamente e se o usuário tem permissão para configurá-lo.
* **Relatórios não gerados**: Verifique se os relatórios estão configurados corretamente e se o usuário tem permissão para gerá-los.
* **Limites de API**: Verifique se as requisições à API do Jira estão dentro dos limites permitidos para evitar erros de rate limiting.
* **Erros de rede**: Verifique se a conexão de rede está estável e se não há erros de comunicação com o servidor do Jira.

Ao final desta skill, você terá adquirido as habilidades necessárias para gerenciar projetos de forma eficaz utilizando a ferramenta Jira.
