# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Leitura de Arquivo
- **Erro de Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida indicando que o arquivo não foi encontrado.
- **Erro de Permissão de Leitura:** Se o arquivo "SKILL.md" não puder ser lido devido a permissões insuficientes, uma mensagem de erro será exibida indicando que não há permissão para ler o arquivo.

### Tratamento de Caminhos Relativos
- **Caminho Relativo Inválido:** Se um caminho relativo for inválido ou não puder ser resolvido, uma mensagem de erro será exibida indicando que o caminho é inválido.

### Segurança
- **Injeção de Comando:** Para evitar injeção de comandos, todos os caminhos e nomes de arquivos são validados e sanitizados antes de serem usados.
- **Validação de Entrada:** Todas as entradas de usuário são validadas para garantir que atendam aos requisitos de segurança e não contenham código malicioso.

### Edge Cases
- **Habilidades Duplicadas:** Se múltiplas habilidades com o mesmo nome forem encontradas, apenas a primeira ocorrência será considerada.
- **Descrições de Habilidades Vazias:** Se uma habilidade tiver uma descrição vazia, ela será exibida como "Descrição não disponível".