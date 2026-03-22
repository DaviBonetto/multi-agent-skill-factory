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

O tratamento de exceções e edge cases é crucial para garantir a robustez e confiabilidade do script de extração. Aqui estão alguns exemplos de como lidar com esses casos:

* **Tabelas malformadas**: O script deve ser capaz de lidar com tabelas que não seguem a sintaxe markdown padrão. Isso pode ser feito usando bibliotecas de parsing de markdown que possam lidar com erros de sintaxe.
* **Valores não numéricos**: O script deve ser capaz de lidar com valores que não são numéricos, como texto ou datas. Isso pode ser feito usando funções de parsing que possam lidar com diferentes tipos de dados.
* **Tabelas vazias**: O script deve ser capaz de lidar com tabelas vazias, ou seja, tabelas que não contêm nenhuma linha ou coluna. Isso pode ser feito usando condições que verifiquem se a tabela está vazia antes de tentar extrair os dados.
* **Erros de conexão**: O script deve ser capaz de lidar com erros de conexão, como timeouts ou erros de rede. Isso pode ser feito usando mecanismos de retry e timeout que possam lidar com esses erros.
* **Erros de permissão**: O script deve ser capaz de lidar com erros de permissão, como falta de permissão para acessar o repositório ou o arquivo. Isso pode ser feito usando condições que verifiquem se o script tem permissão para acessar o recurso antes de tentar extrair os dados.

Exemplos de código que lidam com esses casos:

```python
import pandas as pd

def extract_table(table):
    try:
        # Tentar parsear a tabela
        df = pd.read_csv(table, sep='|')
        return df
    except pd.errors.EmptyDataError:
        # Lidar com tabelas vazias
        print("Tabela vazia")
        return None
    except pd.errors.ParserError:
        # Lidar com tabelas malformadas
        print("Tabela malformada")
        return None

def extract_values(table):
    try:
        # Tentar extrair os valores
        values = table.split('|')
        return values
    except ValueError:
        # Lidar com valores não numéricos
        print("Valores não numéricos")
        return None

def run_extractor(repo_id, task_type):
    try:
        # Tentar executar o script
        uv.run scripts/evaluation_manager.py extract-readme \
          --repo-id repo_id \
          --task-type task_type
    except ConnectionError:
        # Lidar com erros de conexão
        print("Erro de conexão")
        return None
    except PermissionError:
        # Lidar com erros de permissão
        print("Erro de permissão")
        return None
