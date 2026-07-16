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
O tratamento de exceções e edge cases é crucial para garantir a robustez e a segurança das habilidades. Aqui estão alguns casos a considerar:
* **Habilidades não encontradas**: se uma habilidade não for encontrada, uma mensagem de erro clara deve ser exibida para o usuário.
* **Descrições de habilidades vazias**: se a descrição de uma habilidade estiver vazia, uma mensagem de erro deve ser exibida para o usuário.
* **Caminhos relativos inválidos**: se um caminho relativo for inválido, uma mensagem de erro deve ser exibida para o usuário.
* **Erros de permissão**: se ocorrer um erro de permissão ao acessar um arquivo ou diretório, uma mensagem de erro deve ser exibida para o usuário.
* **Edge cases de habilidades**: habilidades com nomes ou descrições muito longas ou com caracteres especiais devem ser tratadas corretamente para evitar erros.

Para lidar com esses casos, é recomendado implementar um sistema de tratamento de exceções robusto, que inclua:
* Verificação de entrada de usuário
* Validação de habilidades e descrições
* Tratamento de erros de permissão e caminhos inválidos
* Uso de try-catch para capturar e tratar exceções

Isso ajudará a garantir que as habilidades sejam executadas corretamente e que os erros sejam tratados de forma eficaz.