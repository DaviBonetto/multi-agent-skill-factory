# Saving Results to Hugging Face Hub
**⚠️ CRITICAL:** Job environments are ephemeral. ALL results are lost when a job completes unless persisted to the Hub or external storage.
...
## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros de Autenticação
Verifique se o token de autenticação é válido e se o usuário tem permissão para realizar a operação.
```python
try:
    api = HfApi(token=os.environ.get("HF_TOKEN"))
    api.upload_file("results.json", "results.json", "username/results", repo_type="dataset")
except Exception as e:
    print(f"Erro ao realizar upload: {e}")
```
...