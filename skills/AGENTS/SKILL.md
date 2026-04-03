# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
 - hf-cli -> "skills/hf-cli/SKILL.md"
 - huggingface-community-evals -> "skills/huggingface-community-evals/SKILL.md"
 - huggingface-datasets -> "skills/huggingface-datasets/SKILL.md"
 - huggingface-gradio -> "skills/huggingface-gradio/SKILL.md"
 - huggingface-jobs -> "skills/huggingface-jobs/SKILL.md"
 - huggingface-llm-trainer -> "skills/huggingface-llm-trainer/SKILL.md"
 - huggingface-paper-publisher -> "skills/huggingface-paper-publisher/SKILL.md"
 - huggingface-papers -> "skills/huggingface-papers/SKILL.md"
 - huggingface-tool-builder -> "skills/huggingface-tool-builder/SKILL.md"
 - huggingface-trackio -> "skills/huggingface-trackio/SKILL.md"
 - huggingface-vision-trainer -> "skills/huggingface-vision-trainer/SKILL.md"
 - transformers-js -> "skills/transformers-js/SKILL.md"

**Importante:** Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
### hf-cli
`Hugging Face Hub CLI (hf) para download, upload e gerenciamento de repositórios, modelos, datasets e Spaces no Hugging Face Hub. Substitui o comando huggingface-cli agora depreciado.`
### huggingface-community-evals
`Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de trabalhos do HF Jobs, PRs de model-card, publicação de .eval_results ou automação de community-evals.`
### huggingface-datasets
`Use essa habilidade para fluxos de trabalho da API do Visualizador de Datasets do Hugging Face que buscam metadados de subconjunto/divisão, paginam linhas, procuram texto, aplicam filtros, baixam URLs parquet e leem tamanho ou estatísticas.`
### huggingface-gradio
`Crie interfaces de usuário web Gradio e demos em Python. Use ao criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots.`
### huggingface-jobs
`Essa habilidade deve ser usada quando os usuários desejam executar qualquer carga de trabalho na infraestrutura do Hugging Face Jobs. Cobertura de scripts UV, trabalhos baseados em Docker, seleção de hardware, estimativa de custo, autenticação com tokens, gerenciamento de segredos, configuração de tempo limite e persistência de resultados. Projetado para cargas de trabalho de processamento de dados, inferência, experimentos, trabalhos em lote e tarefas baseadas em Python. Deve ser invocado para tarefas que envolvam computação em nuvem, cargas de trabalho de GPU ou quando os usuários mencionam executar trabalhos na infraestrutura do Hugging Face sem configuração local.`
### huggingface-llm-trainer
`Essa habilidade deve ser usada quando os usuários desejam treinar ou ajustar finamente modelos de linguagem usando TRL (Aprendizado de Reforço de Transformador) na infraestrutura do Hugging Face Jobs. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além da conversão GGUF para implantação local. Inclui orientação sobre o pacote de trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de datasets, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub e persistência de modelos. Deve ser invocado para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento no Hugging Face Jobs sem configuração de GPU local.`
### huggingface-paper-publisher
`Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta a criação de páginas de artigos, vinculação de artigos a modelos/datasets, reivindicação de autorias e geração de artigos de pesquisa baseados em markdown profissionais.`
### huggingface-papers
`Pesquise e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/datasets/espacios vinculados, repositório GitHub e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID do arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA.`
### huggingface-tool-builder
`Use essa habilidade quando o usuário deseja construir ferramentas/scripts ou alcançar uma tarefa onde o uso de dados da API do Hugging Face ajudaria. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa habilidade cria um script reutilizável para buscar, enriquecer ou processar dados.`
### huggingface-trackio
`Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use ao registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analisar métricas registradas (CLI). Suporta visualização de dashboard em tempo real, alertas com webhooks, sincronização do espaço do HF e saída JSON para automação.`
### huggingface-vision-trainer
`Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e qualquer classificador Transformers), e SAM/SAM2 de segmentação usando Transformers do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparo de dataset no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa delimitadora/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs.`
### transformers-js
`Use Transformers.js para executar modelos de aprendizado de máquina de estado da arte diretamente em JavaScript/TypeScript. Suporta tarefas de NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em Node.js e navegadores (com WebGPU/WASM) usando modelos pré-treinados do Hugging Face Hub.`

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Autenticação
- **Caso:** O usuário não está autenticado no Hugging Face Hub.
- **Ação:** Solicite que o usuário se autentique antes de realizar a ação desejada.
### Erros de Permissão
- **Caso:** O usuário não tem permissão para realizar uma ação específica.
- **Ação:** Informe o usuário sobre as permissões necessárias e forneça orientações sobre como obtê-las.
### Erros de Conexão
- **Caso:** Ocorre um erro de conexão ao tentar acessar o Hugging Face Hub.
- **Ação:** Verifique a conexão de rede e tente novamente. Se o problema persistir, contate o suporte.
### Datasets e Modelos Não Encontrados
- **Caso:** O dataset ou modelo solicitado não é encontrado.
- **Ação:** Verifique se o nome do dataset ou modelo está correto e se ele está disponível no Hugging Face Hub.
### Parâmetros Inválidos
- **Caso:** São fornecidos parâmetros inválidos para uma ação.
- **Ação:** Informe o usuário sobre os parâmetros válidos e solicite que ele forneça os parâmetros corretos.

Caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets/scripts` seria referenciado como `hf-datasets/scripts/example.py`.