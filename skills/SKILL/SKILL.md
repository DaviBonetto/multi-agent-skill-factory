---
name: huggingface-tool-builder
description: Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. This is especially useful when chaining or combining API calls or the task will be repeated/automated. This Skill creates a reusable script to fetch, enrich or process data.
---

# Hugging Face API Tool Builder

Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping and intermediate processing where helpful. You can access the API directly, as well as use the `hf` command line tool. Model and Dataset cards can be accessed from repositories directly.

## Script Rules

Make sure to follow these rules:
 - Scripts must take a `--help` command line argument to describe their inputs and outputs
 - Non-destructive scripts should be tested before handing over to the User
 - Shell scripts are preferred, but use Python or TSX if complexity or user need requires it.
 - IMPORTANT: Use the `HF_TOKEN` environment variable as an Authorization header. For example: `curl -H "Authorization: Bearer ${HF_TOKEN}" https://huggingface.co/api/`. This provides higher rate limits and appropriate authorization for data access.
 - Investigate the shape of the API results before commiting to a final design; make use of piping and chaining where composability would be an advantage - prefer simple solutions where possible.
 - Share usage examples once complete.
 - Handle errors and exceptions properly, including API rate limits, network errors, and invalid user input.

Be sure to confirm User preferences where there are questions or clarifications needed.

## Sample Scripts

Paths below are relative to this skill directory.

Reference examples:
- `references/hf_model_papers_auth.sh` — uses `HF_TOKEN` automatically and chains trending → model metadata → model card parsing with fallbacks; it demonstrates multi-step API usage plus auth hygiene for gated/private content.
- `references/find_models_by_paper.sh` — optional `HF_TOKEN` usage via `--token`, consistent authenticated search, and a retry path when arXiv-prefixed searches are too narrow; it shows resilient query strategy and clear user-facing help.
- `references/hf_model_card_frontmatter.sh` — uses the `hf` CLI to download model cards, extracts YAML frontmatter, and emits NDJSON summaries (license, pipeline tag, tags, gated prompt flag) for easy filtering.

Baseline examples (ultra-simple, minimal logic, raw JSON output with `HF_TOKEN` header):
- `references/baseline_hf_api.sh` — bash
- `references/baseline_hf_api.py` — python
- `references/baseline_hf_api.tsx` — typescript executable

Composable utility (stdin → NDJSON):
- `references/hf_enrich_models.sh` — reads model IDs from stdin, fetches metadata per ID, emits one JSON object per line for streaming pipelines.

Composability through piping (shell-friendly JSON output):
- `references/baseline_hf_api.sh 25 | jq -r '.[].id' | references/hf_enrich_models.sh | jq -s 'sort_by(.downloads) | reverse | .[:10]'`
- `references/baseline_hf_api.sh 50 | jq '[.[] | {id, downloads}] | sort_by(.downloads) | reverse | .[:10]'`
- `printf '%s
' openai/gpt-oss-120b meta-llama/Meta-Llama-3.1-8B | references/hf_model_card_frontmatter.sh | jq -s 'map({id, license, has_extra_gated_prompt})'`

## High Level Endpoints

The following are the main API endpoints available at `https://huggingface.co`

```
/api/datasets
/api/models
/api/spaces
/api/collections
/api/daily_papers
/api/notifications
/api/settings
/api/whoami-v2
/api/trending
/oauth/userinfo
```

## Accessing the API

The API is documented with the OpenAPI standard at `https://huggingface.co/.well-known/openapi.json`.

**IMPORTANT:** DO NOT ATTEMPT to read `https://huggingface.co/.well-known/openapi.json` directly as it is too large to process. 

**IMPORTANT** Use `jq` to query and extract relevant parts. For example, 

 Command to Get All 160 Endpoints

```bash
curl -s "https://huggingface.co/.well-known/openapi.json" | jq '.paths | keys | sort'
```

Model Search Endpoint Details

```bash
curl -s "https://huggingface.co/.well-known/openapi.json" | jq '.paths["/api/models"]'
```

You can also query endpoints to see the shape of the data. When doing so constrain results to low numbers to make them easy to process, yet representative.

## Using the HF command line tool

The `hf` command line tool gives you further access to Hugging Face repository content and infrastructure. 

```bash
❯ hf --help
Usage: hf [OPTIONS] COMMAND [ARGS]...

  Hugging Face Hub CLI

Options:
  --help                Show this message and exit.

Commands:
  auth                 Manage authentication (login, logout, etc.).
  buckets              Commands to interact with buckets.
  cache                Manage local cache directory.
  collections          Interact with collections on the Hub.
  datasets             Interact with datasets on the Hub.
  discussions          Manage discussions and pull requests on the Hub.
  download             Download files from the Hub.
  endpoints            Manage Hugging Face Inference Endpoints.
  env                  Print information about the environment.
  extensions           Manage hf CLI extensions.
  jobs                 Run and manage Jobs on the Hub.
  models               Interact with models on the Hub.
  papers               Interact with papers on the Hub.
  repos                Manage repos on the Hub.
  skills               Manage skills for AI assistants.
  spaces               Interact with spaces on the Hub.
  sync                 Sync files between local directory and a bucket.
  upload               Upload a file or a folder to the Hub.
  upload-large-folder  Upload a large folder to the Hub.
  version              Print information about the hf version.
  webhooks             Manage webhooks on the Hub.
```

The `hf` CLI command has replaced the now deprecated `huggingface-cli` command.

## ⚠️ Tratamento de Exceções e Edge Cases

Ao criar scripts para interagir com a API do Hugging Face, é importante considerar os seguintes casos de exceção e edge cases:

* **Rate limits**: A API do Hugging Face tem limites de taxa para evitar abusos. Se o script exceder esses limites, ele receberá um erro 429. Nesse caso, o script deve aguardar um tempo antes de tentar novamente.
* **Erros de rede**: Erros de rede podem ocorrer durante a execução do script. Nesse caso, o script deve tentar novamente após um tempo.
* **Entrada de usuário inválida**: O script deve validar a entrada de usuário para evitar erros. Por exemplo, se o usuário fornecer um ID de modelo inválido, o script deve retornar um erro.
* **Respostas da API inválidas**: A API do Hugging Face pode retornar respostas inválidas ou inconsistentes. Nesse caso, o script deve lidar com essas respostas de forma apropriada.
* **Timeouts**: O script deve ter timeouts para evitar que ele fique executando indefinidamente.

Para lidar com esses casos, o script pode usar técnicas como:

* **Retry**: Tentar novamente após um tempo se ocorrer um erro.
* **Validação de entrada**: Validar a entrada de usuário para evitar erros.
* **Tratamento de erros**: Lidar com erros de forma apropriada, como retornar um erro ou aguardar um tempo antes de tentar novamente.
* **Timeouts**: Estabelecer timeouts para evitar que o script fique executando indefinidamente.

Exemplo de como lidar com rate limits:
```bash
while true; do
  response=$(curl -s -H "Authorization: Bearer ${HF_TOKEN}" https://huggingface.co/api/models)
  if [ $? -eq 429 ]; then
    sleep 60
  else
    break
  fi
done
```
Esse exemplo tenta novamente após 1 minuto se ocorrer um erro 429.