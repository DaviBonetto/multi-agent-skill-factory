# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante**: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Arquivo não encontrado**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida indicando o caminho incorreto.
- **Permissão de leitura**: Se o arquivo "SKILL.md" não tiver permissão de leitura, uma mensagem de erro será exibida solicitando permissão de leitura.

### Erros de Formatação
- **Formatação inválida**: Se a formatação do arquivo "SKILL.md" for inválida, uma mensagem de erro será exibida indicando a linha e a coluna onde o erro ocorreu.

### Edge Cases
- **Nenhum arquivo "SKILL.md" encontrado**: Se nenhum arquivo "SKILL.md" for encontrado nos diretórios, uma mensagem será exibida indicando que não há habilidades disponíveis.
- **Múltiplos arquivos "SKILL.md"**: Se múltiplos arquivos "SKILL.md" forem encontrados no mesmo diretório, uma mensagem de aviso será exibida indicando que apenas um arquivo por diretório é permitido.

### Segurança
- **Injeção de código**: Para evitar injeção de código, todos os inputs de usuário serão sanitizados e validados antes de serem processados.
- **Validação de dados**: Todos os dados serão validados antes de serem processados para evitar erros de execução.