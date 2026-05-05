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
### Tratamento de Erros
- **Erro de Arquivo Não Encontrado:** Caso o arquivo "SKILL.md" não seja encontrado no diretório especificado, uma mensagem de erro será exibida indicando que o arquivo não foi encontrado.
- **Erro de Permissão:** Se o usuário não tiver permissão para acessar o diretório ou o arquivo "SKILL.md", uma mensagem de erro será exibida indicando que não há permissão para acessar o arquivo.
- **Erro de Formatação:** Se o arquivo "SKILL.md" estiver com formatação inválida, uma mensagem de erro será exibida indicando que o arquivo não pode ser processado devido à formatação inválida.

### Edge Cases
- **Habilidades com Nomes Iguais:** Caso haja habilidades com nomes iguais em diretórios diferentes, o sistema deve ser capaz de distinguir entre elas com base no caminho do diretório.
- **Habilidades com Descrições Vazias:** Se uma habilidade tiver uma descrição vazia, o sistema deve exibir uma mensagem indicando que a descrição da habilidade está vazia.
- **Diretórios Vazios:** Se um diretório estiver vazio e não contiver um arquivo "SKILL.md", o sistema deve ignorar esse diretório e não exibir erros.