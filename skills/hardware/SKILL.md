## Hardware Acceleration
### Apple Silicon (Metal)
```bash
make clean && make GGML_METAL=1
llama-cli -m model.gguf -ngl 99 -p "Hello"
```
### NVIDIA (CUDA)
```bash
make clean && make GGML_CUDA=1
llama-cli -m model.gguf -ngl 35 -p "Hello"
# Hybrid for large models
llama-cli -m llama-70b.Q4_K_M.gguf -ngl 20
# Multi-GPU split
llama-cli -m large-model.gguf --tensor-split 0.5,0.5 -ngl 60
```
### AMD (ROCm)
```bash
make LLAMA_HIP=1
llama-cli -m model.gguf -ngl 999
```
### CPU
```bash
# Match physical cores, not logical threads
llama-cli -m model.gguf -t 8 -p "Hello"
# BLAS acceleration
make LLAMA_OPENBLAS=1
```
### ⚠️ Tratamento de Exceções e Edge Cases
#### Erros Comuns
*   **Erro de Compilação**: Se ocorrer um erro durante a compilação, verifique se as dependências necessárias estão instaladas e se o código fonte está atualizado.
*   **Erro de Execução**: Se ocorrer um erro durante a execução, verifique se os parâmetros passados estão corretos e se o modelo está carregado corretamente.
#### Edge Cases
*   **Modelos Muito Grandes**: Para modelos muito grandes, é recomendável utilizar a opção `--tensor-split` para dividir o modelo em múltiplas GPUs.
*   **Recursos de Hardware Insuficientes**: Se os recursos de hardware forem insuficientes, é recomendável reduzir o tamanho do modelo ou utilizar um hardware mais potente.
*   **Problemas de Segurança**: Se ocorrerem problemas de segurança, como vazamento de dados ou acesso não autorizado, é recomendável verificar as permissões de acesso e implementar medidas de segurança adicionais.
#### Tratamento de Exceções
*   **Try-Except**: Utilize blocos try-except para capturar e tratar exceções que possam ocorrer durante a execução do código.
*   **Logging**: Utilize logging para registrar erros e exceções, permitindo uma análise mais detalhada dos problemas ocorridos.
Exemplo de tratamento de exceções:
```python
try:
    # Código que pode gerar exceções
    llama_cli = llama_cli.LlamaCLI()
    llama_cli.run()
except Exception as e:
    # Tratamento da exceção
    print(f"Erro: {e}")
    logging.error(f"Erro: {e}")
```
