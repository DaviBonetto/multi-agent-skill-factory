---
name: Desenvolvimento de Aplicativos Móveis com React Native
description: Esta habilidade ensina como criar aplicativos móveis para Android e iOS utilizando React Native, incluindo design de interfaces, navegação e integração com APIs, abordando também tratamento de exceções e edge cases para uma experiência de usuário robusta.

## Objetivo
O objetivo desta habilidade é capacitar os desenvolvedores a criar aplicativos móveis para Android e iOS utilizando React Native, abordando desde o design de interfaces até a integração com APIs, garantindo uma experiência de usuário cross-plataforma de alta qualidade, aproveitando a eficiência e a flexibilidade do React Native.

## Pré-requisitos
Para começar a desenvolver aplicativos móveis com React Native, é necessário ter:
- Conhecimento básico em JavaScript e React
- Noção de desenvolvimento de aplicativos móveis
- Ambiente de desenvolvimento configurado com Node.js, npm e React Native CLI
- Dispositivos ou emuladores Android e iOS para testes

## Passo a Passo Técnico / Exemplos de Código
### Configurando o Ambiente
Primeiramente, é necessário configurar o ambiente de desenvolvimento. Isso inclui instalar o Node.js, npm e o React Native CLI. Você pode instalar o React Native CLI usando o seguinte comando:
```bash
npm install -g react-native-cli
```
### Criando um Novo Projeto
Para criar um novo projeto React Native, use o comando:
```bash
npx react-native init NomeDoProjeto
```
Substitua `NomeDoProjeto` pelo nome do seu projeto.

### Design de Interfaces
O design de interfaces é crucial para a experiência do usuário. React Native oferece componentes prontos para uso, como `View`, `Text`, `Image`, entre outros. Por exemplo, para criar uma tela de boas-vindas, você pode usar:
```jsx
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const TelaBoasVindas = () => {
  return (
    <View style={styles.container}>
      <Text>Bem-vindo!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default TelaBoasVindas;
```
### Navegação
Para navegar entre telas, você pode usar o `react-navigation`. Primeiro, instale-o:
```bash
npm install @react-navigation/native
```
E então, configure a navegação:
```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import TelaBoasVindas from './TelaBoasVindas';
import OutraTela from './OutraTela';

const Stack = createStackNavigator();

const Navegador = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="BoasVindas" component={TelaBoasVindas} />
        <Stack.Screen name="OutraTela" component={OutraTela} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default Navegador;
```
### Integração com APIs
Para integrar seu aplicativo com APIs, você pode usar o `fetch` ou bibliotecas como `axios`. Por exemplo, para fazer uma requisição GET:
```jsx
import axios from 'axios';

const buscarDados = async () => {
  try {
    const resposta = await axios.get('https://api.exemplo.com/dados');
    console.log(resposta.data);
  } catch (erro) {
    console.error(erro);
  }
};
```
## Validação
Para validar o funcionamento do aplicativo, é importante testá-lo em diferentes dispositivos e emuladores, tanto para Android quanto para iOS. Além disso, utilize ferramentas de debugging como o React Native Debugger para identificar e solucionar problemas. Certifique-se de que todas as funcionalidades estejam trabalhando como esperado, incluindo a navegação, a integração com APIs e o design responsivo.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros de Rede
Ao fazer requisições de rede, é importante tratar erros que possam ocorrer devido a problemas de conexão ou ao servidor. Por exemplo:
```jsx
import axios from 'axios';

const buscarDados = async () => {
  try {
    const resposta = await axios.get('https://api.exemplo.com/dados');
    console.log(resposta.data);
  } catch (erro) {
    if (erro.response) {
      // O servidor respondeu com um código de status de erro
      console.log(erro.response.data);
      console.log(erro.response.status);
      console.log(erro.response.headers);
    } else if (erro.request) {
      // A requisição foi feita, mas não houve resposta
      console.log(erro.request);
    } else {
      // Ocorreu um erro ao configurar a requisição
      console.log('Erro', erro.message);
    }
    console.log(erro.config);
  }
};
```
### Tratamento de Erros de Interface
Ao trabalhar com interfaces do usuário, é importante tratar erros que possam ocorrer devido a entradas inválidas do usuário. Por exemplo:
```jsx
import React, { useState } from 'react';
import { View, Text, TextInput, StyleSheet } from 'react-native';

const TelaLogin = () => {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState(null);

  const handleLogin = () => {
    if (!email || !senha) {
      setErro('Por favor, preencha todos os campos');
    } else {
      // Lógica de login
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="E-mail"
        value={email}
        onChangeText={(texto) => setEmail(texto)}
      />
      <TextInput
        style={styles.input}
        placeholder="Senha"
        secureTextEntry
        value={senha}
        onChangeText={(texto) => setSenha(texto)}
      />
      {erro && <Text style={styles.erro}>{erro}</Text>}
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    width: 300,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    padding: 10,
  },
  erro: {
    color: 'red',
    marginBottom: 10,
  },
});

export default TelaLogin;
```
### Edge Cases de Navegação
Ao trabalhar com navegação, é importante considerar edge cases como a navegação para telas que não existem ou a falta de permissão para acessar certas telas. Por exemplo:
```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import TelaBoasVindas from './TelaBoasVindas';
import OutraTela from './OutraTela';

const Stack = createStackNavigator();

const Navegador = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="BoasVindas" component={TelaBoasVindas} />
        <Stack.Screen name="OutraTela" component={OutraTela} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default Navegador;
```
Neste exemplo, se o usuário tentar navegar para uma tela que não existe, o aplicativo não irá quebrar, mas sim, não irá fazer nada. Para tratar isso, você pode adicionar um evento de erro na navegação:
```jsx
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import TelaBoasVindas from './TelaBoasVindas';
import OutraTela from './OutraTela';

const Stack = createStackNavigator();

const Navegador = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="BoasVindas" component={TelaBoasVindas} />
        <Stack.Screen name="OutraTela" component={OutraTela} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

Navegador.onError = (erro) => {
  console.log(erro);
};

export default Navegador;
