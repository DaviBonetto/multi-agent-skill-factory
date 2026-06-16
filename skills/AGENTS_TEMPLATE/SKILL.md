# SKILL
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erro de Arquivo Não Encontrado**: Se o arquivo "SKILL.md" não for encontrado no diretório especificado, uma mensagem de erro deve ser exibida informando ao usuário sobre o problema e fornecendo orientações sobre como resolver.
- **Erro de Permissão**: Se o usuário não tiver permissão para acessar o arquivo "SKILL.md" ou o diretório, uma mensagem de erro deve ser exibida explicando a situação e sugerindo como obter as permissões necessárias.
- **Erro de Formatação**: Se o arquivo "SKILL.md" estiver mal formatado ou não seguir as convenções esperadas, uma mensagem de erro deve ser exibida ao usuário, indicando o problema e como corrigi-lo.

### Edge Cases
- **Habilidades com Nomes Duplicados**: Se houver habilidades com nomes idênticos, o sistema deve ser capaz de lidar com essa situação, possivelmente solicitando ao usuário que especifique qual habilidade deseja acessar ou implementando uma lógica para resolver automaticamente a ambiguidade.
- **Caminhos Relativos**: O sistema deve ser capaz de lidar corretamente com caminhos relativos dentro das pastas de habilidades, garantindo que os recursos sejam acessados corretamente independentemente do local de onde a habilidade é acessada.
- **Segurança**: Todas as habilidades e arquivos acessados devem ser verificados para garantir que não contenham código malicioso ou vulnerabilidades de segurança, protegendo assim o sistema e os usuários.