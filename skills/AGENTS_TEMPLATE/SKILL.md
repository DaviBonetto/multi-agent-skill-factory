# Introdução às Skills
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
No desenvolvimento e utilização dessas habilidades, é crucial considerar os seguintes casos de bordo e exceções:
- **Arquivos Não Encontrados:** Caso o arquivo "SKILL.md" não seja encontrado no diretório especificado, uma mensagem de erro clara deve ser exibida, indicando o caminho incorreto ou a falta do arquivo.
- **Descrições de Habilidades Vazias:** Se a descrição de uma habilidade estiver vazia, deve-se exibir uma mensagem padrão indicando que a descrição não está disponível ou que o campo está vazio.
- **Caminhos Relativos Incorretos:** Se os caminhos relativos dentro das pastas de habilidades forem incorretos, o sistema deve ser capaz de lidar com esses erros, seja exibindo uma mensagem de erro ou tentando resolver o caminho correto.
- **Erros de Permissão:** Em caso de erros de permissão ao acessar arquivos ou pastas, o sistema deve informar ao usuário sobre o problema de permissão e, se possível, oferecer soluções ou alternativas.
- **Tratamento de Erros Gerais:** Para qualquer erro não previsto, o sistema deve ter um mecanismo de tratamento de exceções genérico que forneça informações úteis para o usuário e/ou para os desenvolvedores, ajudando na identificação e resolução do problema.

Essas considerações são essenciais para garantir a robustez, segurança e usabilidade das habilidades documentadas.