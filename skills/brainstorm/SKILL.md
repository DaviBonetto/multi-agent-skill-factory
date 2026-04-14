# SKILL
## Descrição
description: "Deprecated - use the superpowers:brainstorming skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers brainstorming" skill instead.

## Uso
Para utilizar esta skill, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a skill "superpowers brainstorming" ao invés.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para utilizar a skill "superpowers brainstorming", mostre uma mensagem de erro informando sobre a falta de permissão.
- Se a skill "superpowers brainstorming" não estiver disponível, mostre uma mensagem de erro informando sobre a indisponibilidade da skill.
- Se o usuário tentar utilizar esta skill após a sua remoção, mostre uma mensagem de erro informando que a skill foi removida e direcione-o para a skill "superpowers brainstorming".

### Tratamento de Erros
- Verifique se o usuário está autenticado antes de tentar utilizar a skill.
- Verifique se a skill "superpowers brainstorming" está disponível antes de tentar redirecionar o usuário.
- Trate quaisquer erros que ocorram durante a execução da skill e mostre mensagens de erro amigáveis ao usuário.

### Segurança
- Verifique se o usuário tem permissão para acessar a skill "superpowers brainstorming" antes de redirecioná-lo.
- Utilize protocolos de segurança adequados para proteger as informações do usuário durante a transição para a skill "superpowers brainstorming".
- Certifique-se de que a skill "superpowers brainstorming" esteja configurada corretamente e seja segura para uso.