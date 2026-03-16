# SKILLs Documentados
Você tem habilidades adicionais documentadas em diretórios que contêm um arquivo "SKILL.md".

Essas habilidades são:
 - gradio -> "skills/huggingface-gradio/SKILL.md"
 - hf-cli -> "skills/hf-cli/SKILL.md"
 - hugging-face-dataset-viewer -> "skills/hugging-face-dataset-viewer/SKILL.md"
 - hugging-face-datasets -> "skills/hugging-face-datasets/SKILL.md"
 - hugging-face-evaluation -> "skills/hugging-face-evaluation/SKILL.md"
 - hugging-face-jobs -> "skills/hugging-face-jobs/SKILL.md"
 - hugging-face-model-trainer -> "skills/hugging-face-model-trainer/SKILL.md"
 - hugging-face-paper-publisher -> "skills/hugging-face-paper-publisher/SKILL.md"
 - hugging-face-tool-builder -> "skills/hugging-face-tool-builder/SKILL.md"
 - hugging-face-trackio -> "skills/hugging-face-trackio/SKILL.md"
 - hugging-face-vision-trainer -> "skills/hugging-face-vision-trainer/SKILL.md"
 - transformers-js -> "skills/transformers.js/SKILL.md"

IMPORTANTE: Você DEVE ler o arquivo SKILL.md sempre que a descrição das habilidades corresponder à intenção do usuário ou possa ajudar a realizar sua tarefa.

## Habilidades Disponíveis
### gradio
`Construa interfaces de usuário web Gradio e demos em Python. Use ao criar ou editar aplicativos Gradio, componentes, ouvintes de eventos, layouts ou chatbots.`
### hf-cli
`CLI do Hugging Face Hub (hf) para download, upload e gerenciamento de repositórios, modelos, conjuntos de dados e Spaces no Hugging Face Hub. Substitui o comando `huggingface-cli` agora obsoleto.`
### hugging-face-dataset-viewer
`Use essa habilidade para fluxos de trabalho da API do Visualizador de Conjuntos de Dados do Hugging Face que buscam metadados de subconjuntos/subdivisões, paginam linhas, procuram texto, aplicam filtros, baixam URLs parquet e lêem tamanho ou estatísticas.`
### hugging-face-datasets
`Crie e gerencie conjuntos de dados no Hugging Face Hub. Suporta inicialização de repositórios, definição de configurações/solicitações de sistema, atualizações de linhas em streaming e consultas/transormações de conjuntos de dados baseadas em SQL. Projetado para funcionar ao lado do servidor MCP do HF para fluxos de trabalho de conjuntos de dados abrangentes.`
### hugging-face-evaluation
`Adicione e gerencie resultados de avaliação em cartões de modelo do Hugging Face. Suporta extração de tabelas de avaliação do conteúdo do README, importação de pontuações da API de Análise Artificial e execução de avaliações de modelo personalizadas com vLLM/lighteval. Funciona com o formato de metadados model-index.`
### hugging-face-jobs
`Essa habilidade deve ser usada quando os usuários desejam executar qualquer carga de trabalho na infraestrutura de Trabalhos do Hugging Face. Cobertura de scripts UV, trabalhos baseados em Docker, seleção de hardware, estimativa de custo, autenticação com tokens, gerenciamento de segredos, configuração de tempo limite e persistência de resultados. Projetado para cargas de trabalho de computação de propósito geral, incluindo processamento de dados, inferência, experimentos, trabalhos em lote e tarefas baseadas em Python. Deve ser invocado para tarefas que envolvam computação em nuvem, cargas de trabalho de GPU ou quando os usuários mencionam executar trabalhos na infraestrutura do Hugging Face sem configuração local.`
### hugging-face-model-trainer
`Essa habilidade deve ser usada quando os usuários desejam treinar ou ajustar finamente modelos de linguagem usando TRL (Aprendizado de Reforço de Transformador) na infraestrutura de Trabalhos do Hugging Face. Cobertura de métodos de treinamento SFT, DPO, GRPO e modelagem de recompensa, além de conversão GGUF para implantação local. Inclui orientação sobre o pacote de Trabalhos TRL, scripts UV com formato PEP 723, preparo e validação de conjuntos de dados, seleção de hardware, estimativa de custo, monitoramento Trackio, autenticação do Hub e persistência de modelos. Deve ser invocado para tarefas que envolvam treinamento de GPU em nuvem, conversão GGUF ou quando os usuários mencionam treinamento na infraestrutura de Trabalhos do Hugging Face sem configuração de GPU local.`
### hugging-face-paper-publisher
`Publique e gerencie artigos de pesquisa no Hugging Face Hub. Suporta criação de páginas de artigos, vinculação de artigos a modelos/conjuntos de dados, reivindicação de autorias e geração de artigos de pesquisa baseados em markdown profissionais.`
### hugging-face-tool-builder
`Use essa habilidade quando o usuário deseja construir ferramentas/scripts ou alcançar uma tarefa onde o uso de dados da API do Hugging Face possa ajudar. Isso é especialmente útil quando encadeando ou combinando chamadas de API ou a tarefa será repetida/automatizada. Essa Habilidade cria um script reutilizável para buscar, enriquecer ou processar dados.`
### hugging-face-trackio
`Acompanhe e visualize experimentos de treinamento de ML com Trackio. Use ao registrar métricas durante o treinamento (API Python), disparar alertas para diagnósticos de treinamento ou recuperar/analisar métricas registradas (CLI). Suporta visualização de painel em tempo real, alertas com webhooks, sincronização do Espaço do HF e saída JSON para automação.`
### hugging-face-vision-trainer
`Treine e ajuste finamente modelos de visão para detecção de objetos (D-FINE, RT-DETR v2, DETR, YOLOS), classificação de imagens (modelos timm — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — e qualquer classificador Transformers) e segmentação SAM/SAM2 usando Transformers do Hugging Face em GPUs de nuvem do Hugging Face Jobs. Cobertura de preparo de conjuntos de dados no formato COCO, aumento de dados com Albumentations, avaliação mAP/mAR, métricas de precisão, segmentação SAM com prompts de caixa/ponto, perda DiceCE, seleção de hardware, estimativa de custo, monitoramento Trackio e persistência do Hub. Use quando os usuários mencionam treinamento de detecção de objetos, classificação de imagens, SAM, SAM2, segmentação, matting de imagens, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, modelos de caixa delimitadora ou ajuste fino de modelos de visão no Hugging Face Jobs.`
### transformers-js
`Use Transformers.js para executar modelos de aprendizado de máquina de última geração diretamente em JavaScript/TypeScript. Suporta NLP (classificação de texto, tradução, resumo), visão computacional (classificação de imagens, detecção de objetos), áudio (reconhecimento de fala, classificação de áudio) e tarefas multimodais. Funciona em Node.js e navegadores (com WebGPU/WASM) usando modelos pré-treinados do Hugging Face Hub.`

## ⚠️ Tratamento de Exceções e Edge Cases
### Erros de Autenticação
- **Caso de Uso:** Quando o usuário não está autenticado corretamente no Hugging Face Hub.
- **Tratamento:** Verifique se o token de autenticação está válido e se o usuário tem permissões necessárias. Caso contrário, solicite ao usuário que se autentique novamente ou forneça as permissões necessárias.
### Erros de Conexão
- **Caso de Uso:** Quando ocorre um erro de conexão ao acessar a API do Hugging Face Hub.
- **Tratamento:** Verifique se a conexão de rede está estável e se o servidor do Hugging Face Hub está disponível. Caso contrário, tente novamente após um período de tempo ou forneça uma mensagem de erro ao usuário.
### Erros de Formatação de Dados
- **Caso de Uso:** Quando os dados fornecidos pelo usuário estão em um formato inválido.
- **Tratamento:** Verifique se os dados estão no formato correto e se atendem aos requisitos da API do Hugging Face Hub. Caso contrário, forneça uma mensagem de erro ao usuário e solicite que os dados sejam corrigidos.
### Outros Erros
- **Caso de Uso:** Quando ocorre um erro não esperado.
- **Tratamento:** Registre o erro e forneça uma mensagem de erro genérica ao usuário. Além disso, verifique se o erro é recorrente e se é necessário realizar ajustes no código para evitar que ele ocorra novamente.

Os caminhos referenciados dentro das pastas de habilidades são relativos àquela habilidade. Por exemplo, o script `example.py` na pasta `hf-datasets` seria referenciado como `hf-datasets/scripts/example.py`.