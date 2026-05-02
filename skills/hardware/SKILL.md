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
Antes de executar os comandos, certifique-se de que:
- O ambiente de desenvolvimento esteja configurado corretamente.
- As dependências necessárias estejam instaladas.
- Os modelos de linguagem estejam baixados e configurados corretamente.
**Tratamento de Erros Comuns:**
*   **Erro de Compilação:** Verifique se o código fonte está atualizado e se as dependências estão corretas.
*   **Erro de Execução:** Verifique se o modelo de linguagem está carregado corretamente e se os parâmetros de entrada estão válidos.
*   **Erro de Memória Insuficiente:** Aumente a quantidade de memória disponível ou otimize o uso de memória do modelo.
**Edge Cases:**
*   **Modelos de Linguagem Grandes:** Para modelos de linguagem muito grandes, considere usar a opção de split de tensor para distribuir o processamento entre múltiplas GPUs.
*   **Entradas de Tamanho Variável:** Ajuste o parâmetro `-ngl` de acordo com o tamanho da entrada para garantir o processamento eficiente.
*   **Ambientes de Desenvolvimento Diferentes:** Ajuste as configurações de compilação e execução de acordo com as especificações do ambiente de desenvolvimento.
**Segurança:**
*   **Atualize Regularmente:** Mantenha o código fonte e as dependências atualizados para garantir a segurança e evitar vulnerabilidades conhecidas.
*   **Use Autenticação:** Quando necessário, use autenticação para proteger o acesso aos modelos de linguagem e aos dados de treinamento.
*   **Monitore o Uso de Recursos:** Monitore o uso de recursos do sistema para detectar possíveis abusos ou ataques de força bruta.