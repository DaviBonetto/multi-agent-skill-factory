# Community GPU grants

When a non-PRO user has a good use case for ZeroGPU (open research demo, hobbyist project, educational tool, institutional showcase) and doesn't want to subscribe, they can request a free community grant from Hugging Face.

## The flow

1. **Build the Space.** Create it as `--flavor cpu-basic` (the user is not PRO, so creating with `--flavor zero-a10g` will fail at `create_repo`). Code the app for ZeroGPU anyway — `import spaces`, `@spaces.GPU`, module-scope `.to("cuda")`. The Space will technically run on CPU until the grant is approved, but it'll be ready to switch over instantly.

   In this mode you **can't iterate-with-real-inference** before the grant — the CPU Space won't actually run heavy compute. Get the app to BUILD cleanly and `RUNNING` (even if the runtime would OOM on real input), then submit.

2. **Submit a Community Tab discussion** on the Space. Title:

   ```
   Apply for a GPU community grant: <Personal|Company|Academic> project
   ```

   Pick the closest fit. Body:

   ```
   Description of the app: one paragraph on what it does + who it's for.
   Justification: one paragraph on why this should run on ZeroGPU
   (open-source, research, educational, etc.). 
   ```

   If the user didn't give you a justification, a reasonable default is "Non-PRO wants to build a public ZeroGPU app — happy to provide more context if helpful."

3. **Wait.** Open and publicly-facing applications by researchers, tinkerers, and institutions are typically approved. Approval can take days.

4. **Once approved**, the Space is moved to ZeroGPU automatically — no code change needed. The user comes back and you can iterate / refine with real GPU access.

## When to suggest this

- User is not on PRO but their use case is a clear fit for ZeroGPU (a public ML demo, not a private tool).
- The model fits in `large` (≤ 48 GB VRAM at the chosen precision).

## When NOT to suggest this

- Private / commercial / closed-source projects — push the user toward PRO instead.
- The model genuinely needs dedicated paid hardware (huge LLM, vLLM/JAX/ONNX as main model with heavy init) — `canPay=True` users can use paid flavors directly.
- The user is already PRO — they have ZeroGPU access; no grant needed.

## Posting the request programmatically

```python
from huggingface_hub import HfApi

api = HfApi(token="hf_...")
try:
    api.create_discussion(
        repo_id="<ns>/<space>",
        repo_type="space",
        title="Apply for a GPU community grant: Personal project",
        description="<description and justification>",
    )
except Exception as e:
    print(f"Error creating discussion: {e}")

## ⚠️ Tratamento de Exceções e Edge Cases

- **Erro de autenticação**: Se o token de acesso for inválido ou expirado, o usuário receberá um erro de autenticação. Nesse caso, é necessário atualizar o token e tentar novamente.
- **Erro de permissão**: Se o usuário não tiver permissão para criar discussões no repositório, ele receberá um erro de permissão. Nesse caso, é necessário verificar as permissões do usuário e conceder as permissões necessárias.
- **Erro de conexão**: Se houver um problema de conexão com o servidor, o usuário receberá um erro de conexão. Nesse caso, é necessário verificar a conexão de rede e tentar novamente.
- **Modelo muito grande**: Se o modelo for muito grande e não couber na memória do GPU, o usuário receberá um erro de memória insuficiente. Nesse caso, é necessário otimizar o modelo ou usar um GPU com mais memória.
- **Uso excessivo de recursos**: Se o usuário estiver usando excessivamente os recursos do GPU, ele pode receber um erro de uso excessivo de recursos. Nesse caso, é necessário otimizar o código e reduzir o uso de recursos.