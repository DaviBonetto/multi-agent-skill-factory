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
* **Erro de Compilação**: Certifique-se de que o ambiente de compilação esteja configurado corretamente e que as dependências necessárias estejam instaladas. Em caso de erros de compilação, verifique os logs de compilação para identificar a causa raiz do problema.
* **Incompatibilidade de Hardware**: Verifique se o hardware utilizado é compatível com a aceleração de hardware escolhida (Metal, CUDA, ROCm, etc.). Em caso de incompatibilidade, escolha uma opção de aceleração de hardware alternativa.
* **Modelos Grandes**: Ao trabalhar com modelos grandes, é importante considerar a capacidade de memória disponível no hardware. Em caso de falta de memória, considere utilizar técnicas de otimização de memória, como a divisão de tensores.
* **Erros de Execução**: Em caso de erros de execução, verifique os logs de execução para identificar a causa raiz do problema. Além disso, certifique-se de que as dependências necessárias estejam instaladas e configuradas corretamente.
* **Segurança**: Ao trabalhar com aceleração de hardware, é importante considerar a segurança do sistema. Certifique-se de que as permissões de acesso sejam configuradas corretamente e que os dados sejam protegidos contra acessos não autorizados.
* **Otimização de Desempenho**: Para otimizar o desempenho da aceleração de hardware, considere utilizar técnicas de otimização, como a utilização de threads paralelos, a otimização de memória e a utilização de algoritmos eficientes. Além disso, certifique-se de que o hardware esteja configurado corretamente e que as dependências necessárias estejam instaladas.