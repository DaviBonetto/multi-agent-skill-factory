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
*   Certifique-se de que o modelo esteja corretamente compilado e que as dependências estejam instaladas.
*   Verifique se o modelo está compatível com o hardware utilizado.
*   Em caso de erros de inicialização, verifique se as variáveis de ambiente estão corretamente configuradas.
#### Edge Cases
*   **Modelos muito grandes**: Em casos onde o modelo é muito grande para caber na memória da GPU, considere utilizar o modo híbrido ou a divisão de tensor.
*   **Múltiplas GPUs**: Ao utilizar múltiplas GPUs, certifique-se de que as GPUs estejam corretamente configuradas e que o modelo esteja otimizado para utilização de múltiplas GPUs.
*   **Problemas de desempenho**: Em caso de problemas de desempenho, verifique se o modelo está otimizado para o hardware utilizado e se as configurações de inicialização estão corretas.
#### Segurança
*   **Validação de entrada**: Certifique-se de que as entradas sejam validadas corretamente para evitar ataques de injeção de código.
*   **Atualizações de segurança**: Mantenha o modelo e as dependências atualizados com as últimas atualizações de segurança.
*   **Uso de criptografia**: Considere utilizar criptografia para proteger os dados de treinamento e os modelos treinados.