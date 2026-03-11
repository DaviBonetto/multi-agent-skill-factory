# SKILL
## Introdução
A skill de parse de media types é responsável por analisar e processar os tipos de mídia em requisições HTTP.

## Histórico de Versões
### 0.3.0 / 2014-09-07
* Support Node.js 0.6
* Throw error when parameter format invalid on parse

### 0.2.0 / 2014-06-18
* Add `typer.format()` to format media types

### 0.1.0 / 2014-06-17
* Accept `req` as argument to `parse`
* Accept `res` as argument to `parse`
* Parse media type with extra LWS between type and first parameter

### 0.0.0 / 2014-06-13
* Initial implementation

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
* Verificar se o parâmetro de entrada é válido antes de realizar o parse.
* Lançar um erro personalizado com mensagem clara e concisa quando o parâmetro de entrada for inválido.
* Utilizar try-catch para capturar e tratar exceções durante o processo de parse.

### Edge Cases
* Lidar com casos de entrada vazia ou nula.
* Considerar a possibilidade de entrada com caracteres especiais ou não ASCII.
* Testar a skill com diferentes tipos de mídia e parâmetros para garantir a robustez e flexibilidade.

### Segurança
* Validar a entrada para evitar ataques de injeção de código ou cross-site scripting (XSS).
* Utilizar bibliotecas e frameworks de segurança para proteger a aplicação contra vulnerabilidades conhecidas.
* Realizar testes de segurança regulares para garantir a integridade da skill.

## Exemplos de Implementação
* Exemplo de uso da skill em uma aplicação web:
```javascript
const mediaTypeParser = require('media-type-parser');
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  const mediaType = mediaTypeParser.parse(req.headers['content-type']);
  res.send(`Media Type: ${mediaType}`);
});
```

## Testes
* Testes unitários para a skill:
```javascript
const mediaTypeParser = require('media-type-parser');
const assert = require('assert');

describe('Media Type Parser', () => {
  it('should parse media type correctly', () => {
    const mediaType = mediaTypeParser.parse('application/json; charset=utf-8');
    assert.equal(mediaType, 'application/json');
  });
});

## Uso
A skill pode ser utilizada em aplicações web para analisar e processar os tipos de mídia em requisições HTTP. Ela fornece métodos para parsear e formatar os tipos de mídia, além de tratar exceções e edge cases.