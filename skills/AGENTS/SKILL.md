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
 - transformers-js -> "skills/transformers-js/SKILL.md"

## Habilidades Disponíveis
### hf-cli
"Hugging Face Hub CLI (`hf`) para download, upload e gerenciamento de modelos, conjuntos de dados, espaços, buckets, repositórios, trabalhos e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar buckets do Hugging Face; executar ou agendar trabalhos na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, conjuntos de dados e espaços; ler, pesquisar ou navegar por artigos acadêmicos; gerenciar coleções; consultar conjuntos de dados; configurar espaços; configurar webhooks; ou implantar e gerenciar pontos de extremidade de inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema do Hugging Face e ao AI e ML em geral. Use também para necessidades de armazenamento em nuvem, como checkpoints de treinamento, pipelines de dados ou rastros de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o `huggingface-cli` obsoleto."

### huggingface-best
>

### huggingface-community-evals
"Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU local e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de trabalhos do HF, PRs de cartões de modelo, publicação de resultados de avaliação ou automação de avaliações da comunidade."

### huggingface-datasets
"Use essa habilidade para fluxos de trabalho da API do Visualizador de Conjuntos de Dados do Hugging Face que recuperam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet, leem tamanho ou estatísticas."

### huggingface-gradio
"Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."

### huggingface-llm-trainer
"Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com a infraestrutura de trabalhos do Hugging Face. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de conjuntos de dados, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub, seleção/leaderboards de modelo e persistência de modelo. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."

### huggingface-local-models
"Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Cobertura de encontrar GGUFs, seleção de quantização, execução de servidores, busca de arquivo GGUF exato, conversão e serviço de local compatível com OpenAI."

### huggingface-paper-publisher
"Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta a criação de páginas de artigos, vinculação de artigos a modelos/conjuntos de dados, reivindicação de autoria e geração de artigos de pesquisa profissionais baseados em markdown."

### huggingface-papers
"Procure e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/conjuntos de dados/espacos vinculados, repositório Github e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA."

### huggingface-tool-builder
"Use essa habilidade quando o usuário quiser construir ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."

### huggingface-trackio
"Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analisar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do espaço do HF e saída JSON para automação."

### huggingface-vision-trainer
"Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — mais qualquer classificador de Transformadores) e segmentação SAM/SAM2 usando Transformadores do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparo de conjunto de dados no formato COCO, aumento de dados Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."

### transformers-js
"Use Transformers.js para executar modelos de aprendizado de máquina de estado da arte diretamente em JavaScript/TypeScript. Suporta tarefas de NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de execução de servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Autenticação
- **Caso de Uso:** O usuário não está autenticado no Hugging Face Hub.
- **Tratamento:** Redirecione o usuário para a página de login do Hugging Face Hub e forneça instruções sobre como se autenticar.

### Erros de Permissão
- **Caso de Uso:** O usuário não tem permissão para acessar um recurso específico do Hugging Face Hub.
- **Tratamento:** Informe o usuário sobre as permissões necessárias e forneça instruções sobre como solicitar acesso.

### Erros de Conexão
- **Caso de Uso:** O usuário está enfrentando problemas de conexão com o Hugging Face Hub.
- **Tratamento:** Forneça dicas de solução de problemas para conexão, como verificar a conexão de internet e tentar novamente.

### Erros de Modelo
- **Caso de Uso:** O usuário está enfrentando problemas com um modelo específico do Hugging Face Hub.
- **Tratamento:** Forneça informações sobre como diagnosticar e solucionar problemas comuns de modelo, como verificar a documentação do modelo e buscar ajuda na comunidade do Hugging Face.

### Edge Cases
- **Caso de Uso:** O usuário está tentando usar uma habilidade de forma inesperada ou com parâmetros inválidos.
- **Tratamento:** Forneça mensagens de erro claras e concisas, indicando o que deu errado e como corrigir. Além disso, considere adicionar validação de entrada para prevenir erros semelhantes no futuro.

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o `scripts/example.py` da habilidade `hf-datasets` seria referenciado como `hf-datasets/scripts/example.py`.