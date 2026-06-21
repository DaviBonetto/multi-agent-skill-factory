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
### Erros de Ordenação
*   Caso haja um erro de ordenação durante a reordenação das listas, o commit não deve ser realizado.
*   Verificar se as listas estão em ordem alfabética estrita antes de realizar o commit.
### Erros de Formatação
*   Caso haja um erro de formatação durante a reordenação das listas, o commit não deve ser realizado.
*   Verificar se as listas estão formatadas corretamente antes de realizar o commit.
### Edge Cases
*   Caso haja um novo item adicionado às listas, ele deve ser adicionado em ordem alfabética.
*   Caso haja um item removido das listas, as listas devem ser reordenadas para manter a ordem alfabética.
### Tratamento de Exceções
*   Caso ocorra um erro durante a reordenação das listas, o erro deve ser tratado e o commit não deve ser realizado.
*   Caso ocorra um erro durante a verificação das listas, o erro deve ser tratado e o commit não deve ser realizado.
### Segurança
*   As listas devem ser verificadas para garantir que não contenham informações sensíveis.
*   As listas devem ser protegidas contra alterações não autorizadas.