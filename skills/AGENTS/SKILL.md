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
 - huggingface-lora-space-builder -> "skills/huggingface-lora-space-builder/SKILL.md"
 - huggingface-paper-publisher -> "skills/huggingface-paper-publisher/SKILL.md"
 - huggingface-papers -> "skills/huggingface-papers/SKILL.md"
 - huggingface-spaces -> "skills/huggingface-spaces/SKILL.md"
 - huggingface-tool-builder -> "skills/huggingface-tool-builder/SKILL.md"
 - huggingface-trackio -> "skills/huggingface-trackio/SKILL.md"
 - huggingface-vision-trainer -> "skills/huggingface-vision-trainer/SKILL.md"
 - huggingface-zerogpu -> "skills/huggingface-zerogpu/SKILL.md"
 - train-sentence-transformers -> "skills/train-sentence-transformers/SKILL.md"
 - transformers-js -> "skills/transformers-js/SKILL.md"
 - trl-training -> "skills/trl-training/SKILL.md"

## Habilidades Disponíveis
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, datasets, espaços, buckets, repositórios, papers, jobs e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Hugging Face Buckets; executar ou agendar jobs na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, datasets e espaços; ler, buscar ou navegar por artigos acadêmicos; gerenciar coleções; consultar datasets; configurar espaços; configurar webhooks; ou implantar e gerenciar pontos de extremidade de inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema do Hugging Face e à IA e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou traces de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o depreciado 'huggingface-cli'."
huggingface-best: ""
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU local e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de jobs do HF, PRs de model-card, publicação de .eval_results ou automação de community-evals."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Dataset Viewer do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, buscam texto, aplicam filtros, baixam URLs parquet, leem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário da web e demos em Python com Gradio. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com a infraestrutura de jobs do Hugging Face. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de jobs TRL, scripts UV com formato PEP 723, preparo e validação de datasets, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub e persistência de modelo. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Cobertura de encontrar GGUFs, seleção de quantização, execução de servidores, busca de arquivos GGUF exatos, conversão e serviço local compatível com OpenAI."
huggingface-lora-space-builder: "Crie e publique um demo Gradio no Hugging Face Spaces para um LoRA fornecido pelo usuário. Use quando alguém pede para criar, gerar, enviar ou publicar um Space, demo, aplicativo Gradio ou playground para um LoRA — incluindo LoRAs para Qwen-Image, Qwen-Image-Edit, LTX-Video, Wan, FLUX, SDXL ou outros modelos de base de difusão. Também dispara quando alguém descreve um LoRA que treinou ou hospeda no Hub e deseja compartilhá-lo. Cobertura de escolha da pipeline de base certa e receita de inferência `diffusers`, design de interface de usuário personalizada para a tarefa e entradas do LoRA (controle de união/multi-tarefa, edição, vídeo, imagem, etc.), respeitando as recomendações do model-card (palavras de gatilho, etapas, orientação, escala LoRA, entradas de exemplo) e envio para hardware ZeroGPU como um Space privado por padrão."
huggingface-paper-publisher: "Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta a criação de páginas de artigos, vinculação de artigos a modelos/datasets, reivindicação de autoridade e geração de artigos de pesquisa profissionais baseados em markdown."
huggingface-papers: "Pesquise e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/datasets/espacos vinculados, repositório GitHub e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA."
huggingface-spaces: "Crie, implante e mantenha aplicativos no Hugging Face Spaces — Gradio / Docker / SDKs estáticos, ZeroGPU e hardware dedicado, carregamento de modelo, depuração, buckets, provedores de inferência, subvenções da comunidade. Use sempre que o usuário peça para criar ou hospedar um aplicativo no Hugging Face, migrar código para ZeroGPU, corrigir um Space que não constrói ou executa, ou trabalhar com `hf spaces …`, `@spaces.GPU`, frontmatter do README do Space ou o pacote Python `spaces`."
huggingface-tool-builder: "Use essa habilidade quando o usuário deseja construir ferramentas/Scripts ou realizar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analizar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do Space do HF e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — mais qualquer classificador Transformers) e segmentação SAM/SAM2 usando Transformers do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparo de conjunto de dados no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa delimitadora/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste de modelos de visão no Hugging Face Jobs."
huggingface-zerogpu: "Demos de IA e computação de GPU com Gradio Spaces e Hugging Face Spaces ZeroGPU. Use quando escrever ou revisar código que usa `@spaces.GPU`, configurar `python_version` ou `requirements.txt` para um Space ZeroGPU, ou lidar com restrições de código específicas do ZeroGPU — isolamento de processo baseado em pickle, semântica `gr.State` através da fronteira do trabalhador, sem `torch.compile` (use AoTI em vez disso), builds de roda CUDA (sem `nvcc` na compilação ou tempo de execução), dimensionamento grande versus extra grande, e chamadas de duração dinâmica. Certifique-se de usar essa habilidade sempre que o usuário mencionar ZeroGPU, `@spaces.GPU` ou o pacote Python `spaces`, ou encontrar erros de código específicos do ZeroGPU, como `PicklingError` através da fronteira do trabalhador, `duração ilegal` ou falhas de build de roda `flash-attn` — mesmo quando o usuário não pede explicitamente orientação sobre codificação ZeroGPU. Dispara em `import spaces` ou `@spaces.GPU` no código."
train-sentence-transformers: "Treine ou ajuste modelos de sentence-transformers em `SentenceTransformer` (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, deduplicação, multimodal), `CrossEncoder` (reranker; pontuação de par para classificação de par/pesquisa de dois estágios) e `SparseEncoder` (SPLADE, modelo de embedding esparsa; para recuperação de aprendizado esparsa). Cobertura de seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de ponta em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos) e áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de execução de servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."
trl-training: "Treine e ajuste modelos de linguagem de transformador usando TRL (Aprendizado de Reforço de Transformador). Suporta SFT, DPO, GRPO, KTO, RLOO e treinamento de modelo de recompensa via comandos CLI."

## Caminhos Referenciados
Os caminhos dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets/scripts` seria referenciado como `hf-datasets/scripts/example.py`.

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Autenticação
- **Caso de Uso:** O usuário não está autenticado no Hugging Face Hub.
- **Ação:** Redirecione o usuário para a página de login do Hugging Face Hub e forneça instruções sobre como se autenticar.

### Erros de Permissão
- **Caso de Uso:** O usuário não tem permissão para acessar um recurso específico no Hugging Face Hub.
- **Ação:** Informe o usuário sobre as permissões necessárias e forneça instruções sobre como solicitá-las.

### Erros de Conexão
- **Caso de Uso:** O usuário está enfrentando problemas de conexão com o Hugging Face Hub.
- **Ação:** Forneça dicas de solução de problemas para conexão, como verificar a conexão de internet e tentar novamente.

### Erros de Modelo
- **Caso de Uso:** O modelo solicitado pelo usuário não está disponível ou não pode ser carregado.
- **Ação:** Informe o usuário sobre o problema e forneça alternativas, como modelos semelhantes ou opções de treinamento personalizado.

### Outros Erros
- **Caso de Uso:** O usuário enfrenta um erro não especificado.
- **Ação:** Forneça uma mensagem de erro genérica e solicite que o usuário forneça mais detalhes para ajudar a resolver o problema.

Essas são apenas algumas das exceções e casos de bordo que podem ser tratados. É importante continuar a monitorar e atualizar a lista à medida que mais casos surgem.