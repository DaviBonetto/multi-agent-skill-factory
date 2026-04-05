# SKILL
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou puder ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
Para garantir a robustez e a segurança das habilidades, é fundamental considerar os casos de bordo e exceções. Aqui estão algumas diretrizes para lidar com esses cenários:
* **Erros de Arquivo**: Em caso de erro ao acessar ou ler arquivos, como o arquivo "SKILL.md", é importante fornecer uma mensagem de erro clara e útil para o usuário, indicando a causa do problema e possíveis soluções.
* **Caminhos Relativos**: Ao trabalhar com caminhos relativos dentro das pastas de habilidades, é crucial garantir que os caminhos sejam resolvidos corretamente para evitar erros de acesso a arquivos ou diretórios.
* **Descrições de Habilidades**: As descrições das habilidades devem ser claras e precisas, evitando ambiguidades que possam levar a interpretações erradas ou uso indevido das habilidades.
* **Segurança**: Todas as habilidades devem ser projetadas com segurança em mente, considerando possíveis vulnerabilidades e implementando medidas para mitigá-las, como validação de entrada de usuário e proteção contra injeção de código malicioso.
* **Manuseio de Exceções**: As exceções devem ser capturadas e tratadas de forma apropriada, fornecendo feedback útil ao usuário e registrando o evento para análise posterior, se necessário.

Ao seguir essas diretrizes, podemos garantir que as habilidades sejam robustas, seguras e fáceis de usar, proporcionando uma experiência positiva para os usuários.