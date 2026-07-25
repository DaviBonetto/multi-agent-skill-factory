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
No processo de utilização dessas habilidades, é fundamental considerar os seguintes casos de bordo e exceções:
- **Arquivos Não Encontrados**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro clara deve ser exibida, indicando o caminho incorreto ou a falta do arquivo.
- **Descrições de Habilidades Vazias**: Se a descrição de uma habilidade estiver vazia, deve-se exibir uma mensagem padrão indicando que a descrição não está disponível ou que a habilidade não foi documentada corretamente.
- **Caminhos Relativos Incorretos**: Se os caminhos relativos dentro das pastas de habilidades forem incorretos, o sistema deve ser capaz de lidar com esses erros, seja exibindo uma mensagem de erro ou tentando resolver o caminho correto automaticamente.
- **Permissões de Acesso**: O sistema deve verificar as permissões de acesso aos arquivos e pastas, garantindo que apenas usuários autorizados possam visualizar ou modificar as habilidades documentadas.
- **Tratamento de Erros de Formatação**: Em caso de erros de formatação no arquivo "SKILL.md" ou em qualquer outro arquivo referenciado, o sistema deve ser capaz de identificar e relatar esses erros de forma clara, sem comprometer a estabilidade do sistema.