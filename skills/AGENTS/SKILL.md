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
hf-cli: "Hugging Face Hub CLI (hf) para download, upload e gerenciamento de modelos, conjuntos de dados, espaços, buckets, repositórios, trabalhos e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar buckets do Hugging Face; executar ou agendar trabalhos na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, conjuntos de dados e espaços; ler, pesquisar ou navegar por artigos acadêmicos; gerenciar coleções; consultar conjuntos de dados; configurar espaços; definir webhooks; ou implantar e gerenciar pontos de extremidade de inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou quiser fazer algo relacionado ao ecossistema Hugging Face e à IA e ML em geral. Use também para necessidades de armazenamento em nuvem, como pontos de verificação de treinamento, pipelines de dados ou traços de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o habilidade `huggingface-cli` obsoleta."
huggingface-best: ">"
huggingface-community-evals: "Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de trabalhos do HF, PRs de cartões de modelo, publicação de resultados de avaliação da comunidade ou automação de avaliações da comunidade."
huggingface-datasets: "Use essa habilidade para fluxos de trabalho da API do Visualizador de Conjuntos de Dados do Hugging Face que recuperam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs de parquet e leem tamanho ou estatísticas."
huggingface-gradio: "Crie interfaces de usuário da web e demos em Python com Gradio. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."
huggingface-llm-trainer: "Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com a infraestrutura de trabalhos do Hugging Face. Aborda métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de conjunto de dados, seleção de hardware, estimativa de custo, monitoramento do Trackio, autenticação do Hub, seleção/painel de modelos e persistência de modelo. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local."
huggingface-local-models: "Use para selecionar modelos para executar localmente com llama.cpp e GGUF em CPU, Mac Metal, CUDA ou ROCm. Aborda encontrar GGUFs, seleção de quantização, execução de servidores, busca exata de arquivos GGUF, conversão e serviço local compatível com OpenAI."
huggingface-paper-publisher: "Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta a criação de páginas de artigos, vinculação de artigos a modelos/conjuntos de dados, reivindicação de autorias e geração de artigos de pesquisa baseados em markdown profissionais."
huggingface-papers: "Procure e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/conjuntos de dados/espacos vinculados, repositório do Github e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID do arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA."
huggingface-tool-builder: "Use essa habilidade quando o usuário deseja criar ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."
huggingface-trackio: "Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analizar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do espaço do HF e saída JSON para automação."
huggingface-vision-trainer: "Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e qualquer classificador de Transformadores) e segmentação SAM/SAM2 usando Transformadores do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Aborda preparo de conjunto de dados no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/bola, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento do Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."
train-sentence-transformers: "Treine ou ajuste finamente modelos de sentence-transformers em `SentenceTransformer` (bi-encoder; modelo de embedding denso ou estático; para recuperação, similaridade, clusterização, classificação, mineração de paráfrases, dedup, multimodal), `CrossEncoder` (rerank; pontuação de par para classificação de par / recuperação em duas etapas) e `SparseEncoder` (SPLADE, modelo de embedding esparsa; para recuperação aprendida-esparsa). Aborda seleção de perda, mineração de negativos difíceis, avaliadores, destilação, LoRA, Matryoshka e publicação no Hugging Face Hub. Use para qualquer tarefa de treinamento de sentence-transformers."
transformers-js: "Use Transformers.js para executar modelos de aprendizado de máquina de ponta em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de execução de servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
- **Erro de Autenticação**: Em caso de erro de autenticação, verifique se as credenciais estão corretas e se o token de acesso está válido. Se o problema persistir, tente resetar as credenciais ou contate o suporte.
- **Erro de Conexão**: Se ocorrer um erro de conexão, verifique se a conexão de internet está estável e se o servidor está disponível. Tente novamente após alguns minutos ou contate o suporte se o problema persistir.
- **Erro de Processamento**: Em caso de erro de processamento, verifique se os dados de entrada estão corretos e se o modelo está treinado para lidar com esses dados. Se o problema persistir, tente ajustar os parâmetros do modelo ou contate o suporte.

### Edge Cases
- **Dados Inválidos**: Se os dados de entrada forem inválidos, o modelo pode não funcionar corretamente. Verifique se os dados estão no formato correto e se estão dentro dos limites esperados.
- **Modelo não Treinado**: Se o modelo não estiver treinado para lidar com os dados de entrada, pode não funcionar corretamente. Verifique se o modelo está treinado para o tipo de dados que está sendo usado e se está atualizado.
- **Conflito de Dependências**: Se houver conflito de dependências entre as bibliotecas usadas, o modelo pode não funcionar corretamente. Verifique se as dependências estão atualizadas e se são compatíveis entre si.

### Prevenção de Erros
- **Validação de Dados**: Sempre valide os dados de entrada antes de processá-los para garantir que estão no formato correto e dentro dos limites esperados.
- **Testes**: Faça testes regulares para garantir que o modelo está funcionando corretamente e que não há erros ou problemas.
- **Atualização de Dependências**: Mantenha as dependências atualizadas para garantir que o modelo está usando as últimas versões das bibliotecas e frameworks.
