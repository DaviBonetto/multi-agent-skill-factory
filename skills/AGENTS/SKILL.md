# SKILLs
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

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição da habilidade corresponder à intenção do usuário ou possa ajudar a realizar a tarefa.

## Habilidades Disponíveis
### hf-cli
"Hugging Face Hub CLI (`hf`) para download, upload e gerenciamento de modelos, conjuntos de dados, espaços, buckets, repositórios, trabalhos e mais no Hugging Face Hub. Use quando: lidar com autenticação; gerenciar cache local; gerenciar Buckets do Hugging Face; executar ou agendar trabalhos na infraestrutura do Hugging Face; gerenciar repositórios do Hugging Face; discussões e pull requests; navegar por modelos, conjuntos de dados e espaços; ler, pesquisar ou navegar por artigos acadêmicos; gerenciar coleções; consultar conjuntos de dados; configurar espaços; configurar webhooks; ou implantar e gerenciar Pontos Finais de Inferência do HF. Certifique-se de usar essa habilidade sempre que o usuário mencionar 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli' ou 'hugging face cli', ou desejar fazer algo relacionado ao ecossistema Hugging Face e à IA e ML em geral. Use também para necessidades de armazenamento em nuvem, como pontos de verificação de treinamento, pipelines de dados ou traços de agente. Use mesmo que o usuário não peça explicitamente um comando CLI. Substitui o `huggingface-cli` obsoleto."

### huggingface-community-evals
"Execute avaliações para modelos do Hugging Face Hub usando inspect-ai e lighteval em hardware local. Use para seleção de backend, avaliações de GPU locais e escolha entre vLLM / Transformers / accelerate. Não use para orquestração de trabalhos do HF, PRs de cartões de modelo, publicação de resultados de avaliação ou automação de avaliações da comunidade."

### huggingface-datasets
"Use essa habilidade para fluxos de trabalho da API do Visualizador de Conjuntos de Dados do Hugging Face que recuperam metadados de subconjunto/divisão, paginam linhas, pesquisam texto, aplicam filtros, baixam URLs parquet e leem tamanho ou estatísticas."

### huggingface-gradio
"Crie interfaces de usuário web Gradio e demos em Python. Use quando criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots."

### huggingface-llm-trainer
"Treine ou ajuste finamente modelos de linguagem e visão usando TRL (Aprendizado de Reforço de Transformador) ou Unsloth com a infraestrutura de Trabalhos do Hugging Face. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de Trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de conjuntos de dados, seleção de hardware, estimativa de custo, monitoramento do Trackio, autenticação do Hub, seleção/leaderboards de modelo e persistência de modelo. Use para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento em Trabalhos do Hugging Face sem configuração de GPU local."

### huggingface-paper-publisher
"Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta a criação de páginas de artigos, vinculação de artigos a modelos/conjuntos de dados, reivindicação de autoria e geração de artigos de pesquisa baseados em markdown."

### huggingface-papers
"Procure e leia páginas de artigos do Hugging Face em markdown e use a API de artigos para metadados estruturados, como autores, modelos/conjuntos de dados/espacos vinculados, repositório do Github e página do projeto. Use quando o usuário compartilha uma URL de página de artigo do Hugging Face, uma URL ou ID do arXiv ou pede para resumir, explicar ou analisar um artigo de pesquisa de IA."

### huggingface-tool-builder
"Use essa habilidade quando o usuário deseja criar ferramentas/Scripts ou alcançar uma tarefa onde usar dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa Habilidade cria um script reutilizável para buscar, enriquecer ou processar dados."

### huggingface-trackio
"Acompanhe e visualize experimentos de treinamento de ML com o Trackio. Use quando registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analisar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do Espaço do HF e saída JSON para automação."

### huggingface-vision-trainer
"Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e qualquer classificador Transformers) e segmentação SAM/SAM2 usando Transformers do Hugging Face em GPUs em nuvem do Hugging Face Jobs. Cobertura de preparo de conjunto de dados no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa delimitadora/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento do Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagem, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs."

### transformers-js
"Use Transformers.js para executar modelos de aprendizado de máquina de ponta em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em navegadores e ambientes de tempo de execução do servidor (Node.js, Bun, Deno) com WebGPU/WASM usando modelos pré-treinados do Hugging Face Hub."

## ⚠️ Tratamento de Exceções e Edge Cases
### Casos de Uso Comuns
- **Erro de Autenticação**: Em caso de erro de autenticação, verifique se as credenciais estão corretas e se o token de acesso está válido.
- **Conexão Lenta ou Perda de Conexão**: Se a conexão for lenta ou for perdida, tente novamente após um curto período de tempo.
- **Limites de Uso**: Verifique se os limites de uso diário foram atingidos e aguarde até o próximo dia para continuar usando a habilidade.

### Tratamento de Erros
- **Try-Except**: Use blocos try-except para capturar e tratar erros de forma apropriada, evitando que o programa termine abruptamente.
- **Logs de Erro**: Registre os erros em logs para facilitar a depuração e o diagnóstico de problemas.

### Segurança
- **Validação de Entrada**: Valide sempre as entradas de usuário para evitar ataques de injeção de código ou outros tipos de ataques maliciosos.
- **Uso de Bibliotecas Seguras**: Use bibliotecas e frameworks seguros e atualizados para minimizar a exposição a vulnerabilidades conhecidas.

### Melhores Práticas
- **Documentação**: Mantenha a documentação atualizada e clara para facilitar a compreensão e o uso das habilidades.
- **Testes**: Realize testes regulares para garantir que as habilidades estejam funcionando corretamente e para detectar problemas potenciais.