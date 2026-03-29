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

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Erro de Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida informando o caminho incorreto.
- **Erro de Permissão:** Se o acesso ao arquivo "SKILL.md" for negado devido a permissões insuficientes, uma mensagem de erro será exibida solicitando permissão de leitura.

### Erros de Formatação
- **Formatação Inválida:** Se o arquivo "SKILL.md" contiver formatação inválida, uma mensagem de erro será exibida indicando a linha e o caractere onde o erro ocorreu.

### Edge Cases
- **Habilidades Duplicadas:** Se múltiplas habilidades com o mesmo nome forem encontradas, apenas a primeira ocorrência será considerada e uma advertência será exibida sobre a duplicata.
- **Caminhos Relativos:** Se os caminhos relativos dentro das pastas de habilidades forem malformados ou não puderem ser resolvidos, uma mensagem de erro será exibida solicitando correção do caminho.

### Segurança
- **Validação de Entrada:** Todas as entradas de usuário serão validadas para prevenir injeção de código malicioso ou outros ataques.
- **Autenticação e Autorização:** Acesso às habilidades e arquivos será controlado por meio de autenticação e autorização adequadas para garantir que apenas usuários autorizados possam visualizar ou modificar as habilidades.