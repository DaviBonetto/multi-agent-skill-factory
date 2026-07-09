# Production Defaults — What and Why
These defaults turn a working demo into something you can leave running. They favor "you'll find out about problems" over "absolute minimum cost". Tune any of them away if needed — the deployment script should be the starting point, not bare `create_endpoint`.
## Autoscaling — enabled, target tracking on invocations
| Setting | Default | Why |
|---|---|---|
| `MinCapacity` | 1 | Keep one warm. Min=0 enables scale-to-zero but adds cold-start latency on every gap. |
| `MaxCapacity` | 4 | Cap on scale-out. Raise for known peaks. |
| Target metric | `SageMakerVariantInvocationsPerInstance` | Scales on actual request load, not noisy GPU/CPU. |
| Target value | 20 invocations/min/instance | Conservative. Tune to model latency: faster model = higher target. |
| `ScaleInCooldown` | 300s | Long enough to avoid flapping. |
| `ScaleOutCooldown` | 60s | Scale out faster than in — under spikes, you want capacity now. |
For LLMs, the right target depends heavily on latency. A 100ms model handles 600/min easily; a 5s model maxes at ~12/min. 20 is a safe default for typical LLM latencies.
For embeddings (TEI), each request is much faster — typically <100ms on CPU and <20ms on GPU. The default of 20 will autoscale far too aggressively and waste money. Use `--target-invocations-per-instance 100–500` for embedding deployments. Rule of thumb: target ≈ 60 / (typical request latency in seconds).
## CloudWatch alarms — 3 by default
- **`ModelLatency` p99 > 30s for 5min** — slow inference, runaway requests, model loading issues.
- **`Invocation5XXErrors` sum > 5 in 5min** — container crashes, OOM, ping failures.
- **`OverheadLatency` p99 > 2s for 5min** — SageMaker platform issues, separate from model.
Without `--sns-alarm-topic`, alarms exist but don't notify. The deploy script warns when this happens.
## Data capture — disabled (opt-in via `--enable-data-capture`)
Useful for debugging "why did the model say that?" weeks later, building eval datasets, and audit trails for sensitive domains. But it creates ongoing S3 costs the user didn't necessarily ask for and stores data they may not realize is being kept — opt-in is the right default.
When enabled: 100% sampling, both input and output captured. URI defaults to `s3://sagemaker-<region>-<account>/<endpoint>/data-capture/`. Execution role needs write access to this prefix — if IAM was scoped narrowly to the model bucket, capture fails silently.
## Resource tagging
| Tag | Value |
|---|---|
| `Project` | User-supplied or model name |
| `Owner` | Caller ARN's user/email portion |
| `Environment` | `dev` (default) |
| `CreatedBy` | `agentic-deploy-skills` |
| `ModelArtifact` | S3 URI of the model |
`CreatedBy` matters most — `aws resourcegroupstaggingapi get-resources --tag-filters Key=CreatedBy,Values=agentic-deploy-skills` finds every resource these skills created.
## Endpoint naming
`<model-name>-<YYYYMMDD-HHMM>` by default. Timestamped names enable blue-green-ish iteration (bring up new, validate, delete old). Override with `--endpoint-name` if you have naming conventions.
## Not defaulted (need user input)
- **VPC config** — needs VPC ID + subnets
- **KMS encryption** — needs a specific key
- **Multi-variant endpoints** — uncommon enough that defaulting adds complexity
- **Async inference config** — different deployment pathway entirely
## Teardown
`python3 scripts/teardown.py <endpoint-name>` deletes endpoint → endpoint config → model in safe order. Autoscaling targets and alarms cleaned up separately. Data capture S3 objects are NOT deleted — that's the user's call.
## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Configuração
- Verifique se o arquivo de configuração está correto e completo.
- Certifique-se de que as credenciais de acesso estão válidas e configuradas corretamente.
### Erros de Rede
- Verifique a conectividade de rede e certifique-se de que o endpoint está acessível.
- Use ferramentas de diagnóstico de rede para identificar problemas de conectividade.
### Erros de Modelo
- Verifique se o modelo está treinado e pronto para uso.
- Certifique-se de que o modelo está configurado corretamente e que as dependências estão instaladas.
### Erros de Autoscaling
- Verifique se o autoscaling está configurado corretamente e se os limites estão definidos.
- Certifique-se de que o autoscaling está funcionando corretamente e que os recursos estão sendo escalados conforme necessário.
### Erros de Data Capture
- Verifique se o data capture está configurado corretamente e se os dados estão sendo coletados.
- Certifique-se de que os dados estão sendo armazenados corretamente e que os acessos estão controlados.
### Edge Cases
- **Modelo com alta latência**: ajuste o target de invocações por instância para evitar sobrecarga.
- **Requisições com grande volume de dados**: ajuste o tamanho do buffer de entrada para evitar erros de processamento.
- **Erros de autenticação**: verifique as credenciais de acesso e certifique-se de que as políticas de segurança estão configuradas corretamente.