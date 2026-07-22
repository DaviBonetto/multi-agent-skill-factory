---
name: hf-mem
description: Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub
---

`hf_mem` estimates the required memory for inference, including model weights and an optional KV cache, for Safetensors and GGUF for models on the Hugging Face Hub using HTTP Range requests i.e., without downloading or loading any weights locally.

## When to use?

- User asks how much VRAM or memory a model needs to run
- User wants to know if a model fits on their GPU or a given instance
- User references a Hugging Face model ID or URL and asks about inference requirements

## What are the requirements?

- `uv` installed (for `uvx`)
- `HF_TOKEN` env var or `--hf-token` flag (for gated or private models only)

## How to run?

Run with `--model-id` pointing to the Hugging Face Hub repository which will check that it either contains Safetensors (via `model.safetensors`, `model.safetensors.index.json` if sharded, or `model_index.json` for Diffusers) or GGUF model weights within.

```bash
uvx hf-mem --model-id <model-id> --json-output
```

If the repository contains GGUF model weights in multiple precisions / quantizations, the estimations will be on a per-file basis, whereas for inference you won't load all of those but rather only a single precision. This being said, for GGUF you might as well need to provide `--gguf-file` to target the specific file (or path if sharded) you want to run.

```bash
uvx hf-mem --model-id <model-id> --gguf-file <file-or-path> --json-output
```

Additionally, `hf-mem` comes with an `--experimental` flag that will also calculate the KV cache memory requirements too, useful for large-language models, meaning it applies to LLMs (`...ForCausalLM`), VLMs (`...ForConditionalGeneration`), and GGUF models.

As per the context window, it will be read from the default or overridden with `--max-model-len` a la vLLM. And, same goes for the KV cache precision, which will default to the model precision unless manually set via `--kv-cache-dtype` a la vLLM too.

For Safetensors use as:

```bash
uvx hf-mem --model-id <model-id> --experimental [--max-model-len N] [--batch-size N] [--kv-cache-dtype auto|bfloat16|fp8|fp8_ds_mla|fp8_e4m3|fp8_e5m2|fp8_inc] --json-output
```

And, for GGUF use as:

```bash
uvx hf-mem --model-id <model-id> --gguf-file <file-or-path> --experimental [--max-model-len N] [--batch-size N] [--kv-cache-dtype auto|F32|F16|Q4_0|Q4_1|Q5_0|Q5_1|Q8_0|Q8_1|Q2_K|Q3_K|Q4_K|Q5_K|Q6_K|Q8_K|IQ2_XXS|IQ2_XS|IQ3_XXS|IQ1_S|IQ4_NL|IQ3_S|IQ2_S|IQ4_XS|I8|I16|I32|I64|F64|IQ1_M|BF16|TQ1_0|TQ2_0|MXFP4] --json-output
```

## Examples

For Transformers with Safetensors weights:

```bash
uvx hf-mem --model-id MiniMaxAI/MiniMax-M2 --json-output
```

For Diffusers with Safetensors weights:

```bash
uvx hf-mem --model-id Qwen/Qwen-Image --json-output
```

For Sentence Transformers with Safetensors weights:

```bash
uvx hf-mem --model-id google/embeddinggemma-300m --json-output
```

With `--experimental` to include the KV cache estimation for LLMs and VLMs:

```bash
uvx hf-mem --model-id mistralai/Mistral-7B-v0.1 --experimental --json-output
```

And, for LLMs or VLMs with GGUF weights:

```bash
uvx hf-mem --model-id unsloth/Qwen3.5-397B-A17B-GGUF --gguf-file Q4_K_M --experimental --json-output
```

## ⚠️ Tratamento de Exceções e Edge Cases

- **Modelo não encontrado**: Se o modelo não for encontrado no Hugging Face Hub, o comando retornará um erro com uma mensagem indicando que o modelo não foi encontrado.
- **Modelo com pesos inválidos**: Se o modelo tiver pesos inválidos ou corrompidos, o comando retornará um erro com uma mensagem indicando que os pesos são inválidos.
- **Repositório com múltiplos modelos**: Se o repositório tiver múltiplos modelos, o comando retornará um erro com uma mensagem indicando que o repositório tem múltiplos modelos e solicitando que o usuário especifique o modelo desejado.
- **Parâmetros inválidos**: Se os parâmetros fornecidos forem inválidos, o comando retornará um erro com uma mensagem indicando que os parâmetros são inválidos.
- **Erro de autenticação**: Se o token de autenticação for inválido ou expirado, o comando retornará um erro com uma mensagem indicando que o token de autenticação é inválido.
- **Erro de conexão**: Se ocorrer um erro de conexão ao acessar o Hugging Face Hub, o comando retornará um erro com uma mensagem indicando que ocorreu um erro de conexão.
- **Modelo com precisão não suportada**: Se o modelo tiver uma precisão não suportada, o comando retornará um erro com uma mensagem indicando que a precisão não é suportada.
- **Tamanho do modelo muito grande**: Se o tamanho do modelo for muito grande, o comando pode retornar um erro com uma mensagem indicando que o tamanho do modelo é muito grande. Nesse caso, o usuário pode precisar ajustar o parâmetro `--max-model-len` para um valor maior.