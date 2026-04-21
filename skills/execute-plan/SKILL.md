# SKILL
## Descrição
description: "Deprecated - use the superpowers:executing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

## Uso
Para utilizar esta skill, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a skill "superpowers executing-plans" em vez disso.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- Se o usuário não tiver permissão para executar a skill "superpowers executing-plans", mostre uma mensagem de erro informando sobre a falta de permissão.
- Se a skill "superpowers executing-plans" não estiver disponível, mostre uma mensagem de erro informando sobre a indisponibilidade da skill.
- Se o usuário tentar executar esta skill após a sua remoção, mostre uma mensagem de erro informando que a skill foi removida e direcione-o para a skill "superpowers executing-plans".

### Tratamento de Erros
- Se ocorrer um erro durante a execução da skill, mostre uma mensagem de erro genérica e solicite que o usuário tente novamente.
- Se o erro for específico da skill "superpowers executing-plans", mostre uma mensagem de erro detalhada e forneça orientações sobre como resolver o problema.

### Segurança
- Certifique-se de que a skill "superpowers executing-plans" seja executada com as permissões necessárias para evitar acessos não autorizados.
- Valide os inputs do usuário para evitar injeção de comandos ou outros tipos de ataques mal-intencionados.
- Implemente um sistema de logging para registrar todas as tentativas de execução da skill e os erros ocorridos, para fins de auditoria e melhoria da segurança.