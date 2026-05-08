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
Para garantir a robustez e a segurança das habilidades, é fundamental considerar os seguintes casos:
* **Habilidades não encontradas:** Se uma habilidade não for encontrada no diretório especificado, o sistema deve retornar uma mensagem de erro clara e concisa, indicando que a habilidade não existe ou não está disponível.
* **Arquivos SKILL.md corrompidos ou malformados:** Se o arquivo SKILL.md estiver corrompido ou malformado, o sistema deve detectar o erro e retornar uma mensagem de erro apropriada, evitando que o sistema entre em um estado inconsistente.
* **Caminhos relativos inválidos:** Se um caminho relativo for inválido ou não puder ser resolvido, o sistema deve retornar uma mensagem de erro indicando que o caminho é inválido ou não pode ser acessado.
* **Permissões de acesso:** O sistema deve verificar as permissões de acesso às habilidades e arquivos relacionados, garantindo que apenas usuários autorizados possam acessar e executar as habilidades.
* **Tratamento de erros de execução:** O sistema deve ter mecanismos de tratamento de erros de execução para lidar com erros inesperados durante a execução das habilidades, garantindo que o sistema permaneça estável e seguro.

Ao considerar esses casos e implementar os tratamentos de exceção e edge cases apropriados, podemos garantir que as habilidades sejam executadas de forma segura e confiável.