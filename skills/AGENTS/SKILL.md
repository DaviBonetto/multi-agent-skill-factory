# SKILL
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
 - hf-cli -> "skills/hf-cli/SKILL.md"
 - hf-mem -> "skills/hf-mem/SKILL.md"
 - huggingface-best -> ""
 - huggingface-community-evals -> ""
 - huggingface-datasets -> ""
 - huggingface-gradio -> ""
 - huggingface-llm-trainer -> ""
 - huggingface-local-models -> ""
 - huggingface-lora-space-builder -> ""
 - huggingface-paper-publisher -> ""
 - huggingface-papers -> ""
 - huggingface-spaces -> ""
 - huggingface-tool-builder -> ""
 - huggingface-trackio -> ""
 - huggingface-vision-trainer -> ""
 - huggingface-zerogpu -> ""
 - train-sentence-transformers -> ""
 - transformers-js -> ""
 - trl-training -> ""

## Habilidades Disponíveis
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, datasets, espaços, buckets, repositórios, papers, jobs e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Hugging Face Buckets; executar ou agendar jobs no Hugging Face infrastructure; gerenciar Hugging Face repositórios; discussões e pull requests; navegar modelos, datasets e espaços; ler, pesquisar ou navegar papers acadêmicos; gerenciar coleções; consultar datasets; configurar espaços; definir webhooks; ou implantar e gerenciar HF Inference Endpoints. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema Hugging Face e à IA e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou rastros de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o depreciado 'huggingface-cli'."
hf-mem: "Hugging Face CLI para estimar a memória necessária para carregar pesos de modelos Safetensors ou GGUF para inferência a partir do Hugging Face Hub"
huggingface-best: ""
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU local, e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de jobs do HF, PRs de model-card, publicação de .eval_results ou automação de community-evals."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Dataset Viewer do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet, e leem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste modelos de linguagem e visão usando TRL (Transformer Reinforcement Learning) ou Unsloth com a infraestrutura de jobs do Hugging Face. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de jobs TRL, scripts UV com formato PEP 723, preparo e validação de datasets, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub e persistência de modelos. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Cobertura de encontrar GGUFs, seleção de quantização, execução de servidores, busca de arquivos GGUF exatos, conversão e servindo localmente compatível com OpenAI."
huggingface-lora-space-builder: "Crie e publique um demo Gradio no Hugging Face Spaces para um LoRA fornecido pelo usuário. Use quando alguém pede para criar, gerar, enviar ou publicar um Space, demo, aplicativo Gradio ou playground para um LoRA — incluindo LoRAs para Qwen-Image, Qwen-Image-Edit, LTX-Video, Wan, FLUX, SDXL ou outros modelos de difusão base. Também dispara quando alguém descreve um LoRA que treinou ou hospeda no Hub e deseja compartilhá-lo. Cobertura de escolha da pipeline base correta e receita de inferência 'diffusers', design de UI personalizado para a tarefa e entradas do LoRA (controle de união/multi-tarefa, edição, vídeo, imagem, etc.), respeitando as recomendações do model-card (palavras de gatilho, etapas, orientação, escala LoRA, entradas de exemplo), e envio para hardware ZeroGPU como um Space privado por padrão."
huggingface-paper-publisher: "Publique e gerencie pesquisas em papel no Hugging Face Hub. Suporta criação de páginas de papel, vinculação de papéis a modelos/datasets, reivindicação de autorias e geração de artigos de pesquisa profissionais baseados em markdown."
huggingface-papers: "Procure e leia páginas de papel do Hugging Face em markdown, e use a API de papéis para metadados estruturados, como autores, modelos/datasets/espacos vinculados, repositório GitHub e página do projeto. Use quando o usuário compartilha uma URL de página de papel do Hugging Face, uma URL ou ID arXiv, ou pede para resumir, explicar ou analisar um papel de pesquisa de IA."
huggingface-spaces: "Crie, implante e mantenha aplicativos no Hugging Face Spaces — Gradio / Docker / SDKs Estáticos, ZeroGPU e hardware dedicado, carregamento de modelos, depuração, buckets, provedores de inferência, subvenções da comunidade. Use sempre que o usuário peça para criar ou hospedar um aplicativo no Hugging Face, portar código para ZeroGPU, corrigir um Space que não constrói ou executa, ou trabalhar com 'hf spaces …', '@spaces.GPU', frontmatter do README do Space ou o pacote Python 'spaces'."
huggingface-tool-builder: "Use essa habilidade quando o usuário deseja construir ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face ajudaria. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa Habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento, ou recuperar/analizar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do Space do HF e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — mais qualquer classificador Transformers), e SAM/SAM2 segmentação usando Hugging Face Transformers em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparo de datasets no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/bola, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagens, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora, ou ajuste de modelos de visão no Hugging Face Jobs."
huggingface-zerogpu: "Demos de IA e computação de GPU com Gradio Spaces e Hugging Face Spaces ZeroGPU. Use quando escrever ou revisar código que usa '@spaces.GPU', configurar 'python_version' ou 'requirements.txt' para um Space ZeroGPU, ou lidar com restrições de código específicas do ZeroGPU — isolamento de processo baseado em pickle, semântica 'gr.State' através da fronteira do trabalhador, sem 'torch.compile' (use AoTI em vez disso), builds de roda CUDA (sem 'nvcc' no build ou runtime), tamanho grande versus xlarge, e chamadas de duração dinâmica. Certifique-se de usar essa habilidade sempre que o usuário menciona ZeroGPU, '@spaces.GPU' ou o pacote Python 'spaces', ou atinge erros de código específicos do ZeroGPU, como 'PicklingError' através da fronteira do trabalhador, 'duração ilegal' ou falhas de build de roda 'flash-attn' — mesmo quando o usuário não pede explicitamente orientação de codificação ZeroGPU. Acione em 'import spaces' ou '@spaces.GPU' no código."
train-sentence-transformers: "Treine ou ajuste modelos de sentence-transformers em 'SentenceTransformer' (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, dedup, multimodal), 'CrossEncoder' (reranker; pontuação de pares para recuperação em duas etapas / classificação de pares), e 'SparseEncoder' (SPLADE, modelo de embedding esparsa; para recuperação aprendida-esparsa). Cobertura de seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de ponta em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de execução servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."
trl-training: "Treine e ajuste modelos de linguagem de transformador usando TRL (Transformers Reinforcement Learning). Suporta SFT, DPO, GRPO, KTO, RLOO e treinamento de modelo de recompensa via comandos CLI."

## Caminhos Referenciados
Os caminhos dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets/scripts` seria referenciado como `hf-datasets/scripts/example.py`. 

## ⚠️ Tratamento de Exceções e Edge Cases
- **Tratamento de Erros**: Implemente tratamento de erros para lidar com exceções inesperadas, como erros de conexão de rede, erros de sintaxe em comandos CLI ou erros de processamento de dados.
- **Edge Cases**: Considere casos de bordo, como entrada de usuário inválida, parâmetros de comando CLI malformados ou situações de limite, como tamanhos de arquivo muito grandes ou conjuntos de dados muito grandes.
- **Validação de Entrada**: Valide a entrada do usuário para garantir que ela esteja no formato correto e dentro dos limites esperados.
- **Testes**: Implemente testes unitários e de integração para garantir que as habilidades funcionem corretamente e sejam robustas o suficiente para lidar com diferentes cenários.
- **Documentação**: Forneça documentação clara e concisa para cada habilidade, incluindo exemplos de uso, parâmetros de comando CLI e saídas esperadas.
- **Manuseio de Exceções**: Implemente um mecanismo de manuseio de exceções para lidar com erros inesperados e fornecer feedback útil ao usuário.
- **Limites de Recursos**: Considere limites de recursos, como memória, CPU e largura de banda de rede, ao implementar as habilidades.
- **Segurança**: Implemente medidas de segurança para proteger contra ataques mal-intencionados, como injeção de comandos ou ataques de força bruta.
- **Compatibilidade**: Garanta que as habilidades sejam compatíveis com diferentes plataformas e ambientes, incluindo sistemas operacionais, navegadores e versões de linguagens de programação.
