---
name: Automação de Testes com Cypress
description: Esta skill ensina como automatizar testes de aplicativos web utilizando Cypress, incluindo testes unitários, de integração e end-to-end.
---

## Objetivo
O objetivo desta skill é capacitar os desenvolvedores a criar testes automatizados para aplicativos web utilizando o framework Cypress, abordando testes unitários, de integração e end-to-end. Com isso, os desenvolvedores poderão garantir a qualidade e a confiabilidade dos aplicativos web de forma eficiente.

## Pré-requisitos
Para iniciar esta skill, é necessário ter conhecimento básico em:
- Desenvolvimento web (HTML, CSS, JavaScript)
- Frameworks de testes
- Ambiente de desenvolvimento (Node.js, npm ou yarn)

## Passo a Passo Técnico / Exemplos de Código
### Instalação do Cypress
Para começar, é necessário instalar o Cypress no projeto. Isso pode ser feito via npm ou yarn:
```bash
npm install cypress
```
ou
```bash
yarn add cypress
```
**Atenção:** Certifique-se de que o Node.js e o npm ou yarn estejam instalados e configurados corretamente no seu ambiente de desenvolvimento.

### Configuração do Cypress
Após a instalação, é necessário configurar o Cypress. Isso pode ser feito editando o arquivo `cypress.json`:
```json
{
  "baseUrl": "https://example.com",
  "viewportWidth": 1280,
  "viewportHeight": 720
}
```
**Observação:** O arquivo `cypress.json` deve ser criado na raiz do projeto. Se o arquivo não existir, o Cypress não funcionará corretamente.

### Escrita de Testes
Agora, é possível começar a escrever testes. Por exemplo, um teste simples para verificar se um elemento está visível:
```javascript
describe('Visibilidade do elemento', () => {
  it('Deve estar visível', () => {
    cy.visit('https://example.com');
    cy.get('#meu-elemento').should('be.visible');
  });
});
```
**Dica:** Utilize o comando `cy.get()` para selecionar elementos da página e o método `should()` para verificar as condições de teste.

## Validação
Para validar os testes, basta executar o comando:
```bash
npx cypress run
```
Isso irá executar todos os testes e exibir os resultados no terminal. Além disso, é possível visualizar os testes em modo interativo com:
```bash
npx cypress open
```
**Atenção:** Certifique-se de que o Cypress esteja configurado corretamente e que os testes estejam escritos de forma válida.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
Para tratar erros durante a execução dos testes, é possível utilizar o bloco `try-catch`:
```javascript
try {
  cy.get('#meu-elemento').should('be.visible');
} catch (error) {
  console.error('Erro ao executar o teste:', error);
}
```
**Observação:** O bloco `try-catch` deve ser utilizado com cautela, pois pode mascarar erros importantes.

### Edge Cases
Alguns exemplos de edge cases que devem ser considerados:
* **Elementos dinâmicos:** Elementos que são carregados dinamicamente após a página ser carregada.
* **Elementos ocultos:** Elementos que estão ocultos ou não são visíveis na página.
* **Elementos com atributos especiais:** Elementos com atributos especiais, como `disabled` ou `readonly`.
* **Páginas com carregamento lento:** Páginas que demoram muito tempo para carregar.

Para lidar com esses edge cases, é possível utilizar comandos como `cy.wait()` para aguardar a carga de elementos dinâmicos ou `cy.get()` com seletores mais específicos para selecionar elementos ocultos ou com atributos especiais.

```javascript
// Aguardar a carga de um elemento dinâmico
cy.wait('@meu-requisicao').then(() => {
  cy.get('#meu-elemento').should('be.visible');
});

// Selecionar um elemento oculto
cy.get('#meu-elemento', { includeHidden: true }).should('be.visible');
```
**Dica:** Utilize o comando `cy.log()` para registrar informações importantes durante a execução dos testes.