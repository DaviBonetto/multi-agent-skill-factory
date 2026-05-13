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
Para garantir a robustez e a segurança das habilidades, é fundamental considerar os seguintes casos de bordo e exceções:
- **Habilidades não documentadas:** Se uma habilidade não tiver um arquivo SKILL.md, ela não deve ser considerada válida. O sistema deve lançar uma exceção ou alertar o usuário sobre a falta de documentação.
- **Caminhos relativos:** Ao referenciar caminhos dentro das pastas de habilidades, é crucial garantir que os caminhos sejam corretos e existam. Caso contrário, o sistema deve tratar o erro adequadamente, seja lançando uma exceção ou fornecendo um caminho padrão.
- **Descrições de habilidades vazias:** Se a descrição de uma habilidade estiver vazia, o sistema deve considerar essa habilidade como não válida ou fornecer uma descrição padrão.
- **Erros de leitura do arquivo SKILL.md:** Se houver um erro ao ler o arquivo SKILL.md, o sistema deve tratar o erro, fornecendo uma mensagem de erro clara ou uma ação alternativa.
- **Segurança:** Todas as habilidades devem ser verificadas para garantir que não contenham código malicioso ou vulnerabilidades de segurança. O sistema deve ter mecanismos para detectar e prevenir tais ameaças.

Ao considerar esses casos de bordo e exceções, podemos garantir que as habilidades adicionais sejam utilizadas de forma segura e eficaz, melhorando a experiência do usuário e a robustez do sistema.