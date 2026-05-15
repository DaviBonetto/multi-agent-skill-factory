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
*   **Erro de Compilação**: Certifique-se de que as dependências necessárias estejam instaladas e configuradas corretamente. Verifique se o comando `make` está sendo executado com as opções corretas.
*   **Erro de Execução**: Verifique se o modelo está sendo carregado corretamente e se os parâmetros de entrada estão válidos. Use a opção `-p` para especificar a entrada correta.
*   **Erro de Memória**: Ajuste o parâmetro `-ngl` para evitar problemas de memória insuficiente. Verifique se o modelo está sendo executado em um dispositivo com recursos suficientes.
#### Edge Cases
*   **Modelos Grandes**: Para modelos muito grandes, considere usar a opção `--tensor-split` para dividir o modelo em partes menores e processá-las em paralelo.
*   **Multi-GPU**: Ao usar múltiplas GPUs, certifique-se de que as GPUs estejam configuradas corretamente e que o modelo esteja sendo executado com a opção `--tensor-split` para aproveitar ao máximo os recursos disponíveis.
*   **CPU**: Ao executar em CPU, ajuste o parâmetro `-t` para corresponder ao número de núcleos físicos disponíveis. Isso ajudará a otimizar o desempenho.
#### Segurança
*   **Validação de Entrada**: Sempre valide a entrada do usuário para evitar ataques de injeção de comandos ou outros tipos de ataques mal-intencionados.
*   **Atualização de Dependências**: Mantenha as dependências atualizadas para garantir que você tenha as últimas correções de segurança e melhorias de desempenho.
*   **Uso de Senhas Fortes**: Use senhas fortes e únicas para proteger o acesso ao sistema e aos modelos de machine learning.