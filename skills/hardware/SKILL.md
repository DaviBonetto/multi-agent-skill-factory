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
#### Erros de Compilação
* Certifique-se de que o ambiente de compilação esteja configurado corretamente antes de executar os comandos `make`.
* Verifique se as dependências necessárias estão instaladas e atualizadas.
#### Erros de Execução
* Verifique se o modelo está carregado corretamente antes de executar o comando `llama-cli`.
* Certifique-se de que os parâmetros de entrada estejam corretos e dentro dos limites aceitáveis.
#### Edge Cases
* **Modelos muito grandes**: Em casos onde os modelos são muito grandes, é recomendável utilizar a opção `--tensor-split` para dividir o modelo em partes menores e processá-las em paralelo.
* **Recursos de hardware insuficientes**: Se os recursos de hardware (memória RAM, capacidade de processamento, etc.) forem insuficientes, o desempenho do modelo pode ser afetado. Nesse caso, é recomendável utilizar um hardware mais potente ou otimizar o modelo para reduzir a carga de processamento.
* **Problemas de compatibilidade**: Em casos onde há problemas de compatibilidade entre o hardware e o software, é recomendável verificar as especificações do hardware e do software para garantir que sejam compatíveis.
#### Segurança
* **Validação de entrada**: Certifique-se de que as entradas sejam validadas corretamente antes de serem processadas pelo modelo.
* **Proteção contra ataques**: Implemente medidas de segurança para proteger o modelo contra ataques, como ataques de força bruta ou ataques de injeção de código malicioso.
* **Atualizações de segurança**: Mantenha o modelo e as dependências atualizadas com as últimas atualizações de segurança para evitar vulnerabilidades conhecidas.