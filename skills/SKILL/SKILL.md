---
name: huggingface-local-models
description: "Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. Covers finding GGUFs, quant selection, running servers, exact GGUF file lookup, conversion, and OpenAI-compatible local serving."
---

# Hugging Face Local Models

Search the Hugging Face Hub for llama.cpp-compatible GGUF repos, choose the right quant, and launch the model with `llama-cli` or `llama-server`.

## Default Workflow

1. Search the Hub with `apps=llama.cpp`.
2. Open `https://huggingface.co/<repo>?local-app=llama.cpp`.
3. Prefer the exact HF local-app snippet and quant recommendation when it is visible.
4. Confirm exact `.gguf` filenames with `https://huggingface.co/api/models/<repo>/tree/main?recursive=true`.
5. Launch with `llama-cli -hf <repo>:<QUANT>` or `llama-server -hf <repo>:<QUANT>`.
6. Fall back to `--hf-repo` plus `--hf-file` when the repo uses custom file naming.
7. Convert from Transformers weights only if the repo does not already expose GGUF files.

## Quick Start

### Install llama.cpp

```bash
brew install llama.cpp
winget install llama.cpp
```

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
make
```

### Authenticate for gated repos

```bash
hf auth login
```

### Search the Hub

```text
https://huggingface.co/models?apps=llama.cpp&sort=trending
https://huggingface.co/models?search=Qwen3.6&apps=llama.cpp&sort=trending
https://huggingface.co/models?search=<term>&apps=llama.cpp&num_parameters=min:0,max:24B&sort=trending
```

### Run directly from the Hub

```bash
llama-cli -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M
llama-server -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M
```

### Run an exact GGUF file

```bash
llama-server 
    --hf-repo unsloth/Qwen3.6-35B-A3B-GGUF 
    --hf-file Qwen3.6-35B-A3B-UD-Q4_K_M.gguf 
    -c 4096
```

### Convert only when no GGUF is available

```bash
hf download <repo-without-gguf> --local-dir ./model-src
python convert_hf_to_gguf.py ./model-src 
    --outfile model-f16.gguf 
    --outtype f16
llama-quantize model-f16.gguf model-q4_k_m.gguf Q4_K_M
```

### Smoke test a local server

```bash
llama-server -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M
```

```bash
curl http://localhost:8080/v1/chat/completions 
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer no-key" 
  -d '{
    "messages": [
      {"role": "user", "content": "Write a limerick about exception handling"}
    ]
  }'
```

## Quant Choice

- Prefer the exact quant that HF marks as compatible on the `?local-app=llama.cpp` page.
- Keep repo-native labels such as `UD-Q4_K_M` instead of normalizing them.
- Default to `Q4_K_M` unless the repo page or hardware profile suggests otherwise.
- Prefer `Q5_K_M` or `Q6_K` for code or technical workloads when memory allows.
- Consider `Q3_K_M`, `Q4_K_S`, or repo-specific `IQ` / `UD-*` variants for tighter RAM or VRAM budgets.
- Treat `mmproj-*.gguf` files as projector weights, not the main checkpoint.

## Load References

- Read [hub-discovery.md](references/hub-discovery.md) for URL-first workflows, model search, tree API extraction, and command reconstruction.
- Read [quantization.md](references/quantization.md) for format tables, model scaling, quality tradeoffs, and `imatrix`.
- Read [hardware.md](references/hardware.md) for Metal, CUDA, ROCm, or CPU build and acceleration details.

## Resources

- llama.cpp: `https://github.com/ggml-org/llama.cpp`
- Hugging Face GGUF + llama.cpp docs: `https://huggingface.co/docs/hub/gguf-llamacpp`
- Hugging Face Local Apps docs: `https://huggingface.co/docs/hub/main/local-apps`
- Hugging Face Local Agents docs: `https://huggingface.co/docs/hub/agents-local`
- GGUF converter Space: `https://huggingface.co/spaces/ggml-org/gguf-my-repo`

## ⚠️ Tratamento de Exceções e Edge Cases

- **Repos com nomes personalizados**: Se um repositório usar nomes de arquivos personalizados, certifique-se de usar `--hf-repo` e `--hf-file` para especificar o repositório e o arquivo GGUF corretos.
- **Conversão de modelos**: Se um repositório não expor arquivos GGUF, certifique-se de converter os pesos do Transformadores para GGUF usando `convert_hf_to_gguf.py`.
- **Quantização**: Se um repositório não fornecer uma recomendação de quantização, use `Q4_K_M` como padrão, a menos que o perfil de hardware sugira outra opção.
- **Erros de autenticação**: Se ocorrer um erro de autenticação ao acessar um repositório, verifique se as credenciais de autenticação estão corretas e se o repositório está configurado corretamente.
- **Erros de inicialização do servidor**: Se ocorrer um erro ao iniciar o servidor, verifique se o modelo está configurado corretamente e se os arquivos GGUF estão presentes no diretório correto.
- **Limitações de memória**: Se o modelo exigir mais memória do que está disponível, considere usar uma quantização mais baixa ou um modelo mais leve.
- **Problemas de compatibilidade**: Se ocorrer um problema de compatibilidade entre o modelo e o hardware, verifique se o modelo está configurado corretamente e se o hardware atende aos requisitos mínimos do modelo.
