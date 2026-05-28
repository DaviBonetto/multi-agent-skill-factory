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
*   **Erro de Compilação**: Verifique se as dependências necessárias estão instaladas e se o código-fonte está atualizado.
*   **Erro de Execução**: Verifique se o modelo está carregado corretamente e se os parâmetros de entrada estão válidos.
#### Edge Cases
*   **Modelos Grandes**: Para modelos muito grandes, considere usar a opção `--tensor-split` para dividir o modelo em múltiplas GPUs.
*   **Recursos Limitados**: Se os recursos de hardware forem limitados, considere reduzir o valor de `-ngl` ou `-t` para evitar erros de memória insuficiente.
*   **Compatibilidade**: Verifique a compatibilidade do modelo com o hardware e o software utilizados.
#### Segurança
*   **Validação de Entrada**: Sempre valide as entradas para evitar ataques de injeção de código malicioso.
*   **Atualização de Dependências**: Mantenha as dependências atualizadas para evitar vulnerabilidades de segurança conhecidas.
*   **Uso de Senhas Fortes**: Use senhas fortes e únicas para proteger o acesso ao sistema e aos modelos.