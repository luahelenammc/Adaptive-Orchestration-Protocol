#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build deterministic AOP composite and Agent Skill ZIP distributions."""
from __future__ import annotations
import argparse, hashlib, io, json, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = "ADAPTIVE_ORCHESTRATION_PROTOCOL.md"
ADAPTERS = [
    "adapters/ADAPTIVE_ORCHESTRATION_ASTRA_ADAPTER.md",
    "adapters/ADAPTIVE_ORCHESTRATION_GPT6_SOL_LUNA_ADAPTER.md",
    "adapters/ADAPTIVE_ORCHESTRATION_GPT6_TERRA_ADAPTER.md",
    "adapters/ADAPTIVE_ORCHESTRATION_GROK_BOT_ADAPTER.md",
]
MEMBERS = [CORE, *ADAPTERS]
SKILL = "skills/moon-adaptive-orchestration/SKILL.md"
COMPOSITE = "downloads/adaptive-orchestration-protocol.zip"
SKILL_ZIP = "downloads/skills/moon-adaptive-orchestration.zip"

def deterministic_zip(files: dict[str, bytes]) -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return out.getvalue()

def composite_bytes() -> bytes:
    return deterministic_zip({name: (ROOT/name).read_bytes() for name in MEMBERS})

def skill_bytes() -> bytes:
    skill_path = ROOT/SKILL
    refs = {"references/ADAPTIVE_ORCHESTRATION_PROTOCOL.md": (ROOT/CORE).read_bytes()}
    refs.update({"references/"+name: (ROOT/name).read_bytes() for name in ADAPTERS})
    hashes = {name: hashlib.sha256(data).hexdigest() for name,data in refs.items()}
    provenance = {
        "source_repository": "https://github.com/luahelenammc/Adaptive-Orchestration-Protocol",
        "source_version": "6.4",
        "canonical_path": CORE,
        "included_reference_sha256": hashes,
        "creator": "Lua Helena Moon Martins Cardoso (Moon)",
        "ai_assisted_coauthor": "Áurion",
        "license": "CC-BY-4.0",
        "transformation": "The bundled references are the canonical core and adapter bytes. The short skill frontend points to this repository as the source of truth.",
    }
    files = {
        "moon-adaptive-orchestration/SKILL.md": skill_path.read_bytes(),
        "moon-adaptive-orchestration/references/PROVENANCE.json": (json.dumps(provenance, ensure_ascii=False, indent=2, sort_keys=True)+"\n").encode(),
        "moon-adaptive-orchestration/LICENSE-CC-BY-4.0.txt": (ROOT/"LICENSES/CC-BY-4.0.txt").read_bytes(),
        **{"moon-adaptive-orchestration/"+name:data for name,data in refs.items()},
    }
    return deterministic_zip(files)

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    outputs={COMPOSITE:composite_bytes(),SKILL_ZIP:skill_bytes()}
    stale=[]
    for rel,data in outputs.items():
        path=ROOT/rel
        if args.check:
            if not path.is_file() or path.read_bytes()!=data: stale.append(rel)
        else:
            path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
    if stale: raise SystemExit("stale or missing packages: "+", ".join(stale))
    print(("verified" if args.check else "built")+f" {len(outputs)} deterministic packages")

if __name__ == "__main__": main()
