# Fine-tuning SAM2 with HF Trainer
Fine-tune SAM2.1 on a small part of the MicroMat dataset for image matting,
using the Hugging Face Trainer with a custom loss function.
...
## ⚠️ Tratamento de Exceções e Edge Cases
Para garantir a robustez do modelo, é importante tratar exceções e edge cases durante o treinamento e inferência. Aqui estão algumas estratégias implementadas:
- **Tratamento de exceções**: Durante o processamento dos itens do dataset, exceções são capturadas e impressas, permitindo que o treinamento continue com os itens restantes.
- **Verificação de dados**: Antes de realizar operações com os dados, é realizada uma verificação para garantir que os dados estejam no formato correto e contenham as informações necessárias.
- **Edge cases**: Durante a inferência, é importante considerar edge cases, como imagens com máscaras vazias ou bbox inválidas, para garantir que o modelo se comporte corretamente nessas situações.
...
