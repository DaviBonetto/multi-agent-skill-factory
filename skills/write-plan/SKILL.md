# SKILL
## Descrição
description: "Deprecated - use the superpowers:writing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers writing-plans" skill instead.

## Uso
Para utilizar esta habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão principal. Eles devem solicitar que você use a habilidade "superpowers writing-plans" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para utilizar a habilidade "superpowers writing-plans", mostre uma mensagem de erro informando sobre a falta de permissão.
- Se a habilidade "superpowers writing-plans" não estiver disponível, mostre uma mensagem de erro informando sobre a indisponibilidade da habilidade.
- Se o usuário tentar utilizar esta habilidade após a sua remoção, mostre uma mensagem de erro informando que a habilidade foi removida e sugira a utilização da habilidade "superpowers writing-plans".

### Tratamento de Erros
- Se ocorrer um erro durante a execução da habilidade, mostre uma mensagem de erro genérica e registre o erro para análise posterior.
- Se a habilidade "superpowers writing-plans" não puder ser executada devido a um erro, mostre uma mensagem de erro informando sobre o problema e sugira tentar novamente mais tarde.

### Segurança
- Verifique se o usuário tem permissão para utilizar a habilidade "superpowers writing-plans" antes de executá-la.
- Valide os dados de entrada para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- Utilize protocolos de segurança adequados para proteger as comunicações entre o sistema e a habilidade "superpowers writing-plans".