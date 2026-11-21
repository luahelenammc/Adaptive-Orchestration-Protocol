<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Release and projections

## Authority

Edit the core and adapter sources only in this repository. AOP semantic changes follow the existing versioning rule in the core; documentation moves, URL repair and package-only work do not earn a semantic bump. Keep adapters subordinate and independently versioned. Do not split the Astra or Sol/Luna family into one router per model version.

## Local build and acceptance

Run from the repository root:

```bash
python scripts/build_packages.py
python scripts/build_packages.py --check
python scripts/validate.py
```

The composite ZIP must contain exactly the core and four adapters in the documented archive paths. The skill ZIP keeps the `moon-adaptive-orchestration` slug, includes its declared references, source hashes, `PROVENANCE.json` and CC BY 4.0 text, and can be used for manual replacement. It does not install a native personal skill.

CI runs the same deterministic build check and validation. No workflow writes to Moon Source or the website. Release changes are promoted there through an independently reviewed PR and a readback receipt.

## Downstream projections

After an accepted source change:

1. build both packages and validate member lists, hashes, links, license metadata and skill references;
2. update only the required Moon Source compatibility pointers, package mirrors and discovery surfaces;
3. update the LUAHELENA AOP card and its two Markdown compatibility mirrors, preserving the PT/EN facade and linking new users directly to this repo;
4. open and validate each downstream PR against its own current branch; never use legacy stubs as package sources;
5. read back the merged files and compare legacy ZIP payload hashes to the new canonical packages;
6. record any unavailable deployment or native skill installation as pending, with an owner and next step.

Moon Source's compatibility verifier consumes this repository's generated package bytes and is read-only. GitHub does not supply an authorized cross-repository write token in that workflow. Until an explicit, verifiable cross-repository trigger exists, downstream updates are performed and reviewed in the same authorized release execution; no automatic synchronization is claimed.

## Recovery

If a downstream projection fails, revert that repository's projection through a normal revert PR while preserving the AOP source release. Correct the canonical package first, then repeat the downstream comparison. Never overwrite a newer canonical artifact from a stale mirror or force-push rewritten history.
