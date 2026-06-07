# SKILL
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
Ao trabalhar com habilidades, é importante considerar os seguintes casos de bordo e exceções:
* **Habilidades não encontradas**: se uma habilidade não for encontrada no diretório especificado, um erro deve ser retornado ao usuário.
* **Arquivos SKILL.md corrompidos**: se o arquivo SKILL.md estiver corrompido ou não puder ser lido, um erro deve ser retornado ao usuário.
* **Caminhos relativos inválidos**: se um caminho relativo dentro de uma pasta de habilidade for inválido, um erro deve ser retornado ao usuário.
* **Descrições de habilidades vazias**: se a descrição de uma habilidade estiver vazia, um aviso deve ser retornado ao usuário.
* **Habilidades duplicadas**: se duas ou mais habilidades tiverem o mesmo nome, um erro deve ser retornado ao usuário.

Para lidar com esses casos, é recomendável implementar um sistema de tratamento de erros robusto que possa lidar com diferentes tipos de exceções e fornecer feedback claro e útil ao usuário. Além disso, é importante garantir que as habilidades sejam testadas rigorosamente para garantir que elas funcionem corretamente em diferentes cenários.