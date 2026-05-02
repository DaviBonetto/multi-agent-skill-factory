# SKILLs Documentados
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
Para garantir a robustez e a segurança das habilidades, é fundamental considerar os seguintes casos:
* **Erro de Arquivo Não Encontrado**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro clara deve ser exibida, indicando o caminho incorreto ou a falta do arquivo.
* **Descrição de Habilidade Vazia**: Se a descrição de uma habilidade estiver vazia, uma mensagem deve ser exibida, solicitando que o usuário forneça uma descrição válida.
* **Caminho Relativo Inválido**: Se um caminho relativo dentro de uma pasta de habilidade for inválido, uma exceção deve ser lançada, indicando o erro e solicitando a correção do caminho.
* **Acesso Não Autorizado**: Se um usuário tentar acessar uma habilidade sem as permissões necessárias, uma mensagem de erro de acesso negado deve ser exibida, explicando as razões e as etapas necessárias para obter as permissões adequadas.
* **Erros de Parseamento**: Em caso de erros durante o parseamento do arquivo "SKILL.md" ou de outros arquivos relacionados, mensagens de erro claras e específicas devem ser exibidas, ajudando o usuário a identificar e corrigir o problema.

Ao considerar esses casos e implementar o tratamento de exceções e edge cases apropriado, as habilidades podem ser tornadas mais robustas, seguras e fáceis de usar.