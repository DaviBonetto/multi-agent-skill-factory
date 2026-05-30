# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar a tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erro de Arquivo Não Encontrado:** Caso o arquivo "SKILL.md" não seja encontrado no diretório especificado, uma mensagem de erro será exibida indicando que o arquivo não foi encontrado.
- **Erro de Permissão:** Se o usuário não tiver permissão para acessar o arquivo "SKILL.md", uma mensagem de erro será exibida indicando que o acesso foi negado.
- **Erro de Formatação:** Se o arquivo "SKILL.md" estiver com formatação inválida, uma mensagem de erro será exibida indicando que o arquivo não pode ser processado.

### Edge Cases
- **Habilidades com Nomes Idênticos:** Caso existam habilidades com nomes idênticos em diretórios diferentes, o sistema priorizará a habilidade que foi registrada primeiro.
- **Caminhos Relativos:** Se os caminhos relativos dentro das pastas de habilidades forem malformados, o sistema tentará resolver o caminho correto, mas pode falhar se o caminho for ambíguo.
- **Descrições de Habilidades Vazias:** Se a descrição de uma habilidade estiver vazia, o sistema exibirá uma mensagem indicando que a descrição não está disponível.

### Segurança
- **Validação de Entradas:** Todas as entradas de usuário serão validadas para prevenir ataques de injeção de código ou outros tipos de ataques maliciosos.
- **Controle de Acesso:** O acesso às habilidades será controlado com base nas permissões do usuário, garantindo que apenas usuários autorizados possam acessar e executar as habilidades.
- **Criptografia:** Todas as comunicações entre o sistema e os usuários serão criptografadas para proteger as informações sensíveis.