---
name: hf-cloud-aws-context-discovery
description: Discover the user's local AWS context (active profile, region, account ID, caller identity) at the start of any AWS task. Use this skill before any other AWS work — deploying to SageMaker, creating resources, calling AWS APIs, or anything that touches an AWS account. Use it especially when the user has not specified a region or profile explicitly, when they say things like "use my AWS account", "deploy to AWS", "use my profile", or when about to make any AWS CLI or SDK call. Never guess the region or account ID — always use this skill to read it from the local configuration first.
---

# AWS Context Discovery

Before doing any AWS work, read the user's local AWS config. Don't guess the region, and don't ask the user for things their config already answers.

## What to Discover

Run these at the start of the AWS work and remember the results for the rest of the session.

### 1. Active Profile

`AWS_PROFILE` env var, else `default`. If the user mentioned a profile in their prompt, that overrides. If the named profile doesn't exist in `~/.aws/config`, surface that clearly.

### 2. Region

Resolution order — stop at the first one that produces a value:
1. Region the user explicitly named in this conversation
2. `AWS_REGION` env var
3. `AWS_DEFAULT_REGION` env var
4. `region` field on the active profile in `~/.aws/config`
5. Ask the user — but only after the first four have failed

Do not fall back to `us-east-1` or any other hardcoded default.

### 3. Credentials, Account ID, Caller ARN

```bash
aws sts get-caller-identity --profile <profile> --region <region>
```

Three purposes in one call: confirms credentials are valid (stop if not), returns the `Account` ID (needed for ARN construction), returns the `Arn` of the caller.

### 4. Identify SSO / Assumed-Role Principals

The `Arn` field tells you what kind of principal this is. The pattern matters because it determines what IAM operations the caller can do.

| ARN Pattern | Type | IAM Write Capability |
|---|---|---|
| `arn:aws:iam::<acct>:user/<name>` | IAM user | Depends on attached policies |
| `arn:aws:sts::<acct>:assumed-role/AWSReservedSSO_<...>/<email>` | **SSO assumed-role** | Typically **none** — can't create/modify IAM roles |
| `arn:aws:sts::<acct>:assumed-role/<role>/<session>` | Regular assumed-role | Depends on the role |

**If the caller is SSO**, surface this immediately before later skills hit `iam:CreateRole` and fail:

> Heads up: you're authenticated via SSO (`AWSReservedSSO_<PermissionSet>_...`). SSO principals usually can't create IAM roles directly. If we need a SageMaker execution role, I'll look for an existing one first — if none exists, you'll need to ask whoever manages your AWS access to create one.

This is the highest-leverage thing this skill does. Surfacing it now turns a confusing mid-deployment error into a five-second conversation.

## Commands to Run

```bash
# Effective profile and region (faster than parsing config files)
aws configure list

# Validate credentials and get identity
aws sts get-caller-identity
aws sts get-caller-identity --profile <profile-name>  # if a profile was named
```

`aws configure list` handles env-var overrides and shows the resolved effective values. Prefer it over parsing `~/.aws/config` yourself. If you need to read raw config (e.g. to list profiles), `~/.aws/config` and `~/.aws/credentials` are plain INI files — read-only.

## What to Report Back

One or two lines, not a wall of text:

> Working with profile `my-profile` in `eu-west-1`, account `123456789012`. You're authenticated via SSO, so we'll need to use an existing IAM role rather than create one.

Don't ask the user to confirm the region you just read from their config — they configured it; that is the confirmation.

If something is wrong (credentials expired, profile doesn't exist, no region anywhere), stop and surface the specific error before continuing.

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções de Credenciais

- **Credenciais Expiradas**: Se as credenciais do usuário estiverem expiradas, o comando `aws sts get-caller-identity` falhará. Nesse caso, é necessário solicitar que o usuário atualize suas credenciais antes de continuar.
- **Credenciais Inválidas**: Se as credenciais forem inválidas (por exemplo, se a chave de acesso ou a chave secreta estiverem incorretas), o comando `aws sts get-caller-identity` também falhará. É necessário solicitar que o usuário verifique e corrija suas credenciais.

### Exceções de Perfil

- **Perfil Não Existe**: Se o perfil especificado pelo usuário não existir em `~/.aws/config`, é necessário informar ao usuário que o perfil não existe e solicitar que ele forneça um perfil válido.
- **Perfil Vazio**: Se o perfil estiver vazio ou não contiver as informações necessárias, é necessário solicitar que o usuário verifique e complete as informações do perfil.

### Exceções de Região

- **Região Não Especificada**: Se o usuário não especificar uma região e nenhuma região for encontrada nas variáveis de ambiente ou no arquivo de configuração, é necessário solicitar que o usuário forneça uma região válida.
- **Região Inválida**: Se a região especificada for inválida, é necessário informar ao usuário que a região é inválida e solicitar que ele forneça uma região válida.

### Outros Edge Cases

- **SSO com Permissões Insuficientes**: Se o usuário estiver autenticado via SSO e não tiver permissões suficientes para realizar a ação desejada, é necessário informar ao usuário sobre as limitações de permissão e orientá-lo sobre como obter as permissões necessárias.
- **Problemas de Conexão**: Se houver problemas de conexão com o AWS (por exemplo, problemas de rede ou servidores AWS indisponíveis), é necessário informar ao usuário sobre o problema e sugerir soluções alternativas ou espera até que o problema seja resolvido.