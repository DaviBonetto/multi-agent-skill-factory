# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**IMPORTANTE**: Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
Ao trabalhar com habilidades, é fundamental considerar os casos de bordo e exceções para garantir a robustez e a segurança do sistema. Aqui estão alguns exemplos de tratamento de exceções e edge cases que devem ser considerados:
* **Habilidades não encontradas**: Se uma habilidade não for encontrada, o sistema deve retornar uma mensagem de erro clara e útil, em vez de falhar silenciosamente.
* **Caminhos relativos**: Ao trabalhar com caminhos relativos, é importante garantir que o sistema possa lidar com caminhos malformados ou inexistentes.
* **Erros de permissão**: O sistema deve lidar com erros de permissão ao acessar arquivos ou pastas, garantindo que o usuário seja notificado e que o sistema não fique travado.
* **Habilidades duplicadas**: Se uma habilidade for duplicada, o sistema deve detectar e lidar com a duplicação, evitando comportamentos inesperados.
* **Parâmetros inválidos**: O sistema deve validar os parâmetros de entrada para as habilidades, garantindo que sejam válidos e coerentes antes de executar a habilidade.

Ao considerar esses casos de bordo e exceções, podemos garantir que o sistema seja mais robusto, seguro e confiável.