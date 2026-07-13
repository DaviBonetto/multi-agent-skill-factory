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
### Erros de Leitura de Arquivos
- **Erro de Arquivo Não Encontrado**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida informando que o arquivo não foi encontrado.
- **Erro de Permissão de Leitura**: Se o usuário não tiver permissão para ler o arquivo "SKILL.md", uma mensagem de erro será exibida informando que não há permissão para acessar o arquivo.

### Tratamento de Dados Inválidos
- **Dados de Habilidade Inválidos**: Se os dados de habilidade forem inválidos ou estiverem faltando, uma mensagem de erro será exibida informando que os dados de habilidade são inválidos.
- **Caminho de Arquivo Inválido**: Se o caminho do arquivo for inválido, uma mensagem de erro será exibida informando que o caminho do arquivo é inválido.

### Segurança
- **Validação de Entradas**: Todas as entradas de usuário serão validadas para evitar ataques de injeção de código ou outros tipos de ataques mal-intencionados.
- **Uso de Bibliotecas Seguras**: Somente bibliotecas seguras e atualizadas serão usadas para evitar vulnerabilidades de segurança.