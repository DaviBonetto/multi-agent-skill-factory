---
name: huggingface-datasets
description: Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics.
---

# Hugging Face Dataset Viewer

Use this skill to execute read-only Dataset Viewer API calls for dataset exploration and extraction.

## Core workflow

1. Optionally validate dataset availability with `/is-valid`.
2. Resolve `config` + `split` with `/splits`.
3. Preview with `/first-rows`.
4. Paginate content with `/rows` using `offset` and `length` (max 100).
5. Use `/search` for text matching and `/filter` for row predicates.
6. Retrieve parquet links via `/parquet` and totals/metadata via `/size` and `/statistics`.

## Defaults

- Base URL: `https://datasets-server.huggingface.co`
- Default API method: `GET`
- Query params should be URL-encoded.
- `offset` is 0-based.
- `length` max is usually `100` for row-like endpoints.
- Gated/private datasets require `Authorization: Bearer <HF_TOKEN>`.

## Dataset Viewer

- `Validate dataset`: `/is-valid?dataset=<namespace/repo>`
- `List subsets and splits`: `/splits?dataset=<namespace/repo>`
- `Preview first rows`: `/first-rows?dataset=<namespace/repo>&config=<config>&split=<split>`
- `Paginate rows`: `/rows?dataset=<namespace/repo>&config=<config>&split=<split>&offset=<int>&length=<int>`
- `Search text`: `/search?dataset=<namespace/repo>&config=<config>&split=<split>&query=<text>&offset=<int>&length=<int>`
- `Filter with predicates`: `/filter?dataset=<namespace/repo>&config=<config>&split=<split>&where=<predicate>&orderby=<sort>&offset=<int>&length=<int>`
- `List parquet shards`: `/parquet?dataset=<namespace/repo>`
- `Get size totals`: `/size?dataset=<namespace/repo>`
- `Get column statistics`: `/statistics?dataset=<namespace/repo>&config=<config>&split=<split>`
- `Get Croissant metadata (if available)`: `/croissant?dataset=<namespace/repo>`

Pagination pattern:

```bash
curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=0&length=100"
curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=100&length=100"
```

When pagination is partial, use response fields such as `num_rows_total`, `num_rows_per_page`, and `partial` to drive continuation logic.

Search/filter notes:

- `/search` matches string columns (full-text style behavior is internal to the API).
- `/filter` requires predicate syntax in `where` and optional sort in `orderby`.
- Keep filtering and searches read-only and side-effect free.

## Querying Datasets

Use `npx parquetlens` with Hub parquet alias paths for SQL querying.

Parquet alias shape:

```text
hf://datasets/<namespace>/<repo>@~parquet/<config>/<split>/<shard>.parquet
```

Derive `<config>`, `<split>`, and `<shard>` from Dataset Viewer `/parquet`:

```bash
curl -s "https://datasets-server.huggingface.co/parquet?dataset=cfahlgren1/hub-stats" 
  | jq -r '.parquet_files[] | "hf://datasets/\(.dataset)@~parquet/\(.config)/\(.split)/\(.filename)"'
```

Run SQL query:

```bash
npx -y -p parquetlens -p @parquetlens/sql parquetlens 
  "hf://datasets/<namespace>/<repo>@~parquet/<config>/<split>/<shard>.parquet" 
  --sql "SELECT * FROM data LIMIT 20"
```

### SQL export

- CSV: `--sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.csv' (FORMAT CSV, HEADER, DELIMITER ',')"`
- JSON: `--sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.json' (FORMAT JSON)"`
- Parquet: `--sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.parquet' (FORMAT PARQUET)"`

## Creating and Uploading Datasets

Use one of these flows depending on dependency constraints.

Zero local dependencies (Hub UI):

- Create dataset repo in browser: `https://huggingface.co/new-dataset`
- Upload parquet files in the repo "Files and versions" page.
- Verify shards appear in Dataset Viewer:

```bash
curl -s "https://datasets-server.huggingface.co/parquet?dataset=<namespace>/<repo>"
```

Low dependency CLI flow (`npx @huggingface/hub` / `hfjs`):

- Set auth token:

```bash
export HF_TOKEN=<your_hf_token>
```

- Upload parquet folder to a dataset repo (auto-creates repo if missing):

```bash
npx -y @huggingface/hub upload datasets/<namespace>/<repo> ./local/parquet-folder data
```

- Upload as private repo on creation:

```bash
npx -y @huggingface/hub upload datasets/<namespace>/<repo> ./local/parquet-folder data --private
```

After upload, call `/parquet` to discover `<config>/<split>/<shard>` values for querying with `@~parquet`.

## ⚠️ Tratamento de Exceções e Edge Cases

### Erros de Autenticação

- Verifique se o token de autenticação está correto e não expirou.
- Certifique-se de que o token de autenticação está sendo passado corretamente nos headers da requisição.

### Erros de Paginação

- Verifique se o `offset` e `length` estão dentro dos limites permitidos.
- Certifique-se de que o `offset` é 0-based.

### Erros de Busca e Filtro

- Verifique se a sintaxe da busca e do filtro está correta.
- Certifique-se de que os campos de busca e filtro estão corretos.

### Erros de Conexão

- Verifique se a conexão com o servidor está estabelecida corretamente.
- Certifique-se de que o servidor está respondendo corretamente.

### Edge Cases

- Verifique se o conjunto de dados está vazio ou não existe.
- Certifique-se de que o conjunto de dados está sendo processado corretamente.
- Verifique se o tamanho do conjunto de dados está dentro dos limites permitidos.
- Certifique-se de que o conjunto de dados está sendo carregado corretamente.

### Tratamento de Exceções

- Implemente try-catch para capturar exceções e erros.
- Verifique se as exceções e erros estão sendo tratados corretamente.
- Certifique-se de que as exceções e erros estão sendo logados corretamente.

### Testes

- Implemente testes unitários e de integração para verificar a funcionalidade do código.
- Verifique se os testes estão sendo executados corretamente.
- Certifique-se de que os testes estão cobrindo todos os cenários possíveis.
