# SKILL
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

## Habilidades Disponíveis
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, datasets, espaços, buckets, repositórios, papers, jobs e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Hugging Face Buckets; executar ou agendar jobs no Hugging Face infrastructure; gerenciar Hugging Face repositórios; discussões e pull requests; navegar por modelos, datasets e espaços; ler, buscar ou navegar por papers acadêmicos; gerenciar coleções; consultar datasets; configurar espaços; configurar webhooks; ou implantar e gerenciar HF Inference Endpoints. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema Hugging Face e ao AI e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou traços de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o depreciado huggingface-cli."
huggingface-best: ""
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de HF Jobs, PRs de model-card, publicação de .eval_results ou automação de community-evals."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Dataset Viewer do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, buscam texto, aplicam filtros, baixam URLs parquet, lêem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Transformer Reinforcement Learning) ou Unsloth com infraestrutura de Hugging Face Jobs. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparação e validação de datasets, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub, seleção/leaderboards de modelos e persistência de modelos. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Cobertura de busca de GGUFs, seleção de quantização, execução de servidores, busca de arquivos GGUF exatos, conversão e servindo local compatível com OpenAI."
huggingface-paper-publisher: "Publique e gerencie papers de pesquisa no Hugging Face Hub. Suporta criação de páginas de papers, vinculação de papers a modelos/datasets, reivindicação de autoria e geração de artigos de pesquisa profissionais baseados em markdown."
huggingface-papers: "Procure e leia páginas de papers do Hugging Face em markdown e use a API de papers para metadados estruturados, como autores, modelos/datasets/espaços vinculados, repositório Github e página do projeto. Use quando o usuário compartilha uma URL de página de paper do Hugging Face, uma URL ou ID arXiv ou pede para resumir, explicar ou analisar um paper de pesquisa de IA."
huggingface-tool-builder: "Use essa habilidade quando o usuário quiser construir ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analisar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização de HF Space e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — mais qualquer classificador Transformers), e SAM/SAM2 segmentação usando Hugging Face Transformers em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparação de datasets no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/bola, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagens, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."
huggingface-zerogpu: "Demonstrações de IA e computação de GPU com Gradio Spaces e Hugging Face Spaces ZeroGPU. Use quando escrever ou revisar código que usa `@spaces.GPU`, configurar `python_version` ou `requirements.txt` para um ZeroGPU Space, ou lidar com restrições de código específicas do ZeroGPU — isolamento de processo baseado em pickle, semântica `gr.State` através da fronteira do trabalhador, sem `torch.compile` (use AoTI em vez disso), builds de roda CUDA (sem `nvcc` na compilação ou tempo de execução), tamanho grande versus xlarge, e chamadas de duração dinâmica. Certifique-se de usar essa habilidade sempre que o usuário mencionar ZeroGPU, `@spaces.GPU` ou o pacote Python `spaces`, ou encontrar erros de código específicos do ZeroGPU, como `PicklingError` através da fronteira do trabalhador, `duração ilegal` ou falhas de build de roda `flash-attn` — mesmo quando o usuário não pede explicitamente orientação sobre codificação ZeroGPU. Acione em `import spaces` ou `@spaces.GPU` no código."
train-sentence-transformers: "Treine ou ajuste finamente modelos de sentence-transformers em `SentenceTransformer` (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, deduplicação, multimodal), `CrossEncoder` (reranker; pontuação de pares para recuperação em duas etapas / classificação de pares), e `SparseEncoder` (SPLADE, modelo de embedding esparsa; para recuperação aprendida-esparsa). Cobertura de seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de última geração diretamente em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de tempo de execução do servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## Caminhos Referenciados
Os caminhos dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets` seria referenciado como `hf-datasets/scripts/example.py`. 

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erro de Autenticação**: Em caso de erro de autenticação, verifique se as credenciais estão corretas e se o token de acesso está válido.
- **Erro de Conexão**: Em caso de erro de conexão, verifique se a conexão com a internet está estável e se o servidor está respondendo.
- **Erro de Dados**: Em caso de erro de dados, verifique se os dados estão no formato correto e se não há dados faltantes.

### Edge Cases
- **Uso de Habilidades**: Em caso de uso de habilidades não documentadas, verifique se a habilidade está disponível e se há documentação disponível.
- **Parâmetros Inválidos**: Em caso de parâmetros inválidos, verifique se os parâmetros estão no formato correto e se não há parâmetros faltantes.
- **Respostas Inesperadas**: Em caso de respostas inesperadas, verifique se a resposta está no formato correto e se não há erros de processamento.

### Exceções
- **Exceção de Autenticação**: Em caso de exceção de autenticação, verifique se as credenciais estão corretas e se o token de acesso está válido.
- **Exceção de Conexão**: Em caso de exceção de conexão, verifique se a conexão com a internet está estável e se o servidor está respondendo.
- **Exceção de Dados**: Em caso de exceção de dados, verifique se os dados estão no formato correto e se não há dados faltantes.

### Melhorias
- **Documentação**: Melhore a documentação das habilidades e dos parâmetros para evitar erros de uso.
- **Testes**: Realize testes regulares para garantir que as habilidades estejam funcionando corretamente.
- **Feedback**: Forneça feedback claro e conciso em caso de erros ou exceções para ajudar os usuários a resolver os problemas.