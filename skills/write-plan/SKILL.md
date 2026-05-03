# Skill: Deprecated Command
## Descrição
description: "Deprecated - use the superpowers:writing-plans skill instead"

Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers writing-plans" skill instead, providing a clear example of its usage, such as: "Para criar um plano de ação, use o comando 'superpowers writing-plans --create-plan <nome_do_plano>'".

## Uso
Para usar esta skill, basta informar ao seu parceiro humano que o comando está depreciado e será removido na próxima versão major. Eles devem solicitar que você use a skill "superpowers writing-plans" em vez disso, seguindo as instruções de uso adequadas.

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Especiais
- **Comando Desconhecido**: Se o usuário informar um comando desconhecido, a skill deve retornar uma mensagem de erro clara e concisa, indicando que o comando não é válido e sugerindo a utilização da skill "superpowers writing-plans", por exemplo: "Comando desconhecido. Por favor, use 'superpowers writing-plans --help' para obter ajuda".
- **Parâmetros Inválidos**: Se o usuário fornecer parâmetros inválidos, a skill deve tratar esses parâmetros como se não tivessem sido fornecidos e retornar uma mensagem de erro amigável, orientando o usuário sobre como usar a skill corretamente, como: "Parâmetros inválidos. Use 'superpowers writing-plans --create-plan <nome_do_plano>' para criar um novo plano".
- **Erros de Sistema**: Em caso de erros de sistema, a skill deve registrar o erro e retornar uma mensagem de erro genérica ao usuário, informando que ocorreu um problema interno e que a equipe de suporte será notificada, por exemplo: "Ocorreu um erro interno. Por favor, tente novamente mais tarde ou contate o suporte".
- **Limitações de Segurança**: A skill deve ser projetada com segurança em mente, garantindo que não haja exposição de informações sensíveis ou vulnerabilidades que possam ser exploradas por ataques mal-intencionados, como utilizar criptografia para proteger dados sensíveis e manter atualizações regulares de segurança.

## Segurança
A segurança é uma prioridade para esta skill. Todas as interações com a skill devem ser realizadas via canais seguros, como HTTPS, e os dados dos usuários devem ser tratados de acordo com as políticas de privacidade e segurança da plataforma, como o GDPR ou a LGPD, dependendo da região. Além disso, a skill deve ser regularmente atualizada para refletir as melhores práticas de segurança e proteger contra novas ameaças, como atualizações de bibliotecas e frameworks.