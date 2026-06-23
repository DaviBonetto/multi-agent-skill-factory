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
Ao trabalhar com as habilidades documentadas, é importante considerar os seguintes casos de bordo e exceções:
- **Arquivos SKILL.md ausentes:** Se um diretório não contém um arquivo SKILL.md, a habilidade não deve ser listada.
- **Caminhos relativos inválidos:** Se um caminho relativo dentro de uma pasta de habilidade for inválido, um erro deve ser lançado e o caminho deve ser tratado como inválido.
- **Descrições de habilidades vazias:** Se a descrição de uma habilidade estiver vazia, a habilidade não deve ser exibida na lista de habilidades disponíveis.
- **Intenção do usuário não correspondente:** Se a descrição da habilidade não corresponder à intenção do usuário, a habilidade não deve ser sugerida como uma opção para realizar a tarefa.
- **Erros de leitura de arquivos:** Se ocorrer um erro ao ler o arquivo SKILL.md, um erro deve ser lançado e o processo deve ser interrompido.
- **Habilidades duplicadas:** Se uma habilidade for listada mais de uma vez, apenas uma instância deve ser exibida na lista de habilidades disponíveis.