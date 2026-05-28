# SKILLs Documentadas
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou puder ajudar a realizar sua tarefa.

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
- **Dados de habilidade inválidos:** Se os dados de habilidade forem inválidos ou inconsistentes, uma mensagem de erro será exibida indicando que os dados são inválidos e não podem ser processados.

### Segurança
- **Injeção de código:** Para evitar injeção de código, todos os dados de entrada serão sanitizados e validados antes de serem processados.
- **Acesso não autorizado:** Somente usuários autorizados terão acesso às habilidades e aos arquivos relacionados. O acesso será controlado por meio de autenticação e autorização adequadas.

### Edge Cases
- **Habilidades duplicadas:** Se houver habilidades duplicadas, apenas a primeira ocorrência será considerada e as demais serão ignoradas.
- **Caminhos relativos:** Se os caminhos relativos forem malformados ou não puderem ser resolvidos, uma mensagem de erro será exibida indicando que o caminho é inválido.