# SKILL
## Descrição
description: "Deprecated - use the superpowers:executing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

## Uso
Para utilizar esta habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a habilidade "superpowers executing-plans" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Especiais
- **Comando Desconhecido**: Se o usuário informar um comando desconhecido, a habilidade deve retornar uma mensagem de erro clara e concisa, indicando que o comando não é suportado e sugerindo a utilização da habilidade "superpowers executing-plans".
- **Parâmetros Inválidos**: Se os parâmetros fornecidos forem inválidos ou inconsistentes, a habilidade deve detectar esses erros e fornecer uma resposta que ajude o usuário a entender o que deu errado e como corrigir.
- **Dependências Não Atendidas**: Se a habilidade "superpowers executing-plans" não estiver disponível devido a dependências não atendidas, a habilidade deve informar ao usuário sobre as dependências necessárias e como resolvê-las.
- **Limitações de Segurança**: A habilidade deve ser projetada para lidar com limitações de segurança, como permissões insuficientes ou restrições de acesso, fornecendo mensagens de erro apropriadas e orientando o usuário sobre como resolver essas questões.

## Segurança
A habilidade deve ser desenvolvida com segurança em mente, garantindo que:
- **Validação de Entrada**: Todas as entradas sejam validadas para prevenir ataques de injeção ou cross-site scripting (XSS).
- **Autenticação e Autorização**: A habilidade deve verificar a autenticação e autorização do usuário antes de executar ações, garantindo que apenas usuários autorizados possam acessar e utilizar a habilidade.
- **Criptografia**: Se a habilidade lidar com dados sensíveis, deve-se utilizar criptografia adequada para proteger esses dados durante a transmissão e o armazenamento.