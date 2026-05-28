---
name: Desenvolvimento de Aplicativos Web com React
description: Esta habilidade técnica avançada ensina como criar aplicativos web dinâmicos e escaláveis utilizando a biblioteca React
---

## Objetivo
O objetivo desta habilidade técnica é capacitar os desenvolvedores a criar aplicativos web dinâmicos e escaláveis utilizando a biblioteca React. Com isso, os desenvolvedores poderão criar interfaces de usuário personalizadas e interativas, melhorando a experiência do usuário final.

## Pré-requisitos
Antes de iniciar esta habilidade técnica, é necessário ter conhecimento básico em:
* JavaScript
* HTML
* CSS
* Conceitos de programação orientada a objetos
* Experiência com frameworks de front-end

## Passo a Passo Técnico / Exemplos de Código
### Instalação do React
Para começar a desenvolver com React, é necessário instalar o pacote `create-react-app` utilizando o npm ou yarn:
```bash
npm install create-react-app
```
ou
```bash
yarn add create-react-app
```
Em seguida, crie um novo projeto React executando o comando:
```bash
npx create-react-app meu-projeto
```
### Estrutura do Projeto
A estrutura básica de um projeto React inclui:
* `public`: pasta que contém os arquivos estáticos, como o ícone da aplicação e o arquivo `index.html`
* `src`: pasta que contém o código fonte da aplicação
* `src/components`: pasta que contém os componentes React
* `src/App.js`: arquivo que contém o componente principal da aplicação

### Criando Componentes React
Um componente React é uma função que retorna um elemento JSX. Por exemplo:
```jsx
import React from 'react';

function Saudacao() {
  return <h1>Olá, mundo!</h1>;
}

export default Saudacao;
```
### Renderizando Componentes
Para renderizar um componente, é necessário importá-lo e utilizá-lo em outro componente. Por exemplo:
```jsx
import React from 'react';
import Saudacao from './Saudacao';

function App() {
  return (
    <div>
      <Saudacao />
    </div>
  );
}

export default App;
```
## Validação
Para validar a aplicação, é necessário executar o comando:
```bash
npm start
```
ou
```bash
yarn start
```
Isso irá iniciar o servidor de desenvolvimento e abrir a aplicação no navegador. Verifique se a aplicação está funcionando corretamente e se os componentes estão sendo renderizados corretamente.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
É importante tratar os erros que podem ocorrer durante a execução da aplicação. Por exemplo, se um componente não for encontrado, é possível tratar o erro utilizando o método `componentDidCatch`:
```jsx
import React, { Component } from 'react';

class App extends Component {
  componentDidCatch(error, info) {
    console.error('Erro:', error);
    console.error('Info:', info);
  }

  render() {
    return (
      <div>
        <Saudacao />
      </div>
    );
  }
}

export default App;
```
### Edge Cases
Alguns exemplos de edge cases que devem ser considerados:
* **Componentes não encontrados**: se um componente não for encontrado, a aplicação deve tratar o erro e exibir uma mensagem de erro ao usuário.
* **Dados inválidos**: se os dados recebidos forem inválidos, a aplicação deve tratar o erro e exibir uma mensagem de erro ao usuário.
* **Conexão de rede perdida**: se a conexão de rede for perdida, a aplicação deve tratar o erro e exibir uma mensagem de erro ao usuário.
* **Tamanho de tela**: a aplicação deve ser responsiva e se adaptar a diferentes tamanhos de tela.
* **Dispositivos móveis**: a aplicação deve ser compatível com dispositivos móveis e se adaptar a diferentes tipos de dispositivos.

Exemplo de como tratar o edge case de componente não encontrado:
```jsx
import React from 'react';

function Saudacao() {
  if (!Saudacao) {
    return <div>Componente não encontrado</div>;
  }
  return <h1>Olá, mundo!</h1>;
}

export default Saudacao;
```
Exemplo de como tratar o edge case de dados inválidos:
```jsx
import React from 'react';

function Saudacao(props) {
  if (!props.nome) {
    return <div>Dados inválidos</div>;
  }
  return <h1>Olá, {props.nome}!</h1>;
}

export default Saudacao;
