---
name: Desenvolvimento de Aplicativos Móveis com React Native
description: Ensina como criar aplicativos móveis cross-plataforma utilizando React Native, incluindo integração com APIs e armazenamento de dados locais.
---

## Objetivo
O objetivo deste guia é fornecer uma visão geral detalhada sobre como desenvolver aplicativos móveis cross-plataforma utilizando React Native. Isso inclui a configuração do ambiente de desenvolvimento, a criação de interfaces de usuário, a integração com APIs e o armazenamento de dados locais.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento prévio em:
- JavaScript
- React
- Conceitos básicos de desenvolvimento móvel
- Ter o Node.js e o JDK (para Android) ou o Xcode (para iOS) instalados no computador

## Passo a Passo Técnico / Exemplos de Código
### Configurando o Ambiente de Desenvolvimento
1. Instale o React Native CLI usando npm:
   ```bash
npm install -g react-native-cli
```
2. Crie um novo projeto React Native:
   ```bash
npx react-native init NomeDoProjeto
```

### Criando a Interface de Usuário
1. Abra o arquivo `App.js` no diretório do seu projeto e comece a criar sua interface de usuário utilizando componentes React Native.

### Integração com APIs
1. Utilize a biblioteca `fetch` para fazer requisições HTTP:
   ```javascript
fetch('https://api.exemplo.com/dados')
  .then(response => {
    if (!response.ok) {
      throw new Error('Erro ao fazer requisição');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

### Armazenamento de Dados Locais
1. Utilize a biblioteca `AsyncStorage` para armazenar dados localmente:
   ```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';

const armazenarDados = async (chave, valor) => {
  try {
    await AsyncStorage.setItem(chave, valor);
  } catch (error) {
    console.error(error);
  }
};
```

## Validação
Para validar o funcionamento do aplicativo, execute-o em um emulador ou dispositivo físico e verifique se as funcionalidades implementadas estão funcionando corretamente. Isso inclui testar a integração com APIs e o armazenamento de dados locais. Utilize ferramentas de depuração como o React Native Debugger para identificar e solucionar problemas.

## Tratamento de Exceções e Edge Cases
### Tratamento de Erros de Rede
- Verifique se o dispositivo tem conexão com a internet antes de fazer requisições HTTP.
- Implemente retry para requisições que falharam devido a problemas de rede.

### Tratamento de Erros de Parseamento de JSON
- Verifique se a resposta da API é um JSON válido antes de tentar parseá-la.
- Implemente tratamento de erros para casos em que a resposta não é um JSON válido.

### Tratamento de Erros de Armazenamento de Dados Locais
- Verifique se o dispositivo tem espaço suficiente em disco antes de armazenar dados localmente.
- Implemente tratamento de erros para casos em que o armazenamento de dados locais falha.

### Exemplos de Código para Tratamento de Exceções
```javascript
// Tratamento de erros de rede
const fetchComRetry = async (url, options) => {
  const maxRetries = 3;
  let retries = 0;
  while (retries < maxRetries) {
    try {
      const response = await fetch(url, options);
      return response;
    } catch (error) {
      retries++;
      if (retries >= maxRetries) {
        throw error;
      }
    }
  }
};

// Tratamento de erros de parseamento de JSON
const parseJsonComTratamentoDeErros = async (response) => {
  try {
    return await response.json();
  } catch (error) {
    console.error('Erro ao parsear JSON:', error);
    throw error;
  }
};
