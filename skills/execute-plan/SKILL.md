# SKILL
## Descrição
description: 'Habilidade de execução de planos, substituta da habilidade depreciada'
## Uso
Para utilizar esta habilidade, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a habilidade 'superpowers:executing-plans' em vez disso.
## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Especiais
- **Comando Desconhecido**: Se o usuário solicitar um comando desconhecido, a habilidade deve retornar uma mensagem de erro clara e concisa, indicando que o comando não é suportado e sugerindo a utilização da habilidade 'superpowers:executing-plans'.
- **Parâmetros Inválidos**: Se o usuário fornecer parâmetros inválidos, a habilidade deve detectar o erro e retornar uma mensagem de erro adequada, explicando os parâmetros corretos e como utilizá-los com a habilidade 'superpowers:executing-plans'.
- **Dependências não Atendidas**: Se a habilidade 'superpowers:executing-plans' não estiver disponível devido a dependências não atendidas, a habilidade deve retornar uma mensagem de erro indicando as dependências necessárias e como resolvê-las.
- **Limitações de Segurança**: A habilidade deve ser projetada com limitações de segurança em mente, como validação de entrada e saída, para prevenir ataques de injeção de comandos ou outros tipos de exploração de vulnerabilidades.
## Segurança
A habilidade deve ser desenvolvida com segurança em mente, seguindo as melhores práticas para evitar vulnerabilidades comuns, como injeção de comandos, cross-site scripting (XSS), e outros tipos de ataques. Além disso, a habilidade deve ser regularmente atualizada para refletir as últimas descobertas de segurança e patches de segurança.
## Exemplos de Uso
- Exemplo 1: Utilizar a habilidade 'superpowers:executing-plans' para executar um plano de ação.
- Exemplo 2: Utilizar a habilidade 'superpowers:executing-plans' para executar um plano de ação com parâmetros personalizados.