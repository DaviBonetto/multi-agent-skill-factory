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
- **Erro de Arquivo Não Encontrado:** Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro será exibida, indicando que o arquivo não foi encontrado.
- **Erro de Permissão:** Se o usuário não tiver permissão para ler o arquivo "SKILL.md", uma mensagem de erro será exibida, indicando que o acesso foi negado.
- **Erro de Formatação:** Se o arquivo "SKILL.md" estiver com formatação inválida, uma mensagem de erro será exibida, indicando que o arquivo não pode ser processado.

### Edge Cases
- **Habilidades com Nomes Iguais:** Se duas ou mais habilidades tiverem o mesmo nome, uma mensagem de aviso será exibida, indicando que há habilidades com nomes duplicados.
- **Caminhos Relativos Inválidos:** Se um caminho relativo for inválido, uma mensagem de erro será exibida, indicando que o caminho é inválido.
- **Descrições de Habilidades Vazias:** Se a descrição de uma habilidade estiver vazia, uma mensagem de aviso será exibida, indicando que a descrição da habilidade está vazia.

### Segurança
- **Validação de Entradas:** Todas as entradas de usuário serão validadas para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- **Controle de Acesso:** O acesso às habilidades será controlado para garantir que apenas usuários autorizados possam visualizar e executar as habilidades.
- **Criptografia:** As informações sensíveis, como senhas e chaves de API, serão criptografadas para proteger contra acessos não autorizados.