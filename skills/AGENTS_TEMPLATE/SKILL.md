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
Para garantir a robustez e a segurança das habilidades, é fundamental considerar os casos de bordo e exceções. Aqui estão algumas diretrizes para lidar com essas situações:
* **Erros de Arquivo**: Se o arquivo "SKILL.md" não for encontrado, uma mensagem de erro clara deve ser exibida, indicando a falta do arquivo e como corrigir a situação.
* **Caminhos Inválidos**: Se os caminhos referenciados dentro das pastas de habilidades forem inválidos, uma exceção deve ser lançada, fornecendo detalhes sobre o caminho inválido e como corrigir o problema.
* **Descrições de Habilidades Vazias**: Se a descrição de uma habilidade estiver vazia, uma mensagem de aviso deve ser exibida, solicitando que o usuário forneça uma descrição válida.
* **Intenção do Usuário**: Se a intenção do usuário não corresponder a nenhuma habilidade documentada, uma mensagem de ajuda deve ser exibida, oferecendo sugestões de habilidades relacionadas ou uma opção para criar uma nova habilidade.
* **Segurança**: Todas as habilidades devem ser validadas para garantir que não contenham código malicioso ou vulnerabilidades de segurança. Isso pode ser feito por meio de análise de código estático e dinâmico, além de testes de segurança regulares.