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

## Segurança

Para garantir a segurança dos modelos e dos dados, é importante seguir as melhores práticas de segurança, incluindo:
- Utilizar autenticação e autorização adequadas para acessar os recursos do HF Jobs
- Utilizar criptografia para proteger os dados em trânsito e em repouso
- Realizar testes de segurança regulares para identificar vulnerabilidades

## ⚠️ Tratamento de Exceções e Edge Cases

Ao trabalhar com o `hf-llm-trainer`, é importante considerar os seguintes casos de exceção e edge cases:
- **Erros de conexão**: Em caso de erros de conexão com o HF Jobs, o agente deve tentar reconectar após um período de tempo razoável.
- **Erros de autenticação**: Em caso de erros de autenticação, o agente deve solicitar as credenciais novamente e tentar autenticar-se novamente.
- **Erros de processamento**: Em caso de erros de processamento, o agente deve registrar o erro e continuar com a próxima tarefa.
- **Modelos inválidos**: Em caso de modelos inválidos, o agente deve registrar o erro e solicitar um novo modelo.
- **Dados inválidos**: Em caso de dados inválidos, o agente deve registrar o erro e solicitar novos dados.
- **Timeouts**: Em caso de timeouts, o agente deve registrar o erro e tentar novamente após um período de tempo razoável.
- **Limites de recursos**: Em caso de limites de recursos, o agente deve registrar o erro e solicitar mais recursos.

Exemplos de código para tratamento de exceções:
```python
try:
    # Código que pode gerar exceção
except Exception as e:
    # Tratamento da exceção
    print(f"Erro: {e}")
    # Registro do erro
    logging.error(f"Erro: {e}")
```
Exemplos de código para edge cases:
```python
if modelo_invalido:
    # Tratamento do modelo inválido
    print("Modelo inválido")
    # Registro do erro
    logging.error("Modelo inválido")
