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
- **Arquivo não encontrado:** Caso o arquivo "SKILL.md" não seja encontrado no diretório especificado, uma mensagem de erro será exibida indicando o caminho incorreto.
- **Permissão de leitura:** Se o arquivo "SKILL.md" não tiver permissão de leitura, uma exceção de permissão será lançada.

### Tratamento de Dados
- **Dados inválidos:** Se os dados fornecidos para a habilidade forem inválidos ou inconsistentes, a habilidade deve lidar com esses dados de forma a evitar erros ou comportamentos inesperados.
- **Dados sensíveis:** Se a habilidade lidar com dados sensíveis, medidas de segurança devem ser implementadas para proteger esses dados, como criptografia ou anonimização.

### Segurança
- **Injeção de código:** A habilidade deve ser projetada para evitar injeção de código malicioso, validando e sanitizando todas as entradas de usuário.
- **Autenticação e autorização:** Se a habilidade requer autenticação ou autorização, esses mecanismos devem ser implementados de forma segura, utilizando protocolos padrão e boas práticas de segurança.

### Edge Cases
- **Entradas extremas:** A habilidade deve ser testada com entradas extremas, como valores muito grandes ou muito pequenos, para garantir que ela lide corretamente com esses casos.
- **Cenários de bordo:** A habilidade deve ser projetada para lidar com cenários de bordo, como falta de recursos ou condições de rede adversas, de forma a minimizar o impacto sobre o usuário.