# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**IMPORTANTE**: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
O tratamento de exceções e edge cases é crucial para garantir a robustez e a confiabilidade das habilidades. Aqui estão alguns pontos a considerar:
* **Erros de arquivo**: Verifique se o arquivo "SKILL.md" existe e é legível antes de tentar acessá-lo.
* **Erros de caminho**: Certifique-se de que os caminhos relativos sejam corretos e existam antes de tentar acessá-los.
* **Erros de descrição**: Verifique se a descrição da habilidade está correta e não vazia antes de exibi-la.
* **Edge cases de habilidades**: Considere casos de bordo, como habilidades com nomes idênticos ou descrições vazias, e defina como elas devem ser tratadas.
* **Tratamento de exceções**: Implemente um tratamento de exceções adequado para lidar com erros inesperados, como erros de sistema de arquivos ou erros de parsing de YAML.

Exemplos de como lidar com esses casos:
```markdown
{{#skills}}
  {{#if description}}
    {{name}}: `{{description}}`
  {{else}}
    {{name}}: `Descrição não disponível`
  {{/if}}
{{/skills}}
```
```markdown
{{#skills}}
  {{#if path}}
    {{name}} -> "{{path}}/SKILL.md"
  {{else}}
    {{name}} -> `Caminho não disponível`
  {{/if}}
{{/skills}}

## Implementação de Tratamento de Exceções
Para garantir a robustez, é fundamental implementar tratamento de exceções para cada habilidade. Isso pode ser feito utilizando blocos try-catch para capturar e lidar com erros de forma adequada.

## Exemplo de Implementação
```python
try:
    # Código da habilidade
except Exception as e:
    # Tratamento de exceção
    print(f"Erro ao executar a habilidade: {e}")
```