---
description: "Deprecated - use the superpowers:executing-plans skill instead"
---
# Introdução
Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

# Uso
Para utilizar essa habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a habilidade "superpowers executing-plans" em vez disso.

# ⚠️ Tratamento de Exceções e Edge Cases
## Casos de Uso Inválidos
- Se o usuário não tiver permissão para executar a habilidade "superpowers executing-plans", mostre uma mensagem de erro informando que a permissão é necessária.
- Se a habilidade "superpowers executing-plans" não estiver disponível, mostre uma mensagem de erro informando que a habilidade não está disponível.
- Se o usuário tentar usar essa habilidade após a sua remoção, mostre uma mensagem de erro informando que a habilidade foi removida e sugira usar a habilidade "superpowers executing-plans" em vez disso.

## Tratamento de Erros
- Se ocorrer um erro durante a execução da habilidade, mostre uma mensagem de erro genérica informando que ocorreu um problema e solicite que o usuário tente novamente.
- Se o erro for específico, mostre uma mensagem de erro detalhada informando o que deu errado e como resolver o problema.

## Segurança
- Certifique-se de que a habilidade "superpowers executing-plans" seja executada com as permissões necessárias para evitar acessos não autorizados.
- Valide os inputs do usuário para evitar injeção de comandos ou outros ataques de segurança.
- Use criptografia adequada para proteger as comunicações entre o sistema e o usuário.