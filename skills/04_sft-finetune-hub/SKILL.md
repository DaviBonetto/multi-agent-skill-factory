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

## Segurança e Conformidade
- Certifique-se de que todos os dados utilizados sejam devidamente anonimizados e estejam em conformidade com as políticas de privacidade.
- Utilize autenticação e autorização adequadas ao acessar recursos da HF.
- Mantenha seus modelos e dados atualizados e seguros.

## ⚠️ Tratamento de Exceções e Edge Cases
- **Erro de Conexão**: Em caso de falha na conexão com a infraestrutura da HF, tente reiniciar o processo de treinamento ou verifique a estabilidade da sua conexão de internet.
- **Modelo Não Convergente**: Se o modelo não convergir durante o treinamento, ajuste os hiperparâmetros ou verifique a qualidade dos dados de treinamento.
- **Exceções de Memória**: Em caso de exceções de memória, reduza o tamanho do lote ou utilize um GPU com mais memória.
- **Divergência de Modelo**: Se o modelo divergir durante o treinamento, verifique a estabilidade do otimizador e ajuste os hiperparâmetros se necessário.
- **Problemas de Dados**: Em caso de problemas com os dados, como dados faltantes ou inconsistentes, verifique a integridade dos dados e ajuste-os se necessário.
- **Limitações de Recursos**: Se você estiver enfrentando limitações de recursos, como falta de memória ou capacidade de processamento, considere utilizar recursos de nuvem mais potentes ou otimizar o uso de recursos.