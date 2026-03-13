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

### Erros de Formatação
- **Formatação inválida:** Se a formatação do arquivo "SKILL.md" for inválida, uma mensagem de erro será exibida indicando que a formatação do arquivo não é válida.
- **Campos obrigatórios:** Se os campos obrigatórios (como `name` e `description`) não forem preenchidos, uma mensagem de erro será exibida indicando quais campos são necessários.

### Segurança
- **Injeção de código:** Para evitar injeção de código, todos os inputs de usuário serão sanitizados e validados antes de serem processados.
- **Dados sensíveis:** Todos os dados sensíveis serão criptografados e armazenados de forma segura para proteger a privacidade dos usuários.

### Edge Cases
- **Nenhum skill encontrado:** Se nenhum skill for encontrado, uma mensagem será exibida indicando que não há habilidades disponíveis.
- **Múltiplos skills com o mesmo nome:** Se múltiplos skills tiverem o mesmo nome, uma mensagem de aviso será exibida indicando que há habilidades duplicadas e solicitando que o usuário especifique qual habilidade deseja usar.