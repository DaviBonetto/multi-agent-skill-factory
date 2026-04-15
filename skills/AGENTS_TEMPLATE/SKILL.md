# Introdução às Habilidades Adicionais
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
{{#skills}}
 - {{name}} -> "{{path}}/SKILL.md"
{{/skills}}

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
{{#skills}}
{{name}}: `{{description}}`

{{/skills}}

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `scripts/example.py` do hf-datasets seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Arquivo
- **Arquivo "SKILL.md" não encontrado:** Verifique se o arquivo "SKILL.md" existe no diretório especificado e se o caminho está correto.
- **Conteúdo inválido no arquivo "SKILL.md":** Certifique-se de que o arquivo "SKILL.md" contenha informações válidas e bem formatadas.

### Erros de Caminho
- **Caminho relativo incorreto:** Verifique se os caminhos relativos dentro das pastas de habilidades estão corretos e se correspondem aos arquivos ou diretórios existentes.
- **Caminho absoluto não suportado:** Lembre-se de que apenas caminhos relativos são suportados dentro das pastas de habilidades.

### Segurança
- **Validação de Entradas:** Sempre valide as entradas de usuário para evitar injeção de código malicioso ou outros ataques.
- **Uso de Dependências:** Certifique-se de que todas as dependências utilizadas estejam atualizadas e sejam de fontes confiáveis para evitar vulnerabilidades de segurança.

### Outros Casos de Borda
- **Múltiplas Habilidades com o Mesmo Nome:** Em caso de habilidades com o mesmo nome, verifique se as descrições são claras o suficiente para distinguir entre elas.
- **Habilidades Desatualizadas:** Regularmente verifique e atualize as habilidades para garantir que elas permaneçam relevantes e funcionais.