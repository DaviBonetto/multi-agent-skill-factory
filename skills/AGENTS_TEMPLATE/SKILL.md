# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** É OBRIGATÓRIO ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

**Observação:** Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Leitura do Arquivo SKILL.md
- **Erro de Arquivo Não Encontrado:** Se o arquivo SKILL.md não for encontrado no diretório especificado, uma mensagem de erro será exibida informando o caminho incorreto.
- **Erro de Permissão de Leitura:** Se houver uma falha de permissão para ler o arquivo SKILL.md, uma mensagem de erro será exibida solicitando permissão de leitura.

### Tratamento de Habilidades Não Documentadas
- **Habilidades Não Listadas:** Se uma habilidade não estiver listada na seção de habilidades disponíveis, mas tiver um arquivo SKILL.md correspondente, uma mensagem de aviso será exibida sugerindo a adição da habilidade à lista.

### Segurança
- **Validação de Entradas:** Todas as entradas de usuário devem ser validadas para evitar injeção de código malicioso ou outros ataques de segurança.
- **Uso de Bibliotecas Seguras:** As bibliotecas utilizadas devem ser mantidas atualizadas e seguras para evitar vulnerabilidades conhecidas.

### Edge Cases
- **Nomes de Habilidades Duplicados:** Se dois ou mais diretórios tiverem o mesmo nome de habilidade, uma mensagem de erro será exibida solicitando a renomeação de uma das habilidades para evitar conflitos.
- **Caminhos Relativos Inválidos:** Se um caminho relativo dentro de uma pasta de habilidade for inválido, uma mensagem de erro será exibida indicando o caminho incorreto.