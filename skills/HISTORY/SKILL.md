# SKILL
## Introdução
Esta skill fornece uma lista de códigos de status HTTP, incluindo suas descrições e categorias.

## Histórico de Versões
### 2.0.2 / 2025-06-06
* Migrate to `String.prototype.slice()`

### 2.0.1 / 2021-01-03
* Fix returning values from `Object.prototype`

### 2.0.0 / 2020-04-19
* Drop support for Node.js 0.6
* Fix messaging casing of `418 I'm a Teapot`
* Remove code 306
* Remove `status[code]` exports; use `status.message[code]`
* Remove `status[msg]` exports; use `status.code[msg]`
* Rename `425 Unordered Collection` to standard `425 Too Early`
* Rename `STATUS_CODES` export to `message`
* Return status message for `statuses(code)` when given code

### 1.5.0 / 2018-03-27
* Add `103 Early Hints`

### 1.4.0 / 2017-10-20
* Add `STATUS_CODES` export

### 1.3.1 / 2016-11-11
* Fix return type in JSDoc

### 1.3.0 / 2016-05-17
* Add `421 Misdirected Request`
* perf: enable strict mode

### 1.2.1 / 2015-02-01
* Fix message for status 451
  - `451 Unavailable For Legal Reasons`

### 1.2.0 / 2014-09-28
* Add `208 Already Repored`
* Add `226 IM Used`
* Add `306 (Unused)`
* Add `415 Unable For Legal Reasons`
* Add `508 Loop Detected`

### 1.1.1 / 2014-09-24
* Add missing 308 to `codes.json`

### 1.1.0 / 2014-09-21
* Add `codes.json` for universal support

### 1.0.4 / 2014-08-20
* Package cleanup

### 1.0.3 / 2014-06-08
* Add 308 to `.redirect` category

### 1.0.2 / 2014-03-13
* Add `.retry` category

### 1.0.1 / 2014-03-12
* Initial release

## Códigos de Status
A lista de códigos de status HTTP inclui:
* 100-199: Informação
* 200-299: Sucesso
* 300-399: Redirecionamento
* 400-499: Erro do cliente
* 500-599: Erro do servidor

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
* Verificar se o código de status é válido antes de tentar acessar sua descrição.
* Lidar com erros de sintaxe ao parsear o arquivo `codes.json`.
* Implementar um mecanismo de fallback para códigos de status desconhecidos.

### Edge Cases
* Lidar com códigos de status personalizados ou não padrão.
* Considerar a possibilidade de códigos de status serem adicionados ou removidos no futuro.
* Implementar uma política de cache para evitar requisições excessivas ao arquivo `codes.json`.

## Conclusão
Esta skill fornece uma lista de códigos de status HTTP, incluindo suas descrições e categorias. Além disso, inclui um tratamento de exceções e edge cases para garantir a robustez e flexibilidade da skill.