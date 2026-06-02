# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
 - hf-cli -> "skills/hf-cli/SKILL.md"
 - huggingface-best -> "skills/huggingface-best/SKILL.md"
 - huggingface-community-evals -> "skills/huggingface-community-evals/SKILL.md"
 - huggingface-datasets -> "skills/huggingface-datasets/SKILL.md"
 - huggingface-gradio -> "skills/huggingface-gradio/SKILL.md"
 - huggingface-llm-trainer -> "skills/huggingface-llm-trainer/SKILL.md"
 - huggingface-local-models -> "skills/huggingface-local-models/SKILL.md"
 - huggingface-paper-publisher -> "skills/huggingface-paper-publisher/SKILL.md"
 - huggingface-papers -> "skills/huggingface-papers/SKILL.md"
 - huggingface-tool-builder -> "skills/huggingface-tool-builder/SKILL.md"
 - huggingface-trackio -> "skills/huggingface-trackio/SKILL.md"
 - huggingface-vision-trainer -> "skills/huggingface-vision-trainer/SKILL.md"
 - huggingface-zerogpu -> "skills/huggingface-zerogpu/SKILL.md"
 - train-sentence-transformers -> "skills/train-sentence-transformers/SKILL.md"
 - transformers-js -> "skills/transformers-js/SKILL.md"

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar a tarefa.

## Habilidades Disponíveis
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, datasets, espaços, buckets, repositórios, papers, jobs e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Hugging Face Buckets; executar ou agendar jobs no Hugging Face infrastructure; gerenciar Hugging Face repositórios; discussões e pull requests; navegar modelos, datasets e espaços; ler, pesquisar ou navegar papers acadêmicos; gerenciar coleções; consultar datasets; configurar espaços; configurar webhooks; ou implantar e gerenciar HF Inference Endpoints. Certifique-se de usar essa habilidade sempre que o usuário menciona 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou deseja fazer algo relacionado ao ecossistema Hugging Face e ao AI e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou rastros de agentes. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o depreciado `huggingface-cli`."
huggingface-best: ""
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de HF Jobs, PRs de model-card, publicação de .eval_results ou automação de community-evals."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Dataset Viewer do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet e leem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Transformer Reinforcement Learning) ou Unsloth com a infraestrutura de Hugging Face Jobs. Aborda métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de datasets, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub, seleção/leaderboards de modelos e persistência de modelos. Use para tarefas que envolvem treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Aborda encontrar GGUFs, seleção de quantização, execução de servidores, busca exata de arquivos GGUF, conversão e serviço de local compatível com OpenAI."
huggingface-paper-publisher: "Publique e gerencie papers de pesquisa no Hugging Face Hub. Suporta criação de páginas de paper, vinculação de papers a modelos/datasets, reivindicação de autoria e geração de artigos de pesquisa baseados em markdown."
huggingface-papers: "Pesquise e leia páginas de paper do Hugging Face em markdown e use a API de papers para metadados estruturados, como autores, modelos/datasets/espaços vinculados, repositório GitHub e página do projeto. Use quando o usuário compartilha uma URL de página de paper do Hugging Face, uma URL ou ID arXiv ou pede para resumir, explicar ou analisar um paper de pesquisa de IA."
huggingface-tool-builder: "Use essa habilidade quando o usuário deseja construir ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analizar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização com HF Space e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — mais qualquer classificador Transformers), e SAM/SAM2 segmentação usando Hugging Face Transformers em GPUs em nuvem do Hugging Face Jobs. Aborda preparo de dataset no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa delimitadora/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagens, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."
huggingface-zerogpu: "Demonstrações de IA e computação de GPU com Gradio Spaces e Hugging Face Spaces ZeroGPU. Use quando escrever ou revisar código que usa `@spaces.GPU`, configurar `python_version` ou `requirements.txt` para um ZeroGPU Space, ou lidar com restrições de código específicas do ZeroGPU — isolamento de processo baseado em pickle, semântica `gr.State` através da fronteira do trabalhador, sem `torch.compile` (use AoTI em vez disso), builds de roda CUDA (sem `nvcc` na compilação ou tempo de execução), tamanhos grandes versus xlarge, e chamadas de duração dinâmica. Certifique-se de usar essa habilidade sempre que o usuário menciona ZeroGPU, `@spaces.GPU` ou o pacote Python `spaces`, ou encontra erros de código específicos do ZeroGPU, como `PicklingError` através da fronteira do trabalhador, `duração ilegal` ou falhas de build de roda `flash-attn` — mesmo quando o usuário não pede explicitamente orientação sobre codificação do ZeroGPU. Acione em `import spaces` ou `@spaces.GPU` no código."
train-sentence-transformers: "Treine ou ajuste finamente modelos sentence-transformers em `SentenceTransformer` (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, dedup, multimodal), `CrossEncoder` (reranker; pontuação de pares para recuperação em duas etapas / classificação de pares), e `SparseEncoder` (SPLADE, modelo de embedding esparsa; para recuperação aprendida-esparsa). Aborda seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de estado da arte diretamente em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de tempo de execução do servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## Caminhos Referenciados
Os caminhos dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets` seria referenciado como `hf-datasets/scripts/example.py`. 

## ⚠️ Tratamento de Exceções e Edge Cases
### Exceções Comuns
- **Erro de Autenticação:** Verifique se as credenciais de autenticação estão corretas e se o token de acesso está válido.
- **Erro de Conexão:** Verifique se a conexão com a internet está estável e se o servidor está respondendo.
- **Erro de Dados:** Verifique se os dados estão no formato correto e se não há erros de sintaxe.

### Edge Cases
- **Uso de Habilidades Concorrentes:** Certifique-se de que as habilidades sejam usadas de forma concorrente e não causem conflitos entre si.
- **Uso de Recursos Externos:** Certifique-se de que os recursos externos, como APIs ou bancos de dados, estejam disponíveis e respondendo corretamente.
- **Uso de Parâmetros Personalizados:** Certifique-se de que os parâmetros personalizados sejam usados corretamente e não causem erros de sintaxe ou semântica.

### Tratamento de Erros
- **Try-Except:** Use blocos try-except para capturar e tratar erros de forma elegante.
- **Logs:** Registre os erros em logs para facilitar a depuração e o diagnóstico.
- **Mensagens de Erro:** Forneça mensagens de erro claras e concisas para o usuário, indicando o que deu errado e como corrigir o problema.