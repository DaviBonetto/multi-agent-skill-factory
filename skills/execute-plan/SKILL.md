---
description: "Deprecated - use the superpowers:executing-plans skill instead"
---

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers executing-plans" skill instead.

### ⚠️ Tratamento de Exceções e Edge Cases
#### Exceções
- **Erro de Comunicação**: Em caso de falha na comunicação com o parceiro humano, o sistema deve registrar o erro e tentar novamente após um período de tempo definido.
- **Erro de Depreciação**: Se o comando for utilizado após a data de remoção programada, o sistema deve exibir uma mensagem de erro claro e direcionar o usuário para a documentação da skill substituta.
- **Erro de Skill Não Encontrada**: Se a skill "superpowers executing-plans" não for encontrada, o sistema deve exibir uma mensagem de erro e fornecer instruções para instalar ou configurar a skill corretamente.

#### Edge Cases
- **Uso em Ambientes de Teste**: Em ambientes de teste, o comando deprecado deve ser permitido para fins de testes de compatibilidade, mas com uma advertência clara sobre a depreciação.
- **Uso por Usuários com Privilégios Especiais**: Usuários com privilégios especiais devem ter acesso ao comando deprecado por um período de tempo limitado após a data de remoção programada, para permitir a transição suave para a nova skill.
- **Documentação e Suporte**: A documentação e o suporte para o comando deprecado devem ser atualizados para refletir a depreciação e direcionar os usuários para a skill substituta.