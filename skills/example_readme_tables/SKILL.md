# Example Evaluation Table Formats

This file shows various formats of evaluation tables that can be extracted from model README files.

## Format 1: Benchmarks as Rows (Most Common)

```markdown
| Benchmark | Score |
|-----------|-------|
| MMLU      | 85.2  |
| HumanEval | 72.5  |
| GSM8K     | 91.3  |
| HellaSwag | 88.9  |
```

## Format 2: Multiple Metric Columns

```markdown
| Benchmark | Accuracy | F1 Score |
|-----------|----------|----------|
| MMLU      | 85.2     | 0.84     |
| GSM8K     | 91.3     | 0.91     |
| DROP      | 78.5     | 0.77     |
```

## Format 3: Benchmarks as Columns

```markdown
| MMLU | HumanEval | GSM8K | HellaSwag |
|------|-----------|-------|-----------|
| 85.2 | 72.5      | 91.3  | 88.9      |
```

## Format 4: Percentage Values

```markdown
| Benchmark     | Score    |
|---------------|----------|
| MMLU          | 85.2%    |
| HumanEval     | 72.5%    |
| GSM8K         | 91.3%    |
| TruthfulQA    | 68.7%    |
```

## Format 5: Mixed Format with Categories

```markdown
### Reasoning

| Benchmark | Score |
|-----------|-------|
| MMLU      | 85.2  |
| BBH       | 82.4  |
| GPQA      | 71.3  |

### Coding

| Benchmark | Score |
|-----------|-------|
| HumanEval | 72.5  |
| MBPP      | 78.9  |

### Math

| Benchmark | Score |
|-----------|-------|
| GSM8K     | 91.3  |
| MATH      | 65.8  |
```

## Format 6: With Additional Columns

```markdown
| Benchmark | Score | Rank | Notes              |
|-----------|-------|------|--------------------|
| MMLU      | 85.2  | #5   | 5-shot             |
| HumanEval | 72.5  | #8   | pass@1             |
| GSM8K     | 91.3  | #3   | 8-shot, maj@1      |
```

## How the Extractor Works

The script will:
1. Find all markdown tables in the README
2. Identify which tables contain evaluation results
3. Parse the table structure (rows vs columns)
4. Extract numeric values as scores
5. Convert to model-index YAML format

## Tips for README Authors

To ensure your evaluation tables are properly extracted:

1. **Use clear headers**: Include "Benchmark", "Score", or similar terms
2. **Keep it simple**: Stick to benchmark name + score columns
3. **Use standard formats**: Follow markdown table syntax
4. **Include numeric values**: Ensure scores are parseable numbers
5. **Be consistent**: Use the same format across multiple tables

## Example Complete README Section

```markdown
# Model Card for MyModel-7B

## Evaluation Results

Our model was evaluated on several standard benchmarks:

| Benchmark     | Score |
|---------------|-------|
| MMLU          | 85.2  |
| HumanEval     | 72.5  |
| GSM8K         | 91.3  |
| HellaSwag     | 88.9  |
| ARC-Challenge | 81.7  |
| TruthfulQA    | 68.7  |

### Detailed Results

For more detailed results and methodology, see our [paper](link).
```

## Running the Extractor

```bash
# Extract from this example
uv run scripts/evaluation_manager.py extract-readme \
  --repo-id "your-username/your-model" \
  --dry-run

# Apply to your model card
uv run scripts/evaluation_manager.py extract-readme \
  --repo-id "your-username/your-model" \
  --task-type "text-generation"
```

## ⚠️ Tratamento de Exceções e Edge Cases

O tratamento de exceções e edge cases é crucial para garantir a robustez e confiabilidade do extrator de tabelas de avaliação. Aqui estão alguns exemplos de como lidar com esses casos:

* **Tabelas malformadas**: O extrator deve ser capaz de lidar com tabelas que não seguem a sintaxe markdown padrão. Isso pode incluir tabelas com linhas ou colunas faltantes, ou com células que contenham texto em vez de números.
* **Valores não numéricos**: O extrator deve ser capaz de lidar com valores não numéricos nas células das tabelas. Isso pode incluir texto, datas ou outros tipos de dados.
* **Tabelas com múltiplas linhas de cabeçalho**: O extrator deve ser capaz de lidar com tabelas que têm múltiplas linhas de cabeçalho. Isso pode incluir tabelas com linhas de cabeçalho que se estendem por várias linhas.
* **Tabelas com células vazias**: O extrator deve ser capaz de lidar com tabelas que têm células vazias. Isso pode incluir tabelas com células que não contêm nenhum valor.
* **Erros de parsing**: O extrator deve ser capaz de lidar com erros de parsing que ocorrem durante a extração das tabelas. Isso pode incluir erros de sintaxe ou erros de formato.

Para lidar com esses casos, o extrator pode implementar as seguintes estratégias:

* **Validação de tabela**: O extrator pode validar a tabela antes de tentar extrair os dados. Isso pode incluir verificar se a tabela está bem formada e se as células contêm valores numéricos.
* **Tratamento de exceções**: O extrator pode implementar tratamento de exceções para lidar com erros que ocorrem durante a extração dos dados. Isso pode incluir capturar exceções e registrar erros para que possam ser investigados posteriormente.
* **Uso de bibliotecas de parsing**: O extrator pode usar bibliotecas de parsing para lidar com tabelas malformadas ou com valores não numéricos. Isso pode incluir usar bibliotecas como pandas ou numpy para lidar com dados numéricos.
* **Implementação de regras de negócios**: O extrator pode implementar regras de negócios para lidar com casos específicos. Isso pode incluir regras para lidar com tabelas que têm múltiplas linhas de cabeçalho ou com células vazias.