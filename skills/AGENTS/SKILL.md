# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
 - hf-cli -> "skills/hf-cli/SKILL.md"
 - huggingface-community-evals -> "skills/huggingface-community-evals/SKILL.md"
 - huggingface-datasets -> "skills/huggingface-datasets/SKILL.md"
 - huggingface-gradio -> "skills/huggingface-gradio/SKILL.md"
 - huggingface-llm-trainer -> "skills/huggingface-llm-trainer/SKILL.md"
 - huggingface-paper-publisher -> "skills/huggingface-paper-publisher/SKILL.md"
 - huggingface-papers -> "skills/huggingface-papers/SKILL.md"
 - huggingface-tool-builder -> "skills/huggingface-tool-builder/SKILL.md"
 - huggingface-trackio -> "skills/huggingface-trackio/SKILL.md"
 - huggingface-vision-trainer -> "skills/huggingface-vision-trainer/SKILL.md"
 - transformers-js -> "skills/transformers-js/SKILL.md"

## Habilidades Disponíveis
### hf-cli
"Hugging Face Hub CLI (`hf`) para download, upload e gerenciamento de modelos, datasets, espaços, buckets, repositórios, papers, jobs e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Buckets do Hugging Face; executar ou agendar jobs na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, datasets e espaços; ler, pesquisar ou navegar por papers acadêmicos; gerenciar coleções; consultar datasets; configurar espaços; configurar webhooks; ou implantar e gerenciar Endpoints de Inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema do Hugging Face e ao AI e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou traces de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o `huggingface-cli` obsoleto."

### huggingface-community-evals
"Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU local e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de Jobs do HF, PRs de model-card, publicação de .eval_results ou automação de community-evals."

### huggingface-datasets
"Use essa habilidade para fluxos de trabalho da API do Dataset Viewer do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet, lêem tamanho ou estatísticas."

### huggingface-gradio
"Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."

### huggingface-llm-trainer
"Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com a infraestrutura de Jobs do Hugging Face. Aborda métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além da conversão GGUF para implantação local. Inclui orientação sobre o pacote de Jobs TRL, scripts UV com formato PEP 723, preparo e validação de datasets, seleção de hardware, estimativa de custo, monitoramento do Trackio, autenticação do Hub, seleção/leaderboards de modelo e persistência de modelo. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."

### huggingface-paper-publisher
"Publique e gerencie papers de pesquisa no Hugging Face Hub. Suporta a criação de páginas de paper, vinculação de papers a modelos/datasets, reivindicação de autoria e geração de artigos de pesquisa baseados em markdown profissionais."

### huggingface-papers
"Procure e leia páginas de paper do Hugging Face em markdown e use a API de papers para metadados estruturados, como autores, modelos/datasets/espacos vinculados, repositório do Github e página do projeto. Use quando o usuário compartilha uma URL de página de paper do Hugging Face, uma URL ou ID do arXiv ou pede para resumir, explicar ou analisar um paper de pesquisa de IA."

### huggingface-tool-builder
"Use essa habilidade quando o usuário quiser construir ferramentas/scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."

### huggingface-trackio
"Acompanhe e visualize experimentos de treinamento de ML com o Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analizar métricas registradas (CLI). Suporta visualização de dashboard em tempo real, alertas com webhooks, sincronização do HF Space e saída JSON para automação."

### huggingface-vision-trainer
"Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e qualquer classificador Transformers), e SAM/SAM2 de segmentação usando Transformers do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Aborda preparo de dataset no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento do Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."

### transformers-js
"Use Transformers.js para executar modelos de aprendizado de máquina de estado da arte diretamente em JavaScript/TypeScript. Suporta tarefas de NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de tempo de execução do servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## ⚠️ Tratamento de Exceções e Edge Cases
- **Tratamento de Erros**: Em caso de erros durante a execução de habilidades, é importante fornecer mensagens de erro claras e úteis para o usuário, indicando a causa do problema e possíveis soluções.
- **Edge Cases**: Para habilidades que lidam com dados externos, como a API do Hugging Face, é crucial considerar casos de bordo, como resposta vazia, erro de conexão, ou dados malformados, e ter um plano para lidar com essas situações de forma robusta.
- **Validação de Entrada**: Sempre valide as entradas do usuário para garantir que elas estejam no formato esperado e contenham os dados necessários para a execução da habilidade, evitando erros por falta de informação ou formato incorreto.
- **Segurança**: Ao lidar com autenticação e autorização, especialmente com a API do Hugging Face, é fundamental garantir que as credenciais do usuário sejam tratadas de forma segura, utilizando métodos de autenticação seguros e protegendo os dados do usuário contra acessos não autorizados.
- **Documentação**: Manter a documentação das habilidades atualizada e clara é essencial para o uso correto e eficaz das habilidades, além de facilitar a resolução de problemas e a melhoria contínua das habilidades.