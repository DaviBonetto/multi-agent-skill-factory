---
name: Desenvolvimento de Aplicativos Móvel com React Native
description: Esta skill ensina a desenvolver aplicativos móveis para Android e iOS utilizando React Native, abordando conceitos como componentes, navegação e integração com APIs, além de tratamento de exceções e edge cases.

## Objetivo
O objetivo desta skill é capacitar os desenvolvedores a criar aplicativos móveis para Android e iOS utilizando a tecnologia React Native, abordando conceitos fundamentais como componentes, navegação e integração com APIs, garantindo a robustez e a segurança dos aplicativos.

## Pré-requisitos
Para iniciar esta skill, é necessário ter conhecimento prévio em:
* Desenvolvimento de aplicações web com JavaScript e React
* Conceitos básicos de programação orientada a objetos
* Familiaridade com o ecossistema de desenvolvimento de aplicativos móveis

## Passo a Passo Técnico / Exemplos de Código
### Instalação do React Native
Para começar a desenvolver aplicativos móveis com React Native, é necessário instalar o framework e configurar o ambiente de desenvolvimento. Isso pode ser feito executando o seguinte comando no terminal:
```bash
npm install -g react-native-cli
```
### Criação de um Novo Projeto
Após a instalação, crie um novo projeto React Native executando:
```bash
npx react-native init NomeDoProjeto
```
### Desenvolvimento de Componentes
Os componentes são a base para a construção de interfaces de usuário em React Native. Um exemplo de componente simples é:
```jsx
import React from 'react';
import { View, Text } from 'react-native';

const MeuComponente = () => {
  return (
    <View>
      <Text>Olá, Mundo!</Text>
    </View>
  );
};

export default MeuComponente;
```
### Navegação entre Telas
A navegação entre telas é fundamental em aplicativos móveis. O React Navigation é uma biblioteca popular para gerenciar a navegação:
```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import TelaPrincipal from './TelaPrincipal';
import TelaSecundaria from './TelaSecundaria';

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="TelaPrincipal" component={TelaPrincipal} />
        <Stack.Screen name="TelaSecundaria" component={TelaSecundaria} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
```
### Integração com APIs
A integração com APIs é crucial para obter dados dinâmicos. O Axios é uma biblioteca popular para fazer requisições HTTP:
```jsx
import axios from 'axios';

const obterDados = async () => {
  try {
    const resposta = await axios.get('https://api.exemplo.com/dados');
    console.log(resposta.data);
  } catch (erro) {
    console.error(erro);
  }
};
```
## Validação
Para validar o conhecimento adquirido, é recomendado desenvolver um aplicativo móvel completo que aborde os conceitos aprendidos, como componentes, navegação e integração com APIs. Além disso, é importante testar o aplicativo em diferentes dispositivos e plataformas para garantir a compatibilidade e a usabilidade.

## ⚠️ Tratamento de Exceções e Edge Cases
Para garantir a robustez e a segurança dos aplicativos, é fundamental tratar exceções e edge cases. Aqui estão alguns exemplos:
* **Tratamento de erros de rede**: ao fazer requisições HTTP, é importante tratar erros de rede, como perda de conexão ou timeouts.
```jsx
import axios from 'axios';

const obterDados = async () => {
  try {
    const resposta = await axios.get('https://api.exemplo.com/dados');
    console.log(resposta.data);
  } catch (erro) {
    if (erro.response) {
      // Tratar erros de resposta
      console.error(erro.response.data);
    } else if (erro.request) {
      // Tratar erros de requisição
      console.error(erro.request);
    } else {
      // Tratar erros desconhecidos
      console.error(erro);
    }
  }
};
```
* **Tratamento de erros de parsing**: ao receber dados em formato JSON, é importante tratar erros de parsing.
```jsx
import axios from 'axios';

const obterDados = async () => {
  try {
    const resposta = await axios.get('https://api.exemplo.com/dados');
    const dados = JSON.parse(resposta.data);
    console.log(dados);
  } catch (erro) {
    if (erro instanceof SyntaxError) {
      // Tratar erros de parsing
      console.error('Erro de parsing:', erro);
    } else {
      // Tratar erros desconhecidos
      console.error(erro);
    }
  }
};
```
* **Tratamento de edge cases**: é importante tratar edge cases, como entrada de usuário inválida ou falta de permissões.
```jsx
import React from 'react';
import { View, Text } from 'react-native';

const MeuComponente = () => {
  const [entrada, setEntrada] = React.useState('');

  const handleEntrada = (texto) => {
    if (texto.length > 10) {
      // Tratar entrada inválida
      console.error('Entrada inválida');
    } else {
      setEntrada(texto);
    }
  };

  return (
    <View>
      <Text>Olá, Mundo!</Text>
      <TextInput value={entrada} onChangeText={handleEntrada} />
    </View>
  );
};

export default MeuComponente;
```
