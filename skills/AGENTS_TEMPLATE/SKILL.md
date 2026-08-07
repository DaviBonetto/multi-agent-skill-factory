# Introdução às Skills
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
No desenvolvimento e utilização dessas habilidades, é crucial considerar os seguintes casos de bordo e exceções:
- **Arquivos Ausentes:** Caso o arquivo "SKILL.md" não seja encontrado no diretório esperado, o sistema deve lançar uma exceção clara indicando o caminho incorreto ou a ausência do arquivo.
- **Descrições Vazias:** Se a descrição de uma habilidade estiver vazia, o sistema deve exibir uma mensagem indicando que a descrição não está disponível ou conter um valor padrão que ajude o usuário a entender a finalidade da habilidade.
- **Caminhos Relativos:** Ao lidar com caminhos relativos dentro das pastas de habilidades, o sistema deve garantir que os caminhos sejam resolvidos corretamente para evitar erros de referência.
- **Erros de Parsing:** Em caso de erros durante o parsing do arquivo "SKILL.md" ou das descrições das habilidades, o sistema deve capturar a exceção e exibir uma mensagem de erro amigável ao usuário, indicando a natureza do problema.
- **Segurança:** Todas as entradas de usuário e dados provenientes de fontes externas devem ser validados e sanitizados para prevenir ataques de injeção ou cross-site scripting (XSS), garantindo a segurança do sistema e dos dados dos usuários.

Essas considerações são essenciais para garantir a robustez, a segurança e a usabilidade das habilidades documentadas.