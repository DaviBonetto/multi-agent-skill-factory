# Platform-neutral README ordering — Phase C design
## Background
Phases A and B (see `2026-05-05-platform-neutral-prose-design.md` and `2026-05-05-platform-neutral-config-refs-design.md`) already neutralized generic Claude prose and config-file references in the README. The remaining platform-leaning signal is layout: the README's two platform listings put Claude Code first and aren't strictly alphabetical elsewhere.
This phase fixes the ordering. No prose changes.
## In scope
1. **Quickstart platform list** (`README.md:7`) — the inline link list of supported harnesses
2. **Installation section ordering** (`README.md:35–152`) — the per-harness install sub-sections
## Out of scope
- Prose, marketplace names, plugin IDs, URLs — all factually correct as-is.
- Visual weight of the Claude Code section (which has two sub-sections — official Anthropic marketplace and Superpowers marketplace). Both are real install paths; collapsing them would hide accurate info.
- Section headings and content within each install block — only the ordering of the blocks changes.
## Substitution
Both listings reorder to strict alphabetical:
| Old order | New order |
|-----------|-----------|
| Claude Code | Claude Code |
| Codex CLI | Codex App |
| Codex App | Codex CLI |
| Factory Droid | Cursor |
| Gemini CLI | Factory Droid |
| OpenCode | Gemini CLI |
| Cursor | GitHub Copilot CLI |
| GitHub Copilot CLI | OpenCode |
Three moves: Codex App swaps with Codex CLI; Cursor moves up two slots; GitHub Copilot CLI moves up one.
Claude Code remains first by alphabetical chance (`Cl…` precedes `Co…`).
## Commit plan
One atomic commit covering both listings, since changing one without the other would create inconsistency between the quickstart and the installation section.
## Verification
- Quickstart anchors (`#claude-code`, `#codex-app`, etc.) still resolve to existing `### …` headings — no headings renamed.
- Each install sub-section's body is byte-identical pre/post; only positions changed.
- `git diff README.md` shows section moves only, no content edits.
## ⚠️ Tratamento de Exceções e Edge Cases
- **Erros de ordenação**: caso a ordenação alfabética não seja possível devido a caracteres especiais ou acentos, a lista deve ser ordenada de forma que os itens sejam apresentados de maneira lógica e consistente.
- **Itens faltantes**: se um item estiver faltando na lista, a ordenação deve ser ajustada para refletir a ausência do item.
- **Duplicatas**: se houver duplicatas na lista, elas devem ser removidas para evitar inconsistências.
- **Caracteres especiais**: se houver caracteres especiais na lista, eles devem ser tratados de forma a garantir que a ordenação seja feita corretamente.
- **Limitações de tamanho**: se a lista for muito grande, pode ser necessário implementar uma solução de paginação ou filtragem para evitar problemas de desempenho.
- **Testes**: a lista deve ser testada para garantir que a ordenação esteja correta e que não haja erros ou inconsistências.