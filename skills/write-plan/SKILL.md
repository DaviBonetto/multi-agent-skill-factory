# Draft Revisado
---
description: "Deprecated - use the superpowers:writing-plans skill instead"
---

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers writing-plans" skill instead.

## Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- **Parâmetros Inválidos**: Caso o usuário forneça parâmetros inválidos ou inconsistentes, o sistema deve retornar uma mensagem de erro clara e concisa, indicando os parâmetros corretos e como utilizá-los.
- **Comando Desconhecido**: Se o usuário tentar utilizar um comando desconhecido ou não suportado, o sistema deve informar que o comando não é reconhecido e sugerir comandos alternativos disponíveis.
- **Dependências não Atendidas**: Se a skill "superpowers:writing-plans" não estiver disponível devido a dependências não atendidas, o sistema deve notificar o usuário sobre as dependências necessárias e como resolvê-las.

### Tratamento de Erros
- **Mensagens de Erro Personalizadas**: O sistema deve fornecer mensagens de erro personalizadas para cada tipo de erro, ajudando o usuário a entender o que deu errado e como corrigir.
- **Logs de Erro**: Todos os erros devem ser registrados em logs para análise posterior, permitindo a identificação de padrões de erro e melhorias contínuas.

### Segurança
- **Validação de Entrada**: Todas as entradas de usuário devem ser validadas para prevenir ataques de injeção de código ou outras vulnerabilidades de segurança.
- **Autenticação e Autorização**: Acesso às skills deve ser controlado por mecanismos de autenticação e autorização, garantindo que apenas usuários autorizados possam utilizar as skills disponíveis.