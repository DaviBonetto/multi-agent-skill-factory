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
### Tratamento de Erros
- **Erro de Arquivo Não Encontrado**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida informando que o arquivo não foi encontrado.
- **Erro de Permissão**: Se o usuário não tiver permissão para ler o arquivo "SKILL.md", uma mensagem de erro será exibida informando que não há permissão para acessar o arquivo.
- **Erro de Formato Inválido**: Se o arquivo "SKILL.md" estiver no formato inválido, uma mensagem de erro será exibida informando que o formato do arquivo é inválido.

### Edge Cases
- **Habilidades com Nomes Duplicados**: Se houver habilidades com nomes duplicados, apenas a primeira habilidade será exibida.
- **Caminhos Relativos Inválidos**: Se os caminhos relativos dentro das pastas de habilidades forem inválidos, uma mensagem de erro será exibida informando que o caminho é inválido.
- **Descrições de Habilidades Vazias**: Se as descrições das habilidades estiverem vazias, elas não serão exibidas.

## Segurança
- **Validação de Entradas**: Todas as entradas de usuário serão validadas para evitar ataques de injeção de código.
- **Proteção contra Acesso Não Autorizado**: Acesso às habilidades será restrito apenas a usuários autorizados.
- **Criptografia de Dados**: Todos os dados sensíveis serão criptografados para garantir a segurança.