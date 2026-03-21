description: "Deprecated - use the superpowers:brainstorming skill instead"
# Introdução
Tell your human partner that this command is deprecated and will be removed in the next major release. They should ask you to use the "superpowers brainstorming" skill instead.

# Instruções
Para utilizar a habilidade correta, siga os passos abaixo:
1. Informe ao seu parceiro humano que este comando está depreciado.
2. Explique que ele será removido na próxima versão major.
3. Sugira a utilização da habilidade "superpowers brainstorming" como alternativa.

# ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Inválidos
- **Comando Desconhecido**: Caso o usuário insira um comando desconhecido, mostre uma mensagem de erro amigável indicando que o comando não é reconhecido e sugira a utilização da habilidade "superpowers brainstorming".
- **Parâmetros Incorretos**: Se o usuário fornecer parâmetros incorretos, mostre uma mensagem de erro explicando como os parâmetros devem ser utilizados corretamente.
- **Uso Excessivo**: Implemente um limite de uso para evitar abusos. Se o limite for atingido, mostre uma mensagem informando que o limite diário foi alcançado e sugira alternativas.

### Tratamento de Erros
- **Mensagens de Erro**: Todas as mensagens de erro devem ser claras, concisas e fornecer orientações sobre como resolver o problema.
- **Logs de Erro**: Registre todos os erros ocorridos para análise posterior e melhoria contínua.

### Segurança
- **Validação de Entrada**: Valide todas as entradas de usuário para evitar injeção de código malicioso.
- **Autenticação**: Certifique-se de que apenas usuários autorizados possam acessar a habilidade.
- **Criptografia**: Use criptografia adequada para proteger dados sensíveis.