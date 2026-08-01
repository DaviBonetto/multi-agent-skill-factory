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

### Exceção 1: Perfil Não Existe

Se o perfil especificado não existir em `~/.aws/config`, retorne um erro claro:

> O perfil `<perfil>` não existe. Por favor, verifique se o nome do perfil está correto ou se o perfil foi configurado corretamente.

### Exceção 2: Região Não Especificada

Se a região não for especificada em nenhum lugar (nem variáveis de ambiente, nem arquivo de configuração), pergunte ao usuário:

> Não foi possível determinar a região. Por favor, especifique a região desejada.

### Exceção 3: Credenciais Inválidas

Se as credenciais forem inválidas ou expiradas, retorne um erro claro:

> As credenciais são inválidas ou expiradas. Por favor, verifique se as credenciais estão atualizadas e válidas.

### Exceção 4: Erro ao Executar Comando AWS

Se ocorrer um erro ao executar um comando AWS, retorne o erro específico:

> Erro ao executar o comando AWS: `<erro>`. Por favor, verifique se o comando está correto e se as credenciais estão válidas.

### Edge Case: Múltiplos Perfis

Se o usuário tiver múltiplos perfis configurados, certifique-se de que o perfil correto esteja sendo usado. Se o usuário não especificar um perfil, use o perfil padrão.

### Edge Case: Região Padrão

Se a região não for especificada em nenhum lugar, não use uma região padrão. Em vez disso, pergunte ao usuário para especificar a região desejada.