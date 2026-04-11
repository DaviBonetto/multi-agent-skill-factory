# SKILL
## Descrição
description: "Deprecated - use the superpowers:writing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers writing-plans" skill instead.

## Uso
Para utilizar esta skill, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão principal. Eles devem solicitar que você use a skill "superpowers writing-plans" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para utilizar a skill "superpowers writing-plans", mostre uma mensagem de erro informando sobre a falta de permissão.
- Se a skill "superpowers writing-plans" não estiver disponível, mostre uma mensagem de erro indicando que a skill não está disponível no momento.
- Se o usuário tentar utilizar esta skill após a data de remoção programada, mostre uma mensagem de erro informando que a skill foi removida e redirecione para a skill "superpowers writing-plans".

### Tratamento de Erros
- Se ocorrer um erro durante a execução da skill, mostre uma mensagem de erro genérica e registre o erro para análise posterior.
- Se a skill "superpowers writing-plans" retornar um erro, mostre a mensagem de erro original e forneça orientações sobre como proceder.

### Segurança
- Verifique se o usuário tem permissão para acessar a skill "superpowers writing-plans" antes de redirecioná-lo.
- Valide todos os inputs do usuário para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- Utilize criptografia adequada para proteger as comunicações entre o usuário e a skill "superpowers writing-plans".