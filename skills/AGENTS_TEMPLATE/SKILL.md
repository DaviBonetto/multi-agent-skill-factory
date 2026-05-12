# SKILLs
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
### Erros de Arquivo
- **Arquivo "SKILL.md" não encontrado**: Verifique se o arquivo "SKILL.md" existe no diretório especificado e se o caminho está correto.
- **Conteúdo do arquivo "SKILL.md" inválido**: Certifique-se de que o arquivo "SKILL.md" contenha informações válidas e esteja formatado corretamente.

### Erros de Caminho
- **Caminho relativo inválido**: Verifique se os caminhos relativos dentro das pastas de habilidades estão corretos e se os arquivos ou diretórios referenciados existem.
- **Caminho absoluto inválido**: Certifique-se de que os caminhos absolutos sejam válidos e os arquivos ou diretórios referenciados existam.

### Segurança
- **Acesso não autorizado**: Certifique-se de que as permissões de acesso sejam configuradas corretamente para os arquivos e diretórios de habilidades, evitando acessos não autorizados.
- **Injeção de código**: Tenha cuidado com a injeção de código malicioso nos arquivos de habilidades, especialmente quando executando scripts ou comandos.

### Outros Edge Cases
- **Nomes de habilidades duplicados**: Trate nomes de habilidades duplicados para evitar confusões e garantir que as habilidades sejam acessadas corretamente.
- **Descrições de habilidades vazias**: Verifique se as descrições das habilidades não estão vazias e forneçam informações úteis sobre a habilidade.