# Project Will — Observation #1 Dataset (2026-07-21 longrun)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21723921.svg)](https://doi.org/10.5281/zenodo.21723921)

Full logs and analyses of **32 autonomous LLM-driven Minecraft villagers** observed for ~6 hours with **no effective institutions provided** — no role assignment, no shared rules, no authority, no contract-enforcement mechanism. The villagers were given only a body, a 9-axis "discontent" state (survival / curiosity / community), and a personality. Nothing is forced by the system; "kill" and "mourn" appear nowhere in the prompts.

This is a single-run (n=1) observational dataset with a technical report. The full report ([REPORT.md](REPORT.md)) is in Japanese; this page is its English summary. Data files are language-independent in structure (in-game utterances are in Japanese).

## Headline numbers

| | |
|---|---|
| Population | 32 spawned + 10 born − 24 dead = **18 survived** |
| Deaths | **all 24 caused by other villagers** (0 starvation, 0 accidents) |
| Motive records | 24/24 killings had a matching grudge-ledger entry (trespass / attacked / witnessed) — 0 without one |
| Restraint | of 59 directed "trespassed my home" relations, 17 (29%) ended in a killing — **71% did not** |
| Mourning | **45 graves, unprompted** (selection rate 52/2,192 menu presentations); 8 graves built by killers for their own victims; epitaphs drifted from mourning ("the fighting ends here") to deterrence to a final "victory monument" in ~5 hours |
| Language | 58 place names invented; 244 second-hand acquisitions across up to 5 hops; **22 competing names for the same area at the end — no convergence** |
| Institutions | a barter-rate agreement, a self-declared "administrator", many commands — **all verbal: 0 contract executions, 0 obedience, no role specialization** |

## Key findings (summary of the report)

1. **Emergence happened at the level of links, not capabilities.** "Trespass → private retribution", "witnessing → revenge", "my own victim → burial", "stagnation → sea voyage" are written nowhere in the prompts. (Caveat: grudge and grief records are re-presented on encounter by design — the record is visible, the reaction is not scripted.)
2. **Institutional concepts stayed verbal.** The split between social behaviors that ran (retribution, burial, naming) and those that stayed talk (contracts, commands, prices) is consistent with the presence or absence of three scaffolds: a **persistent ledger**, a **physical means of execution**, and a **violation cost**. (Single-run inference — no element-wise ablation yet; that is the next observation.)
3. **Information spread only where an output channel existed.** Place names (a dedicated output slot) were received 2,977 times; "who killed whom" (free text only) propagated second-hand **exactly 0 times** across 9,874 utterances — even though 33 villagers held first-hand records of a killing.
4. **A language–state dissociation.** A serial killer declared, one second after his second killing, that "order was preserved thanks to the removal" — while his internal stagnation gauge rose monotonically (78→93) through all six killings. Killing never resolved the killer's own drive.
5. **A contrasting result to Artificial Leviathan** (Dai et al., arXiv:2406.14373). That study gave LLM agents survival drives in a resource-scarce sandbox with no institutions prescribed, and observed the Hobbesian arc: unrestrained conflict → social contracts → an absolute sovereign → a peaceful commonwealth. Its action set, however, includes `concede` — defined as creating a *permanent contract*, after which the system tracks the agent as a subordinate and enforces that "subordinates cannot refuse the rob action from superiors." That environment therefore contains all three scaffolds this report identifies (ledger, means of execution, violation cost), plus a far more abstract action space in which forming a contract costs a single move. In our embodied world none of these exist and every social act must be assembled from physical movement and encounter — and no social contract formed. The difference between the two outcomes appears to lie in the environment, not in the models.
6. **A response to Project Sid's Limitations** (arXiv:2411.00114 §7): we implemented the innate drives Sid described as missing (survival / curiosity / community), withheld the institutional scaffolding Sid provided (constitution, missionary-seeded religion), and observed which societal elements do and do not appear de novo. The result suggests, from the opposite direction, that Sid's choice to provide institutional scaffolding was well-founded.

## What's in this repository

- [REPORT.md](REPORT.md) — technical report (Japanese)
- [VERIFICATION.md](VERIFICATION.md) — claim ↔ data mapping (~50 claims)
- [DATA.md](DATA.md) — data dictionary + known caveats
- [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) — record of design judgments (what was withheld, and why)
- `data/` — 64 files: all 9,874 utterances, 14,969 structured events, a motive audit of all 24 killings, all 45 epitaphs with confirmed authorship, name-propagation networks
- `tools/find.py` — cross-log search tool (`python tools/find.py <term> [--time A B]`)

## System (one paragraph)

Minecraft Fabric mod (body) ⇄ Python brain (mind) ⇄ Gemini 3.1 Flash-Lite, escalating to `gemini-3-flash-preview` only at 4 decision points (attack opportunity, being attacked, witnessing a death, migration). All LLM calls use JSON-schema structured output; generation parameters were left at API defaults. Minecraft 26.1.2 / Fabric Loader 0.19.2. Memory is strictly per-individual — knowledge moves only by seeing, talking, and reading signs. Timestamps `T+HH:MM:SS` count from run start (epoch **1784565997032** = 2026-07-21 01:46:37 JST).

## Video

https://youtu.be/Xn0kTCtqDO0 (Japanese audio, English subtitles)

## License / Citation

Data & documents: **CC BY 4.0** / scripts: **MIT** ([LICENSE](LICENSE))

> Monocola. (2026). *Project Will: Observation #1 — 32 autonomous LLM villagers, 6 hours, no institutions* [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.21723921

(Concept DOI — always resolves to the latest version. v1.0 = 10.5281/zenodo.21723922)

Author: Monocola — questions welcome via Issues, in Japanese or English.
