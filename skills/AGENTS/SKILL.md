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
 - train-sentence-transformers -> "skills/train-sentence-transformers/SKILL.md"
 - transformers-js -> "skills/transformers-js/SKILL.md"

## Habilidades Disponíveis
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, conjuntos de dados, espaços, buckets, repositórios, trabalhos e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar buckets do Hugging Face; executar ou agendar trabalhos na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, conjuntos de dados e espaços; ler, pesquisar ou navegar por artigos acadêmicos; gerenciar coleções; consultar conjuntos de dados; configurar espaços; definir webhooks; ou implantar e gerenciar pontos de extremidade de inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou desejar fazer algo relacionado ao ecossistema do Hugging Face e à IA e ML em geral. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o comando `huggingface-cli` obsoleto."
huggingface-best: ""
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de trabalhos do HF, PRs de cartões de modelo, publicação de resultados de avaliação ou automação de avaliações da comunidade."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Visualizador de Conjuntos de Dados do Hugging Face que recuperam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet e leem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário da web e demos em Python com Gradio. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com infraestrutura de trabalhos do Hugging Face. Aborda métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de conjuntos de dados, seleção de hardware, estimativa de custo, monitoramento do Trackio, autenticação do Hub, seleção/persistência de modelo e liderança. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Aborda encontrar GGUFs, seleção de quantização, execução de servidores, busca exata de arquivos GGUF, conversão e serviço de hospedagem local compatível com OpenAI."
huggingface-paper-publisher: "Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta criar páginas de artigos, vincular artigos a modelos/conjuntos de dados, reivindicar autoria e gerar artigos de pesquisa profissionais baseados em markdown."
huggingface-papers: "Procure e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/conjuntos de dados/espacos vinculados, repositório do Github e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID do arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA."
huggingface-tool-builder: "Use essa habilidade quando o usuário deseja criar ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa Habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analizar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização de espaços do HF e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e classificadores Transformers) e segmentação SAM/SAM2 usando Transformers do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Aborda preparo de conjunto de dados no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa delimitadora/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento do Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste de modelos de visão no Hugging Face Jobs."
train-sentence-transformers: "Treine ou ajuste modelos de sentence-transformers em `SentenceTransformer` (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, dedup, multimodal), `CrossEncoder` (reranker; pontuação de pares para recuperação em duas etapas / classificação de pares) e `SparseEncoder` (SPLADE, modelo de embedding esparsa; para recuperação aprendida-esparsa). Aborda seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de ponta em JavaScript/TypeScript. Suporta tarefas de NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e multimodal. Funciona em navegadores e ambientes de execução de servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Autenticação
- **Caso de Uso:** O usuário não está autenticado no Hugging Face Hub.
- **Tratamento:** Redirecione o usuário para a página de login do Hugging Face Hub e forneça instruções sobre como se autenticar.

### Erros de Permissão
- **Caso de Uso:** O usuário não tem permissão para acessar um recurso específico.
- **Tratamento:** Exiba uma mensagem de erro informando que o usuário não tem permissão para acessar o recurso e forneça instruções sobre como solicitar permissão.

### Erros de Conexão
- **Caso de Uso:** O usuário não consegue se conectar ao Hugging Face Hub devido a problemas de rede.
- **Tratamento:** Exiba uma mensagem de erro informando que houve um problema de conexão e forneça instruções sobre como verificar a conexão de rede.

### Erros de Modelo
- **Caso de Uso:** O modelo solicitado não está disponível ou não pode ser carregado.
- **Tratamento:** Exiba uma mensagem de erro informando que o modelo não está disponível e forneça instruções sobre como selecionar um modelo alternativo.

### Outros Erros
- **Caso de Uso:** Outros erros não especificados.
- **Tratamento:** Exiba uma mensagem de erro genérica e forneça instruções sobre como relatar o problema para obter ajuda adicional.

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `hf-datasets/scripts/example.py` seria referenciado como `hf-datasets/scripts/example.py`.