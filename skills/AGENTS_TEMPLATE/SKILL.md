# Introdução às Habilidades Adicionais
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
- **Erro de Arquivo Não Encontrado:** Caso o arquivo SKILL.md não seja encontrado no diretório especificado, uma mensagem de erro será exibida informando o caminho incorreto.
- **Erro de Formatação:** Se o arquivo SKILL.md estiver com formatação inválida, uma mensagem de erro será exibida solicitando a correção da formatação.
- **Erro de Permissão:** Se o usuário não tiver permissão para acessar o arquivo SKILL.md, uma mensagem de erro será exibida informando a falta de permissão.

### Edge Cases
- **Habilidades Duplicadas:** Caso haja habilidades duplicadas, apenas a primeira ocorrência será considerada.
- **Caminhos Relativos:** Os caminhos relativos devem ser usados com cautela para evitar erros de referência.
- **Descrições Vazias:** Se a descrição de uma habilidade estiver vazia, uma mensagem padrão será exibida em seu lugar.

## Segurança
- **Validação de Entrada:** Todas as entradas de usuário devem ser validadas para evitar ataques de injeção de código.
- **Uso de Bibliotecas Seguras:** Somente bibliotecas seguras e atualizadas devem ser usadas para evitar vulnerabilidades.
- **Controle de Acesso:** O acesso às habilidades deve ser controlado para garantir que apenas usuários autorizados possam visualizar e executar as habilidades.