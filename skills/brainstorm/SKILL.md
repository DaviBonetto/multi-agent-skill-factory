# SKILL
## Descrição
description: 'Essa skill está deprecada. Use a skill superpowers:brainstorming em seu lugar.'
## Uso
Para utilizar a skill superpowers:brainstorming, basta chamar o comando 'superpowers brainstorming'.
## ⚠️ Tratamento de Exceções e Edge Cases
- **Caso de Uso Inválido**: Se o usuário tentar utilizar essa skill em uma versão onde ela já foi removida, o sistema deve retornar uma mensagem de erro clara, indicando que a skill está depreciada e não está mais disponível.
- **Dependência em Versões Antigas**: Se o usuário estiver utilizando uma versão antiga do sistema que ainda suporta essa skill, mas ela está marcada como depreciada, o sistema deve exibir um aviso sobre a depreciação e recomendar a utilização da skill 'superpowers brainstorming' como substituta.
- **Comportamento em Ambientes de Teste**: Em ambientes de teste, a skill deve ser capaz de simular seu comportamento de forma consistente, permitindo que os testes sejam realizados sem interferir com o funcionamento normal do sistema.
- **Documentação e Comunicação**: A documentação da skill deve refletir claramente seu status de depreciação, incluindo a data prevista para sua remoção e as instruções para migrar para a skill recomendada.
- **Manuseio de Erros**: Em caso de erros durante a execução da skill, o sistema deve lidar com esses erros de forma a minimizar o impacto no usuário, fornecendo mensagens de erro claras e úteis para o diagnóstico e resolução do problema.