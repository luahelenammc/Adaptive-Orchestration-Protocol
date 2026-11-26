#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Validate AOP identity, package members, content hashes and skill references."""
from __future__ import annotations
import hashlib, json, re, zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CORE="ADAPTIVE_ORCHESTRATION_PROTOCOL.md"
ADAPTERS=["adapters/ADAPTIVE_ORCHESTRATION_ASTRA_ADAPTER.md","adapters/ADAPTIVE_ORCHESTRATION_GPT6_SOL_LUNA_ADAPTER.md","adapters/ADAPTIVE_ORCHESTRATION_GPT6_TERRA_ADAPTER.md","adapters/ADAPTIVE_ORCHESTRATION_GROK_BOT_ADAPTER.md"]
MEMBERS=[CORE,*ADAPTERS]
EXPECTED={CORE:"6.7",ADAPTERS[0]:"2.1",ADAPTERS[1]:"2.2",ADAPTERS[2]:"1.1",ADAPTERS[3]:"1.0"}
errors=[]
def need(ok,msg):
 if not ok: errors.append(msg)
core=(ROOT/CORE).read_text(encoding="utf-8")
need("https://github.com/luahelenammc/Adaptive-Orchestration-Protocol" in core,"core canonical repository metadata missing")
need("remains independently versioned at 6.7" in core,"stale independent version metadata")
need("Adaptive Orchestration Protocol 6.3 is the current public release" not in core,"stale 6.3 current-release claim")
need("Adaptive Orchestration remains independently versioned at 6.3" not in core,"stale 6.3 lifecycle claim")
for path,version in EXPECTED.items():
 text=(ROOT/path).read_text(encoding="utf-8")
 version_lines=[line for line in text.splitlines()[:45] if "version" in line.casefold() or "adapter" in line.casefold()]
 need(any(version in line for line in version_lines), f"version marker missing or changed: {path}")
 need("MOON-SOURCE-PUBLIC-STAMP" not in text, f"Moon Source ownership stamp remains in standalone artifact: {path}")
need("https://github.com/luahelenammc/Moon-Source/blob/main/portables/adaptive-orchestration/ADAPTIVE_ORCHESTRATION_PROTOCOL.md" not in core,"core points to old canonical path")
need("### Copy-Safe Link Transport" in core and "final user-visible report" in core and "one per line" in core and "independently resolve relevant locators" in core,"copy-safe transport contract missing")
need("Copy-Safe Link Transport" in (ROOT/"skills/moon-adaptive-orchestration/SKILL.md").read_text(encoding="utf-8"),"skill does not project copy-safe transport")
need("moon-adaptive-orchestration" in (ROOT/"skills/moon-adaptive-orchestration/SKILL.md").read_text(encoding="utf-8"),"skill slug missing")
if (ROOT/"downloads/adaptive-orchestration-protocol.zip").exists():
 with zipfile.ZipFile(ROOT/"downloads/adaptive-orchestration-protocol.zip") as z:
  need(z.namelist()==sorted(MEMBERS),"composite ZIP member set/order differs from contract")
  for name in MEMBERS:
   need(z.read(name)==(ROOT/name).read_bytes(),f"composite ZIP bytes differ: {name}")
if (ROOT/"downloads/skills/moon-adaptive-orchestration.zip").exists():
 with zipfile.ZipFile(ROOT/"downloads/skills/moon-adaptive-orchestration.zip") as z:
  names=set(z.namelist())
  base="moon-adaptive-orchestration/"
  required={base+"SKILL.md",base+"references/PROVENANCE.json",base+"LICENSE-CC-BY-4.0.txt",base+"references/ADAPTIVE_ORCHESTRATION_PROTOCOL.md",*(base+"references/"+p for p in ADAPTERS)}
  need(required<=names,"skill ZIP is missing a declared reference, provenance or license")
  provenance=json.loads(z.read(base+"references/PROVENANCE.json"))
  need(provenance["source_version"]==EXPECTED[CORE],"skill provenance version mismatch")
  need(z.read(base+"SKILL.md")== (ROOT/"skills/moon-adaptive-orchestration/SKILL.md").read_bytes(),"skill frontend bytes differ")
  for path in MEMBERS:
   need(z.read(base+"references/"+path)==(ROOT/path).read_bytes(),f"skill reference bytes differ: {path}")
  for path,digest in provenance["included_reference_sha256"].items():
   need(base+path in names,f"skill provenance points to missing package path: {path}")
   if base+path in names: need(hashlib.sha256(z.read(base+path)).hexdigest()==digest,f"skill reference hash mismatch: {path}")
if errors:
 print("AOP validation failed:")
 for err in errors: print("- "+err)
 raise SystemExit(1)
print("AOP identity, versions, compatibility metadata, ZIP members and skill provenance validated")
