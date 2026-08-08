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
### Erros de Leitura de Arquivo
- **Erro de Permissão:** Caso o arquivo "SKILL.md" não possa ser lido devido a permissões insuficientes, uma mensagem de erro deve ser exibida indicando a falta de permissão para acessar o arquivo.
- **Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no caminho especificado, uma mensagem deve informar que o arquivo não foi localizado e sugerir verificar o caminho fornecido.

### Tratamento de Caminhos Relativos
- **Caminhos Inválidos:** Se um caminho relativo dentro de uma pasta de habilidade for inválido (por exemplo, referenciar um diretório que não existe), o sistema deve detectar e relatar o erro, fornecendo detalhes sobre o caminho inválido.

### Segurança
- **Injeção de Código:** Para prevenir injeção de código malicioso através dos arquivos "SKILL.md", todos os dados provenientes desses arquivos devem ser sanitizados e validados antes de serem processados ou exibidos.
- **Validação de Entrada:** Todas as entradas de usuário que afetem a leitura ou processamento dos arquivos "SKILL.md" devem ser validadas para garantir que atendam a expectativas de segurança e não causem comportamentos inesperados no sistema.