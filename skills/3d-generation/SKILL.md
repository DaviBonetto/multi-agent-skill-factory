# 3D Geração de Espaços
## Introdução
A construção de um Espaço cuja saída é um ativo 3D — imagem (ocasionalmente texto) de entrada, mesh (GLB/OBJ/PLY/STL) ou gaussian splat (.ply/.splat) de saída, visualizável no navegador e baixável. Leia este guia sempre que desejar um Espaço/demonstração/área de teste para um modelo de geração 3D, seja um checkpoint de estoque ou sua própria variante finetunada. Pipelines NeRF e modelos de mundo/cena (HunyuanWorld, HY-World) não são cobertos.

O fluxo de trabalho padrão em `SKILL.md` se aplica (criar → construir → iterar → verificar). Este arquivo é o ponto de entrada para 3D; as referências abaixo cobrem as diferenças específicas de 3D.

## Referências Subsequentes
| Quando Ler | Arquivo |
| --- | --- |
| Manipulação de extensões CUDA/C++ — rodas pré-construídas, truques de compilação de inicialização, modo de falha dominante | `[3d-cuda-extensions.md](3d-cuda-extensions.md)` |
| Formatos de saída (GLB/OBJ/PLY/STL, splats), visualizadores, orientação, pré-processamento, padrões de arquivos temporários | `[3d-outputs.md](3d-outputs.md)` |
| Detalhes de seleção de modelo e receitas por família (TRELLIS, Hunyuan3D, TripoSR, SF3D, …) | `[3d-models.md](3d-models.md)` |
| Entregáveis gaussian-splat (TripoSplat, LGM) — decodificação de splat pura PyTorch | `[3d-gsplat.md](3d-gsplat.md)` |

## O que Torna os Espaços 3D Diferentes
1. **Extensões Nativas.** Esses modelos necessitam de extensões CUDA/C++ (nvdiffrast, rasterizadores, marching cubes, bakers de textura) que não podem ser compilados no momento da construção do Espaço. Espaços funcionais usam rodas pré-construídas ou truques de compilação de inicialização — [`3d-cuda-extensions.md`](3d-cuda-extensions.md). Errar isso é o modo de falha dominante.
2. **Código de Modelo Vendido.** Nenhum dos principais modelos 3D é limpo para instalação via pip; cada Espaço oficial carrega a biblioteca do modelo como uma árvore de fonte no repositório do Espaço. Não há uma linha de comando única como no `diffusers`. (Não confie em clones do PyPI: `trellis-3d` envia a árvore Python sem as extensões CUDA ou o conjunto real de dependências.)

Ambos os pontos tornam **"duplicar o Espaço oficial, então editar"** melhor do que "montar do zero" aqui mais do que para qualquer outra classe de modelo.

## Escolhendo um Modelo
| Prioridade | Escolha | Por Quê | Referência |
| --- | --- | --- | --- |
| Melhor Qualidade, Texturas PBR | **TRELLIS.2** | barra de qualidade atual; MIT; ≥24 GB (se encaixa em ZeroGPU large) | `[3d-models.md](3d-models.md)` |
| Saída Texturizada, História de Finetuning | **Hunyuan3D-2.1** (2.0 para mais leve/rápido) | código de treinamento oficial → alvo de finetuning comum; estágio de pintura PBR; licença não comercial | `[3d-models.md](3d-models.md)` |
| Velocidade / Alto Tráfego / Simplicidade | **TripoSR** (sem textura, MIT) ou **SF3D** (texturizada, controlada) | passe único para frente, duração de ~60s, código-base tiny | `[3d-models.md](3d-models.md)` |
| Gaussianos ao Lado de Malha, Entrada Multi-Imagem | **TRELLIS 1** | decodificador dual gaussian+malha; mais leve do que TRELLIS.2 | `[3d-models.md](3d-models.md)` |
| Gaussian Splats como Entregável | **TripoSplat** (ou LGM) | decodificação de splat pura PyTorch, sem rasterizador necessário; `gr.Model3D` renderiza splat `.ply` nativamente | `[3d-gsplat.md](3d-gsplat.md)` |

**Verifique a Porta e a Licença na Fase 0, não na Primeira Construção.** `stabilityai/stable-fast-3d` e `stable-point-aware-3d` são controlados (`gated: auto`) — o usuário deve ter aceito a licença e o Espaço precisa de `HF_TOKEN` como um segredo; verifique o acesso com `hf repos info` / `HfApi().model_info()` antecipadamente. `tencent/Hunyuan3D-*` é não controlado mas **não comercial** — sinalize antes que o Espaço vá para o público. TRELLIS/TripoSR/TripoSplat/LGM são MIT. Apple SHARP é apenas para pesquisa (`apple-amlr`).

## Caminho de Implantação: Duplicar vs Construir
**Duplicar o Espaço Oficial** (padrão para checkpoints de estoque e para finetunes que são uma troca `from_pretrained` — cada arquivo de referência documenta a troca):
```python
from huggingface_hub import HfApi
api = HfApi()
api.duplicate_repo("tencent/Hunyuan3D-2", to_id=f"{username}/my-hunyuan3d",
                   repo_type="space", private=True, space_hardware="zero-a10g",
                   space_secrets=[{"key": "HF_TOKEN", "value": hf_token}],  # apenas se um repositório controlado/privado estiver envolvido
                   exist_ok=True)
```
(`duplicate_space` é o nome depreciado mais antigo.) Confirme que o Espaço de origem está atualmente EM EXECUÇÃO primeiro (`hf spaces info <id> --expand runtime`) — uma origem pausada/quebrada significa bitrot. A duplicação copia *apenas arquivos*; passe `space_hardware=`/`space_secrets=` explicitamente. Em seguida, `hf download <repo> --repo-type space --local-dir .`, faça as edições mínimas (id do repositório do checkpoint, título/README, cortes de UI) e envie de volta com `hf upload ... --repo-type space`. **Resista a reescrever código de manipulação de extensão funcionando que você não entende completamente** — patches de sitecustomize, preloads de `ctypes.CDLL`, caches de autotune e chamadas de `zero.startup()` parecem redundantes até serem removidos.

**Construir a Partir do Zero** (UI personalizado, cortes de forma apenas, sem Espaço oficial ao vivo): comece a partir do esqueleto do TripoSR (o ~200 linhas de aplicativo documentado em [`3d-models.md`](3d-models.md) — o modelo de template mais limpo), vender a árvore da biblioteca do modelo do Espaço oficial ou do GitHub e siga [`3d-cuda-extensions.md`](3d-cuda-extensions.md). Orçamento mais iterações de depuração do que um Espaço de modelo de imagem.

De qualquer forma, **pegue os arquivos ao vivo do Espaço oficial primeiro** (`https://huggingface.co/spaces/{id}/raw/main/{path}`) e trate-os — não os pins do arquivo de referência — como a fonte de verdade. Os arquivos de referência registram o que foi enviado até meados de 2026; o runtime ZeroGPU se move e os Espaços oficiais o acompanham.

## Design de UI
Leia [`3d-outputs.md`](3d-outputs.md) para formatos, visualizadores, pré-processamento e padrões de arquivos temporários. UI de imagem para 3D de linha de base:
- **Entrada**: upload de imagem → pré-visualização de pré-processamento visível (remoção de fundo + recorte — mostre o que o modelo realmente recebe) → gerar.
- **Controles**: apenas as configurações às quais este modelo responde. Semente + randomizar sempre; então por família: etapas de amostragem/orientação (TRELLIS, Hunyuan3D), resolução de marching-cubes (TripoSR), remesh/contagem de vértices/tamanho de textura (SF3D), decimação + tamanho de textura na extração (TRELLIS.2). Não exponha todos os campos de configuração de uma base de código de pesquisa.
- **Saída**: `gr.Model3D` (malhas não texturizadas, splats) ou `LitModel3D` com iluminação HDR (texturizadas/PBR), mais `gr.DownloadButton`s para GLB e formatos secundários. Modelos de duas etapas (TRELLIS) mostram uma pré-visualização de turntable rápida antes da extração de GLB mais lenta.
- **Exemplos**: 3–6 imagens conhecidas boas levantadas dos ativos do Espaço oficial, `cache_examples=True, cache_mode="lazy"`.

## Verificar: Adições Específicas de 3D
Além do teste de fumaça padrão em `SKILL.md` §7:
1. Esses aplicativos expõem **pontos de extremidade encadeados, não um `/predict`** — por exemplo, TripoSR: `/preprocess` (imagem → imagem segmentada) então `/generate` (→ arquivos de malha). `Client(...).view_api()` primeiro, então chame em sequência, alimentando o primeiro resultado no segundo via `handle_file(...)`.
2. **Valide o arquivo retornado, não sua existência.** Malhas:
```python
import trimesh
m = trimesh.load("out.glb", force="scene")
geoms = list(m.geometry.values()) if hasattr(m, "geometry") else [m]
assert geoms and sum(g.faces.shape[0] for g in geoms) > 0, "malha vazia"
```
Gaussian splat `.ply` (sem faces — verifique a contagem de pontos e atributos de splat):
```python
from plyfile import PlyData
v = PlyData.read("out.ply")["vertex"]
assert v.count > 1000, "gaussianos suspeitosamente poucos"
assert {"f_dc_0", "opacity", "scale_0", "rot_0"} <= set(v.data.dtype.names), "não é um ply gaussian"
```
3. **Olhe para ele no navegador uma vez.** Orientação (de pé? enfrentando para a frente?), presença de textura, iluminação do visualizador — os modos de falha que uma verificação programática não pode capturar ([`3d-outputs.md`](3d-outputs.md) → Orientação).
4. Compilações de extensão de tempo de inicialização falham *silenciosamente* (aplicativo ainda inicializa, recurso degrada) — grep o log de execução do topo mesmo quando tudo parece verde. Lista de verificação de falha: parte inferior de [`3d-cuda-extensions.md`](3d-cuda-extensions.md).

## O que Evitar
- Montar um Espaço TRELLIS/Hunyuan a partir do zero quando um Espaço oficial em execução existe para duplicar.
- Confiar em pins de versão do arquivo de referência sobre os arquivos ao vivo do Espaço oficial.
- Compilar extensões CUDA via `requirements.txt` (nenhum nvcc no momento da construção), ou `pip install`-ing pacotes lookalike do PyPI para as bibliotecas do modelo.
- Retornar malhas/gaussianos como objetos na memória de funções `@spaces.GPU` — escreva arquivos, retorne caminhos.
- Nomes de arquivos de saída fixos (`output.glb`) — usuários concorrentes sobrescrevem um ao outro.
- Declarar verde após `RUNNING` + um arquivo retornado. Carregue a malha, conte faces/pontos e olhe para ele uma vez.

## ⚠️ Tratamento de Exceções e Edge Cases
Além dos pontos mencionados anteriormente, é crucial tratar exceções e edge cases para garantir a robustez do Espaço 3D. Isso inclui:
- **Tratamento de Erros de Compilação:** Erros durante a compilação de extensões CUDA/C++ devem ser capturados e tratados adequadamente, fornecendo feedback útil ao usuário.
- **Manipulação de Arquivos:** Ao lidar com arquivos de malha, splats e outros ativos 3D, é importante ter cuidado com a manipulação de arquivos, garantindo que os caminhos sejam corretos e os arquivos sejam tratados de forma apropriada para evitar erros.
- **Limitações de Recursos:** Espaços 3D podem ser intensivos em termos de recursos. É essencial monitorar o uso de recursos e implementar mecanismos para lidar com limitações, como otimização de modelos ou gerenciamento de memória.
- **Compatibilidade de Modelos:** Com muitos modelos 3D disponíveis, a compatibilidade entre diferentes modelos e o Espaço é crucial. Trate as diferenças nos modelos e forneça suporte para vários formatos e configurações.
- **Segurança:** Garanta que o Espaço 3D seja seguro, protegendo contra uploads mal-intencionados de modelos ou arquivos que possam comprometer a segurança do sistema. Valide todos os uploads e implemente medidas de segurança adequadas.

Ao abordar esses desafios e tratar exceções e edge cases de forma eficaz, você pode criar um Espaço 3D robusto e confiável que atenda às necessidades dos usuários e forneça uma experiência de usuário satisfatória.