# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Arquivo não encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida indicando que o arquivo não foi localizado.
- **Permissão de leitura:** Se o arquivo "SKILL.md" não tiver permissão de leitura, uma mensagem de erro será exibida indicando que não é possível ler o arquivo devido a permissões insuficientes.

### Tratamento de Dados Inválidos
- **Descrição de habilidade vazia:** Se a descrição de uma habilidade estiver vazia, ela não será exibida na lista de habilidades disponíveis.
- **Caminho inválido:** Se o caminho para uma habilidade for inválido, uma mensagem de erro será exibida indicando que o caminho é inválido.

### Segurança
- **Injeção de código:** Para prevenir injeção de código, todos os dados de entrada são validados e sanitizados antes de serem processados.
- **Dados sensíveis:** Nenhum dado sensível é armazenado ou processado pelas habilidades. Se uma habilidade requer dados sensíveis, ela deve ser projetada para lidar com esses dados de forma segura.