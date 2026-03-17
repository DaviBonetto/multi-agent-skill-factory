# Retrieving Metrics with Trackio CLI
The `trackio` CLI provides direct terminal access to query Trackio experiment tracking data locally without needing to start the MCP server.
...
## References
- **Complete CLI documentation**: See [docs/source/cli_commands.md](docs/source/cli_commands.md)
- **API and MCP Server**: See [docs/source/api_mcp_server.md](docs/source/api_mcp_server.md)
...
## ⚠️ Tratamento de Exceções e Edge Cases
O tratamento de exceções e edge cases é crucial para garantir a robustez e confiabilidade do sistema. Aqui estão alguns exemplos de como lidar com esses casos:
* **Projeto não encontrado**: Se o projeto não for encontrado, o sistema deve retornar um erro claro e conciso, indicando que o projeto não existe.
* **Run não encontrado**: Se o run não for encontrado, o sistema deve retornar um erro claro e conciso, indicando que o run não existe.
* **Métrica não encontrada**: Se a métrica não for encontrada, o sistema deve retornar um erro claro e conciso, indicando que a métrica não existe.
* **Erro de sintaxe**: Se houver um erro de sintaxe na entrada, o sistema deve retornar um erro claro e conciso, indicando o erro de sintaxe.
* **Valor inválido**: Se o valor for inválido, o sistema deve retornar um erro claro e conciso, indicando que o valor é inválido.
...
