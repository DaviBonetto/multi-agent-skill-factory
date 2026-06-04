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
- **Erro de Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida informando que o arquivo não foi encontrado.
- **Erro de Permissão:** Se o usuário não tiver permissão para acessar o diretório ou o arquivo "SKILL.md", uma mensagem de erro será exibida informando que o acesso foi negado.
- **Erro de Formatação:** Se o arquivo "SKILL.md" estiver com formatação inválida, uma mensagem de erro será exibida informando que o arquivo está com formatação inválida.

### Edge Cases
- **Habilidades Duplicadas:** Se houver habilidades duplicadas, apenas a primeira ocorrência será exibida.
- **Caminhos Relativos:** Se os caminhos relativos forem utilizados, eles serão resolvidos com base no diretório atual.
- **Descrições Vazias:** Se as descrições das habilidades estiverem vazias, elas serão exibidas como "Descrição não disponível".

### Segurança
- **Validação de Entradas:** Todas as entradas de usuário serão validadas para evitar ataques de injeção de código.
- **Uso de Bibliotecas Seguras:** Somente bibliotecas seguras e atualizadas serão utilizadas para evitar vulnerabilidades de segurança.
- **Proteção de Dados:** Todos os dados serão protegidos com criptografia e armazenados de forma segura para evitar acessos não autorizados.