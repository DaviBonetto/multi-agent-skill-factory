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
No tratamento de habilidades, é fundamental considerar casos de exceção e edge cases para garantir a robustez e a segurança do sistema. Aqui estão alguns pontos a serem considerados:
* **Erros de Leitura de Arquivos**: Em caso de falha na leitura do arquivo SKILL.md, o sistema deve ser capaz de lidar com o erro de forma adequada, seja exibindo uma mensagem de erro ao usuário ou registrando o erro para análise posterior.
* **Habilidades Não Encontradas**: Se uma habilidade solicitada não for encontrada, o sistema deve retornar uma resposta clara indicando que a habilidade não está disponível, em vez de simplesmente falhar ou retornar uma resposta vaga.
* **Caminhos Relativos**: Ao lidar com caminhos relativos dentro das pastas de habilidades, é crucial garantir que o sistema possa resolver esses caminhos corretamente, independentemente do local onde a habilidade é executada.
* **Segurança**: Todas as entradas de usuário e dados provenientes de fontes externas devem ser validados e sanitizados para prevenir ataques de injeção de código ou outros tipos de vulnerabilidades de segurança.
* **Limites de Recursos**: O sistema deve ser capaz de lidar com limites de recursos, como memória ou tempo de execução, para evitar que uma habilidade consuma todos os recursos disponíveis e cause problemas de desempenho ou falhas no sistema.