---
name: Automação de Testes com Cypress
description: Esta skill ensina como automatizar testes de aplicações web utilizando o framework Cypress, incluindo a criação de testes unitários e integração
---

## Objetivo
O objetivo desta skill é capacitar os desenvolvedores a criar testes automatizados para aplicações web utilizando o framework Cypress, melhorando a eficiência e a confiabilidade dos testes.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento básico em:
* Desenvolvimento web
* JavaScript
* Familiaridade com o terminal ou prompt de comando

## Passo a Passo Técnico / Exemplos de Código
### Instalação do Cypress
Para começar a utilizar o Cypress, é necessário instalá-lo em seu projeto. Isso pode ser feito utilizando o npm ou o yarn:
```bash
npm install cypress
```
ou
```bash
yarn add cypress
```
Em caso de erro durante a instalação, verifique se o npm ou yarn está atualizado e se o projeto está configurado corretamente.

### Configuração do Cypress
Após a instalação, é necessário configurar o Cypress para que ele possa ser executado em seu projeto. Isso pode ser feito criando um arquivo `cypress.json` na raiz do seu projeto:
```json
{
  "baseUrl": "https://example.com"
}
```
Certifique-se de que o arquivo `cypress.json` esteja no formato JSON correto e que o `baseUrl` seja uma URL válida.

### Criação de Testes
Com o Cypress configurado, agora é possível criar testes para sua aplicação. Por exemplo, para testar se um botão está visível na página:
```javascript
describe('Botão', () => {
  it('Deve estar visível', () => {
    cy.visit('https://example.com')
    cy.get('button').should('be.visible')
  })
})
```
Lembre-se de que os seletores de elementos devem ser específicos e únicos para evitar ambiguidades.

## Validação
Para validar se os testes estão funcionando corretamente, é possível executá-los utilizando o comando:
```bash
npx cypress run
```
Isso irá executar todos os testes e mostrar os resultados no terminal. Além disso, é possível utilizar o modo de depuração do Cypress para visualizar os testes sendo executados em tempo real:
```bash
npx cypress open
```
Em caso de falha nos testes, verifique os logs do Cypress para identificar o problema.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
Para lidar com erros durante a execução dos testes, é possível utilizar o bloco `try-catch` para capturar e tratar as exceções:
```javascript
describe('Botão', () => {
  it('Deve estar visível', () => {
    try {
      cy.visit('https://example.com')
      cy.get('button').should('be.visible')
    } catch (error) {
      console.error('Erro ao executar o teste:', error)
    }
  })
})
```
### Edge Cases
Alguns exemplos de edge cases que devem ser considerados:
* **URL inválida**: o que acontece se a URL do `baseUrl` for inválida?
* **Elemento não encontrado**: o que acontece se o elemento não for encontrado na página?
* **Timeout**: o que acontece se o teste demorar muito para executar?
Para lidar com esses casos, é possível adicionar verificações e tratamentos específicos nos testes:
```javascript
describe('Botão', () => {
  it('Deve estar visível', () => {
    cy.visit('https://example.com')
    cy.get('button', { timeout: 10000 }).should('be.visible')
  })
})
```
Nesse exemplo, o timeout para encontrar o elemento é de 10 segundos. Se o elemento não for encontrado dentro desse tempo, o teste falhará.