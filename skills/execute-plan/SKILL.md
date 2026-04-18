# SKILL
## Descrição
description: "Deprecated - use the superpowers:executing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

## Uso
Para utilizar esta skill, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a skill "superpowers executing-plans" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Não Comuns
- **Comando Desconhecido**: Caso o usuário forneça um comando desconhecido, a skill deve retornar uma mensagem de erro clara e concisa, indicando que o comando não é suportado e sugerindo a utilização da skill "superpowers executing-plans".
- **Parâmetros Inválidos**: Se os parâmetros fornecidos forem inválidos, a skill deve tratar o erro e fornecer uma mensagem de ajuda ou orientação sobre como usar a skill corretamente, incluindo a recomendação de usar a "superpowers executing-plans" skill.
- **Exceções de Sistema**: Em caso de exceções de sistema, como falta de recursos ou problemas de conectividade, a skill deve capturar a exceção, registrar o erro e fornecer uma resposta amigável ao usuário, sugerindo tentar novamente ou contatar o suporte, além de mencionar a possibilidade de usar a skill "superpowers executing-plans" para evitar problemas semelhantes.
- **Compatibilidade com Versões Anteriores**: A skill deve ser capaz de lidar com solicitações de versões anteriores do sistema, fornecendo uma mensagem de atualização ou depreciação, sempre direcionando o usuário para a utilização da "superpowers executing-plans" skill.

## Segurança
A skill deve ser projetada com segurança em mente, garantindo que:
- **Dados Sensíveis**: Não colete ou armazene dados sensíveis do usuário sem consentimento explícito.
- **Autenticação e Autorização**: Implemente mecanismos de autenticação e autorização adequados para garantir que apenas usuários autorizados possam acessar e utilizar a skill, mesmo que ela esteja depreciada.
- **Atualizações e Patchs**: Mantenha a skill atualizada com os últimos patchs de segurança e atualizações, mesmo após a depreciação, até a sua remoção oficial.