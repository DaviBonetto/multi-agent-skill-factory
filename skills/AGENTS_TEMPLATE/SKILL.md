# SKILL
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro deve ser exibida para o usuário.
- Se a descrição da habilidade não corresponder à intenção do usuário, uma mensagem de aviso deve ser exibida.

### Tratamento de Erros
- Todos os erros devem ser tratados e registrados para fins de depuração e melhoria da habilidade.
- Em caso de erro, o sistema deve fornecer uma resposta significativa ao usuário, indicando o problema e as possíveis soluções.

### Segurança
- Todos os dados utilizados pelas habilidades devem ser validados e sanitizados para prevenir ataques de injeção de código ou cross-site scripting (XSS).
- As habilidades devem ser projetadas para lidar com grandes volumes de dados e evitar sobrecargas no sistema.

### Exceções Conhecidas
- Se o diretório da habilidade não for encontrado, uma exceção `DirectoryNotFoundError` deve ser lançada.
- Se o arquivo "SKILL.md" for inválido ou corrompido, uma exceção `FileInvalidError` deve ser lançada.

## Melhorias Futuras
- Implementar um sistema de cache para armazenar as habilidades mais utilizadas e reduzir o tempo de resposta.
- Desenvolver um mecanismo de feedback para que os usuários possam avaliar e sugerir melhorias para as habilidades.