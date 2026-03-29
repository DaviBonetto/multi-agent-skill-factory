---
description: "Deprecated - use the superpowers:executing-plans skill instead"
---
# Introdução
Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

# Uso
Para utilizar essa habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a habilidade "superpowers executing-plans" em vez disso.

# ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para executar a habilidade "superpowers executing-plans", uma mensagem de erro deve ser exibida informando sobre a falta de permissão.
- Se a habilidade "superpowers executing-plans" não estiver disponível, uma mensagem de erro deve ser exibida informando sobre a indisponibilidade da habilidade.
- Se o usuário tentar utilizar essa habilidade de forma indevida, uma mensagem de erro deve ser exibida com orientações sobre o uso correto.

### Tratamento de Erros
- Todos os erros devem ser registrados em um log de erros para análise posterior.
- Em caso de erro, o sistema deve permanecer estável e não afetar outras habilidades.
- O usuário deve receber uma mensagem de erro clara e concisa, informando sobre o problema e como resolvê-lo.

### Segurança
- A habilidade deve ser projetada para evitar ataques de injeção de comandos ou SQL.
- Todas as entradas de usuário devem ser validadas e sanitizadas para evitar vulnerabilidades de segurança.
- A habilidade deve ser executada com permissões mínimas necessárias para evitar danos ao sistema em caso de erro ou ataque.