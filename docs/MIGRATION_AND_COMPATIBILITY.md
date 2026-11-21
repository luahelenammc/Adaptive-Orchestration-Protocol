<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Migration and compatibility

## Authority and lineage

This repository is the sole current semantic and release authority for AOP. Its 6.4 body and four subordinate adapters were transplanted from Moon Source commit [`6ec5d7910b561b392b114a1c7b64695a41e4716a`](https://github.com/luahelenammc/Moon-Source/commit/6ec5d7910b561b392b114a1c7b64695a41e4716a). The migration preserves AOP's existing version family; it is not a rewrite to 7.0 or a reset to 1.0. The original Git history remains in Moon Source. This repository records a source snapshot and links to that history instead of claiming a rewritten path history.

The destination snapshot retains the exact five operational artifacts in the composite package. Source SHA-256 values and legacy package hashes are recorded in the machine-readable [PROVENANCE.json](../PROVENANCE.json).

## Legacy route contract

| Legacy route | Compatibility behavior | New canonical target |
|---|---|---|
| Moon Source `portables/adaptive-orchestration/**` body, adapters and README | Human-readable moved-to pointer; path remains available | This repository's README, core and matching adapter |
| Moon Source `portables/chat-work/**`, `docs/CHAT_WORK_ASTRA_ADAPTER.md` | Human-readable succession pointer | AOP core and adapters |
| Moon Source `downloads/adaptive-orchestration-protocol.zip` and `chat-work-routing-protocol.zip` | Functional ZIP mirrors, rebuilt/verified from this repository; same five-member payload | [Composite ZIP](../downloads/adaptive-orchestration-protocol.zip) |
| Moon Source `downloads/skills/source/moon-adaptive-orchestration/SKILL.md` | Pointer to the maintained skill source | [Skill source](../skills/moon-adaptive-orchestration/SKILL.md) |
| Moon Source `downloads/skills/moon-adaptive-orchestration.zip` | Functional compatibility copy while legacy consumers exist | [Skill ZIP](../downloads/skills/moon-adaptive-orchestration.zip) |
| LUAHELENA `moonsource/downloads/ADAPTIVE_ORCHESTRATION_PROTOCOL.md` | Exact-byte convenience mirror of the current core; it is not an HTTP redirect | [Canonical core](../ADAPTIVE_ORCHESTRATION_PROTOCOL.md) |
| LUAHELENA `moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL.md` | Exact-byte compatibility mirror of the current core; it is not an HTTP redirect | [Canonical core](../ADAPTIVE_ORCHESTRATION_PROTOCOL.md) |
| LUAHELENA `moonsource/index.html` AOP card | Discovery in Moon Source context, labeled as an independent protocol | [Repository home](https://github.com/luahelenammc/Adaptive-Orchestration-Protocol) |

GitHub does not provide arbitrary HTTP redirects for individual Markdown/raw files across repositories, and ZIP payloads cannot act as redirects. The Moon Source GitHub paths therefore use readable pointers for text documents and byte-verified ZIP mirrors. The static site Markdown paths retain useful Markdown bytes; no 301 claim is made. Navigation and new download buttons point directly to this repository.

## Snapshot receipt

Origin commit: `6ec5d7910b561b392b114a1c7b64695a41e4716a`. Original core and adapter file SHA-256 values, plus the three origin package hashes, are preserved in [PROVENANCE.json](../PROVENANCE.json). The values describe the pre-transplant source bytes. Canonical-body editorial adjustments are disclosed in the changelog and provenance record; they do not alter AOP's routing doctrine.

## Related projects

- [Moon Source](https://github.com/luahelenammc/Moon-Source) is the origin and an interoperable consumer/bridge. It no longer versions AOP.
- [LUAHELENA](https://www.luahelena.com.br/moonsource/?lang=en) remains a discovery and convenience-download surface.
- [Moon Cortex](https://github.com/luahelenammc/Moon-Cortex) is a sibling project and has no required AOP dependency.
- Moon Source Language 5.1 remains an optional external conceptual/grammatical reference; AOP does not bundle it or require Moon Source to run.
