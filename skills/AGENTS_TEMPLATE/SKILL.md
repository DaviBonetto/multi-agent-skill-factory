# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Arquivo não encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida indicando que o arquivo não foi localizado.
- **Permissão de leitura:** Se o arquivo "SKILL.md" não tiver permissão de leitura, uma mensagem de erro será exibida indicando que não é possível ler o arquivo.

### Erros de Formatação
- **Formatação inválida:** Se o arquivo "SKILL.md" tiver formatação inválida, uma mensagem de erro será exibida indicando que o arquivo não pode ser processado devido à formatação inválida.

### Edge Cases
- **Nenhum arquivo "SKILL.md" encontrado:** Se nenhum arquivo "SKILL.md" for encontrado nos diretórios especificados, uma mensagem será exibida indicando que não há habilidades disponíveis.
- **Descrição de habilidade vazia:** Se a descrição de uma habilidade estiver vazia, uma mensagem será exibida indicando que a descrição da habilidade não está disponível.

### Segurança
- **Validação de entrada:** Todas as entradas de usuário serão validadas para evitar ataques de injeção de código malicioso.
- **Uso de bibliotecas seguras:** Somente bibliotecas seguras e atualizadas serão usadas para processar os arquivos "SKILL.md" e evitar vulnerabilidades de segurança.