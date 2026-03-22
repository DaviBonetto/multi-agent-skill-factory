---
description: "Deprecated - use the superpowers:executing-plans skill instead"
---

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

### ⚠️ Tratamento de Exceções e Edge Cases
#### Erros Possíveis
*   Caso o usuário não tenha permissão para executar a skill, mostre uma mensagem de erro indicando que a ação não é permitida.
*   Se a skill "superpowers:executing-plans" não estiver disponível, forneça uma mensagem de erro com instruções sobre como habilitá-la.
*   Em caso de falha na comunicação com o servidor, exiba uma mensagem de erro genérica solicitando que o usuário tente novamente mais tarde.

#### Edge Cases
*   **Uso em Ambientes de Teste**: Certifique-se de que a skill funcione corretamente em ambientes de teste, não causando impacto nos dados reais.
*   **Compatibilidade com Versões Anteriores**: A skill deve ser compatível com versões anteriores do sistema, garantindo que os usuários com versões mais antigas possam receber as mensagens de depreciação e instruções corretas.
*   **Acessibilidade**: A mensagem de depreciação e as instruções devem ser acessíveis para usuários com deficiências, seguindo as diretrizes de acessibilidade web.