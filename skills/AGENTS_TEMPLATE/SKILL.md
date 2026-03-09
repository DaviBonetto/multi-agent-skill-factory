# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**IMPORTANTE**: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
No tratamento de habilidades, é fundamental considerar casos de bordo e exceções para garantir a robustez e a segurança do sistema. Aqui estão alguns pontos a serem considerados:
* **Habilidades não documentadas**: Em caso de habilidades não documentadas, o sistema deve ser capaz de lidar com a situação de forma elegante, informando ao usuário sobre a falta de documentação e, se possível, oferecendo alternativas ou orientações sobre como proceder.
* **Caminhos relativos**: Quando se lida com caminhos relativos dentro das pastas de habilidades, é crucial garantir que o sistema possa resolver esses caminhos corretamente, independentemente do local de onde a habilidade é acessada.
* **Erros de leitura ou parsing**: O sistema deve ser capaz de lidar com erros que ocorrem durante a leitura ou parsing dos arquivos de habilidade, fornecendo mensagens de erro claras e úteis para o usuário.
* **Segurança**: É fundamental garantir que o sistema esteja protegido contra possíveis vulnerabilidades de segurança, como injeção de código malicioso através dos arquivos de habilidade. Isso pode ser alcançado através da validação rigorosa dos dados de entrada e da implementação de medidas de segurança adequadas.
* **Manuseio de exceções**: O sistema deve ter um mecanismo robusto para lidar com exceções, garantindo que, em caso de erros, o sistema não entre em um estado inconsistente e que o usuário seja informado de forma clara sobre o que ocorreu e como proceder.