---
name: Automação de Testes de Interface com Cypress
description: Aborda a automação de testes de interface de usuário utilizando o framework Cypress
---

## Objetivo
O objetivo deste guia é apresentar uma abordagem prática para a automação de testes de interface de usuário utilizando o framework Cypress. Com isso, os desenvolvedores e testadores poderão aprender a criar testes automatizados eficazes para garantir a qualidade e a confiabilidade de suas aplicações web.

## Pré-requisitos
Antes de começar, é necessário ter:
- Conhecimento básico em JavaScript e HTML/CSS
- Node.js instalado no computador
- Um projeto Cypress configurado (pode ser criado utilizando o comando `npx cypress open`)

## Passo a Passo Técnico / Exemplos de Código
### Instalação do Cypress
Para instalar o Cypress, execute o seguinte comando no terminal:
```bash
npm install cypress
```
### Configuração do Projeto
Após a instalação, é necessário configurar o projeto. Isso pode ser feito criando um arquivo `cypress/support/index.js` com o seguinte conteúdo:
```javascript
// cypress/support/index.js
import './commands'
```
E um arquivo `cypress/support/commands.js` com os comandos personalizados:
```javascript
// cypress/support/commands.js
Cypress.Commands.add('login', (username, password) => {
  cy.get('input[name="username"]').type(username)
  cy.get('input[name="password"]').type(password)
  cy.get('button[type="submit"]').click()
})
```
### Escrita de Testes
Agora, é possível começar a escrever testes. Por exemplo, para testar o login de um usuário, crie um arquivo `cypress/integration/login.spec.js` com o seguinte conteúdo:
```javascript
// cypress/integration/login.spec.js
describe('Login', () => {
  it('deve realizar login com sucesso', () => {
    cy.visit('https://example.com/login')
    cy.login('username', 'password')
    cy.url().should('eq', 'https://example.com/dashboard')
  })
})
```
## Validação
Para executar os testes e validar a automação, basta executar o comando `npx cypress run` no terminal. Isso irá executar todos os testes configurados e exibir os resultados no console. Além disso, é possível visualizar os testes em execução utilizando o comando `npx cypress open`, que irá abrir a interface gráfica do Cypress.

## ⚠️ Tratamento de Exceções e Edge Cases
É importante considerar os seguintes casos de exceção e edge cases ao criar testes automatizados com Cypress:
- **Erro de rede**: O Cypress pode falhar ao tentar acessar uma URL se houver um problema de rede. Para lidar com isso, é possível adicionar um retry ao comando `cy.visit()`:
```javascript
cy.visit('https://example.com/login', { retry: 3 })
```
- **Elementos não encontrados**: Se um elemento não for encontrado na página, o Cypress irá falhar. Para lidar com isso, é possível adicionar um timeout ao comando `cy.get()`:
```javascript
cy.get('input[name="username"]', { timeout: 10000 })
```
- **Autenticação**: Se a aplicação web exigir autenticação, é necessário lidar com isso nos testes. Uma forma de fazer isso é utilizar o comando `cy.login()` personalizado:
```javascript
Cypress.Commands.add('login', (username, password) => {
  cy.get('input[name="username"]').type(username)
  cy.get('input[name="password"]').type(password)
  cy.get('button[type="submit"]').click()
})
```
- **Diferenças de navegador**: Os testes podem se comportar de forma diferente em diferentes navegadores. Para lidar com isso, é possível utilizar o comando `cy.viewport()` para definir o tamanho da janela do navegador:
```javascript
cy.viewport(1280, 720)
```
- **Diferenças de plataforma**: Os testes podem se comportar de forma diferente em diferentes plataformas (por exemplo, Windows, macOS, Linux). Para lidar com isso, é possível utilizar o comando `cy.exec()` para executar comandos do sistema operacional:
```javascript
cy.exec('ls -l')
```
Ao considerar esses casos de exceção e edge cases, é possível criar testes automatizados mais robustos e confiáveis com Cypress.
