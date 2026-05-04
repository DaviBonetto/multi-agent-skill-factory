# SKILL
## Descrição
description: "Deprecated - use the superpowers:brainstorming skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers brainstorming" skill instead.

## Uso
Para utilizar esta habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a habilidade "superpowers brainstorming" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para utilizar a habilidade "superpowers brainstorming", mostre uma mensagem de erro informando que a habilidade está indisponível.
- Se a habilidade "superpowers brainstorming" estiver desativada, mostre uma mensagem de erro informando que a habilidade está desativada.
- Se o usuário tentar utilizar esta habilidade após a sua remoção, mostre uma mensagem de erro informando que a habilidade foi removida e sugira a utilização da habilidade "superpowers brainstorming" em vez disso.

### Tratamento de Erros
- Se ocorrer um erro durante a execução da habilidade, mostre uma mensagem de erro genérica informando que ocorreu um problema e solicite que o usuário tente novamente.
- Se o erro for específico da habilidade "superpowers brainstorming", mostre uma mensagem de erro detalhada informando o problema e sugira a solução.

### Segurança
- Verifique se o usuário tem permissão para utilizar a habilidade "superpowers brainstorming" antes de executá-la.
- Valide os dados de entrada para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- Utilize criptografia para proteger os dados transmitidos durante a execução da habilidade, se necessário.