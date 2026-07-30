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

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do conjunto de dados `hf-datasets` seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Arquivo não encontrado:** Caso o arquivo "SKILL.md" não seja encontrado no diretório especificado, uma mensagem de erro deve ser exibida informando o caminho incorreto.
- **Permissão de leitura:** Se o arquivo "SKILL.md" não tiver permissão de leitura, uma mensagem de erro deve ser exibida solicitando permissão de leitura.

### Tratamento de Dados
- **Dados inválidos:** Se os dados fornecidos para a habilidade forem inválidos ou inconsistentes, a habilidade deve lidar com esses dados de forma a evitar erros e garantir a estabilidade do sistema.
- **Dados sensíveis:** Se a habilidade lidar com dados sensíveis, como informações de login ou dados pessoais, medidas de segurança adequadas devem ser implementadas para proteger esses dados.

### Segurança
- **Injeção de código:** A habilidade deve ser protegida contra injeção de código malicioso, garantindo que todos os inputs sejam validados e sanitizados.
- **Autenticação e autorização:** A habilidade deve implementar mecanismos de autenticação e autorização adequados para garantir que apenas usuários autorizados possam acessar e utilizar a habilidade.

### Edge Cases
- **Caminhos relativos:** A habilidade deve lidar corretamente com caminhos relativos, garantindo que os arquivos e recursos sejam acessados corretamente independentemente do diretório atual.
- **Caracteres especiais:** A habilidade deve ser capaz de lidar com caracteres especiais em nomes de arquivos e caminhos, garantindo que esses caracteres sejam tratados corretamente e não causem erros.