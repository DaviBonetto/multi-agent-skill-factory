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
### Tratamento de Erros
- **Erro de Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro deve ser exibida informando que o arquivo não foi encontrado.
- **Erro de Permissão:** Se o usuário não tiver permissão para ler o arquivo "SKILL.md", uma mensagem de erro deve ser exibida informando que não há permissão para acessar o arquivo.
- **Erro de Formatação:** Se o arquivo "SKILL.md" estiver com formatação inválida, uma mensagem de erro deve ser exibida informando que o arquivo está com formatação inválida.

### Edge Cases
- **Habilidades com Nomes Iguais:** Se houver habilidades com nomes iguais, o sistema deve ser capaz de distinguir entre elas com base no caminho do arquivo "SKILL.md".
- **Habilidades com Descrições Vazias:** Se uma habilidade tiver uma descrição vazia, o sistema deve exibir uma mensagem informando que a descrição está vazia.
- **Caminhos Relativos:** Se um caminho relativo for utilizado para referenciar um arquivo dentro de uma pasta de habilidade, o sistema deve ser capaz de resolver o caminho correto com base no diretório atual.