# Week 2: Publish a Hub Dataset

Create and share high-quality datasets on the Hub. Good data is the foundation of good models—help the community by contributing datasets others can train on.

## Why This Matters

The best open source models are built on openly available datasets. By publishing well-documented, properly structured datasets, you're directly enabling the next generation of model development. Quality matters more than quantity.

## The Skill

Use `hf-datasets/` for this quest. Key capabilities:
- Initialize dataset repos with proper structure
- Multi-format support: chat, classification, QA, completion, tabular
- Template-based validation for data quality
- Streaming uploads without downloading entire datasets

```bash
# Quick setup with a template
python hf-datasets/scripts/dataset_manager.py quick_setup \
  --repo_id "your-username/dataset-name" --template chat
```

## XP Tiers

### Starter — 50 XP

**Upload a small, clean dataset with a complete dataset card.**

1. Create a dataset with ≤1,000 rows
2. Write a dataset card covering: license, splits, and data provenance
3. Upload to the Hub under the hackathon organization (or your own account)

**What counts:** Clean data, clear documentation, proper licensing.

```bash
python hf-datasets/scripts/dataset_manager.py init \
  --repo_id "hf-skills/your-dataset-name"

python hf-datasets/scripts/dataset_manager.py add_rows \
  --repo_id "hf-skills/your-dataset-name" \
  --template classification \
  --rows_json "$(cat your_data.json)"
```

### Standard — 100 XP

**Publish a conversational dataset with a complete dataset card.**

1. Create a dataset with ≤1,000 rows
2. Write a dataset card covering: license and splits.
3. Upload to the Hub under the hackathon organization.

**What counts:** Clean data, clear documentation, proper licensing.

### Advanced — 200 XP

**Translate a dataset into multiple languages and publish it on the Hub.**

1. Find a dataset on the Hub
2. Translate the dataset into multiple languages
3. Publish the translated datasets on the Hub under the hackathon organization

**What counts:** Translated datasets and merged PRs.

## Resources

- [SKILL.md](../../hf-datasets/SKILL.md) — Full skill documentation
- [Templates](../../hf-datasets/templates/) — JSON templates for each format
- [Examples](../../hf-datasets/examples/) — Sample data and system prompts

## Tratamento de Exceções e Edge Cases

Ao trabalhar com datasets, é importante considerar os seguintes casos de exceção e edge cases:
* **Dados inconsistentes**: Verifique se os dados estão consistentes e não contêm erros de formatação ou valores inválidos.
* **Dados vazios**: Verifique se os dados estão vazios ou contêm apenas valores nulos.
* **Licenças de dados**: Verifique se as licenças de dados estão claras e se os dados podem ser compartilhados publicamente.
* **Problemas de encoding**: Verifique se os dados estão corretamente codificados e se não há problemas de caractere especial.
* **Tamanhos de arquivo**: Verifique se os arquivos de dados não são muito grandes e se podem ser processados corretamente.
* **Erros de upload**: Verifique se os dados estão sendo carregados corretamente e se não há erros de conexão ou timeout.
* **Segurança de dados**: Verifique se os dados estão sendo armazenados e transmitidos de forma segura, utilizando protocolos de criptografia e autenticação adequados.

Para lidar com esses casos, é recomendado:
* **Validar os dados**: Antes de carregar os dados, verifique se eles estão consistentes e não contêm erros.
* **Utilizar templates**: Utilize templates para garantir que os dados estejam no formato correto e sejam consistentes.
* **Testar os dados**: Teste os dados antes de carregá-los para garantir que eles sejam processados corretamente.
* **Monitorar os logs**: Monitore os logs para detectar erros ou problemas durante o carregamento dos dados.
* **Implementar segurança**: Implemente medidas de segurança para proteger os dados, como criptografia e autenticação.

---

**Next Quest:** [Supervised Fine-Tuning](04_sft-finetune-hub.md)