# Week 3: Supervised Fine-Tuning on the Hub

Fine-tune and share models on the Hub. Take a base model, train it on your data, and publish the result for the community to use.

## Why This Matters

Fine-tuning is how we adapt foundation models to specific tasks. By sharing fine-tuned models—along with your training methodology—you're giving the community ready-to-use solutions and reproducible recipes they can learn from.

## The Skill

Use `hf-llm-trainer/` for this quest. Key capabilities:
- **SFT** (Supervised Fine-Tuning) — Standard instruction tuning
- **DPO** (Direct Preference Optimization) — Alignment from preference data
- **GRPO** (Group Relative Policy Optimization) — Online RL training
- Cloud GPU training on HF Jobs—no local setup required
- Trackio integration for real-time monitoring
- GGUF conversion for local deployment

Your coding agent uses `hf_jobs()` to submit training scripts directly to HF infrastructure.

## XP Tiers

We'll announce the XP tiers for this quest soon.

## Resources
- [SKILL.md](../../hf-llm-trainer/SKILL.md) — Full skill documentation
- [SFT Example](../../hf-llm-trainer/scripts/train_sft_example.py) — Production SFT template
- [DPO Example](../../hf-llm-trainer/scripts/train_dpo_example.py) — Production DPO template
- [GRPO Example](../../hf-llm-trainer/scripts/train_grpo_example.py) — Production GRPO template
- [Training Methods](../../hf-llm-trainer/references/training_methods.md) — Method selection guide
- [Hardware Guide](../../hf-llm-trainer/references/hardware_guide.md) — GPU selection

## ⚠️ Tratamento de Exceções e Edge Cases

Ao trabalhar com fine-tuning de modelos, é importante considerar os seguintes casos de bordo e exceções:
* **Dados insuficientes**: Certifique-se de que você tem dados suficientes para treinar o modelo. Se os dados forem insuficientes, o modelo pode não ser capaz de aprender padrões significativos.
* **Dados desequilibrados**: Se os dados estiverem desequilibrados, o modelo pode ser tendencioso em relação à classe majoritária. Use técnicas de oversampling ou undersampling para equilibrar os dados.
* **Parâmetros de treinamento**: Certifique-se de que os parâmetros de treinamento estejam configurados corretamente. Parâmetros como taxa de aprendizado, tamanho do lote e número de épocas podem afetar significativamente o desempenho do modelo.
* **Erros de inicialização**: Certifique-se de que o modelo esteja sendo inicializado corretamente. Erros de inicialização podem levar a resultados inconsistentes ou NaN (Not a Number).
* **Erros de convergência**: Certifique-se de que o modelo esteja convergindo corretamente. Erros de convergência podem levar a resultados inconsistentes ou NaN.
* **Segurança**: Certifique-se de que o modelo esteja sendo treinado em um ambiente seguro. Use técnicas de criptografia e autenticação para proteger os dados e o modelo.
* **Monitoramento**: Certifique-se de que o modelo esteja sendo monitorado corretamente. Use ferramentas de monitoramento para detectar erros ou anomalias durante o treinamento.

Além disso, é importante considerar as seguintes práticas de segurança:
* **Validação de dados**: Certifique-se de que os dados sejam válidos e consistentes antes de treinar o modelo.
* **Autenticação**: Certifique-se de que apenas usuários autorizados possam acessar o modelo e os dados.
* **Criptografia**: Certifique-se de que os dados e o modelo sejam criptografados para proteger contra acessos não autorizados.
* **Backups**: Certifique-se de que os dados e o modelo sejam backups regularmente para evitar perda de dados em caso de falha.