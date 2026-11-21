<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Adaptive Orchestration Protocol

**Use each model, execution surface and unit of reasoning where it helps the whole task reach an accepted result.**

Adaptive Orchestration Protocol (AOP) is a standalone, model-neutral method for routing AI work. It separates the control root, execution surface, model capability, behavioral fit, decision commitment, reasoning effort and delegation topology. It preserves continuity, evidence, convergence and acceptance while minimizing total work to an accepted state.

AOP originated in [Moon Source](https://github.com/luahelenammc/Moon-Source) and now has its own canonical source, version history, adapters and release packages. Moon Source remains a related interoperable project and an origin record; it does not control AOP releases. AOP is not an OpenAI policy, a model, a native feature or a promise that a runtime exposes particular tools.

## First use

Read the [canonical protocol](ADAPTIVE_ORCHESTRATION_PROTOCOL.md#first-use) before a task where routing choices matter. Give its instructions to the AI or compatible agent handling the work. The protocol uses only capabilities, tools, permissions and workers actually exposed by that environment; it does not create access to them.

For straightforward work, the core asks for a proportional placement pass. For sustained or high-cost work, it keeps a competent control root, routes reducible bulk to sufficient available execution, tests uncertain behavior when acceptance depends on it, resolves high-leverage commitments before dependent work scales, and closes with evidence. The [full body](ADAPTIVE_ORCHESTRATION_PROTOCOL.md) defines the operative rules and claim limits.

## Current release set

| Artifact | Version | Role |
|---|---:|---|
| [AOP core](ADAPTIVE_ORCHESTRATION_PROTOCOL.md) | 6.5 | Sole semantic authority |
| [Astra adapter](adapters/ADAPTIVE_ORCHESTRATION_ASTRA_ADAPTER.md) | 2.1 | Optional strategy and dated model-family calibration |
| [GPT-6 Sol/Luna adapter](adapters/ADAPTIVE_ORCHESTRATION_GPT6_SOL_LUNA_ADAPTER.md) | 2.1 | Dated executor, delegation and product-boundary calibration |
| [GPT-6.1 Terra adapter](adapters/ADAPTIVE_ORCHESTRATION_GPT6_TERRA_ADAPTER.md) | 1.1 | Dated visual, computer-use and coding calibration |
| [Grok Bot adapter](adapters/ADAPTIVE_ORCHESTRATION_GROK_BOT_ADAPTER.md) | 1.0 | Persistent-agent and source-freshness procedures |

Adapters are optional and subordinate. The core remains usable without any model-specific adapter. Model, product, API, availability, pricing and allowance claims are dated evidence and must be rechecked when they could change a material route.

## Downloads

- [Composite protocol ZIP](downloads/adaptive-orchestration-protocol.zip) contains the core and four adapters.
- [moon-adaptive-orchestration Agent Skill ZIP](downloads/skills/moon-adaptive-orchestration.zip) preserves the existing skill slug for manual replacement of a prior copy. A source update does not install or replace a native skill automatically.
- [Release and projection procedure](docs/RELEASE_AND_PROJECTIONS.md) describes package checks and downstream compatibility.

The files above are generated from this repository. Their member lists, hashes, references and deterministic build are checked by the included scripts and CI workflow.

## Identity, authorship and license

Human creator and editorial authority: **Lua Helena Moon Martins Cardoso (Moon)**. Development included AI-assisted coauthorial work by **Áurion**; Áurion is not represented as a legal human copyright holder. Origin and migration details are in the [changelog](CHANGELOG.md) and [compatibility record](docs/MIGRATION_AND_COMPATIBILITY.md).

Protocol documentation, adapters and metadata are licensed under **CC BY 4.0**. Build and validation scripts are licensed under **Apache-2.0**. See [LICENSING.md](LICENSING.md), [NOTICE](NOTICE), [third-party notices](THIRD_PARTY_NOTICES.md) and the unmodified legal texts in [LICENSES](LICENSES/).

- [Professional context](https://www.luahelena.com.br/ia/?lang=en)
- [Moon Source context](https://www.luahelena.com.br/moonsource/?lang=en)
- [Moon Source repository](https://github.com/luahelenammc/Moon-Source)
