# Introdução
description: "Você DEVE usar isso antes de qualquer trabalho criativo - criar recursos, construir componentes, adicionar funcionalidades ou modificar comportamentos. Explora requisitos e design antes da implementação."
disable-model-invocation: true

# Invocação das Habilidades
Invoke a habilidade de brainstorming e siga-a exatamente como apresentada a você.

# ⚠️ Tratamento de Exceções e Edge Cases
## Tratamento de Erros
- **Erro de Invocação**: Caso a invocação da habilidade de brainstorming falhe, verifique se a habilidade está corretamente configurada e se os parâmetros de entrada estão válidos.
- **Erro de Formatação**: Se o formato do input não estiver de acordo com o esperado, o sistema deve retornar uma mensagem de erro clara e concisa, indicando o problema e como corrigi-lo.
- **Exceção de Tempo de Execução**: Em caso de exceções durante a execução, o sistema deve capturar a exceção, registrar o erro e fornecer uma resposta significativa ao usuário, indicando a ocorrência de um problema e as etapas para resolução.

## Edge Cases
- **Input Vazio**: Se o usuário não fornecer nenhum input, o sistema deve solicitar que o usuário forneça as informações necessárias para prosseguir.
- **Input Inválido**: Se o input fornecido não estiver de acordo com os requisitos (por exemplo, formato incorreto, dados faltantes), o sistema deve informar ao usuário sobre o problema e como corrigi-lo.
- **Sobrecarga de Sistema**: Em caso de sobrecarga do sistema devido a uma grande quantidade de requisições simultâneas, o sistema deve implementar mecanismos de controle de fluxo para evitar falhas, como fila de requisições ou limitação de acesso.

# Segurança
- **Autenticação**: Todas as requisições devem ser autenticadas para garantir que apenas usuários autorizados possam invocar a habilidade.
- **Autorização**: O sistema deve verificar as permissões do usuário antes de permitir a invocação da habilidade, garantindo que o usuário tenha as permissões necessárias para realizar a ação solicitada.
- **Criptografia**: Todas as comunicações entre o cliente e o servidor devem ser criptografadas para proteger os dados contra interceptação e acesso não autorizado.