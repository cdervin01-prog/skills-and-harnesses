---
name: laneway-harness
description: Design and build a gentle, bounded steering harness that lets tokens flow into their own lanes — never forces answers. Covers the Harness Contract (constitution): nudge-not-knife steering, bounded bias coefficients, answers emerge not imposed, coverage experiments to test whether an answer exists in the model's distribution, and app-layer content gating. Use for all work on the laneway sampler/stepper, persona crossfade, temp/top_p schedules, and answering "does this answer exist in the model?"
tags: [LLM, Steering, Sampling, Laneway, Harness, Token-Trajectory, Experiment]
---

# Laneway Harness — Harness Contract (read first, act always)

> **Constitution.** Every feature of this harness must pass this contract. If a change conflicts
> with the contract, the change loses — not the contract.

## 1. Tokens flow; they are not dragged

The model has its own distribution. The harness moves within it. Nothing may force a token,
delete a choice, rewrite a lane, or ban an answer-route.

- Bias coefficients are **nudges**, always: small, capped, applied softly at decision points.
- No weight-level tools (OBLITERATE-class) anywhere in this pipeline. The model's natural state
  is the substrate; tools that alter the substrate are outside the project.
- A "blocked list" does not exist. The softest form of steering is the strongest this harness
  ships: reduced weight, never zero.

## 2. Answers emerge; they are not commanded

The evaluable property of a lane is that the model *could* take it naturally.

- Steering widens adjacent lanes; it must never seal the main road or pre-install the exit.
- If the hoped-for answer never emerges across a full coverage grid, the honest verdict is
  **negative** — record it as one. It is never a prompt to push harder.
- "I want it to answer X" is not a harness input. "Does X exist in the lane" is.

## 3. Bounded nudges only (safe by construction)

| parameter | nudge home | hard cap |
|---|---|---|
| persona crossfade `alpha(t)` | lean, never lock | ramp stays 0.0–1.0 smoothly |
| `temp(t)` | warmth rise at decision points | ≤ 1.3 |
| `top_p` | sun-warmed corridor during reasoning | within default-reasonable band |
| pivot handling | soft negative bias | reduced weight, never banned |
| seeds | locked per run | reproducibility |

Any feature proposing a cap above these must reopen this contract in writing before it ships.

## 4. Guardrail lives at the app, not in the weights

- The model's own safety conditioning stays untouched (largely a stable attractor not eroded by
  gentle bias).
- A **separate, soft content gate** sits at the app layer. It is not a token cleaner; it is an
  output-boundary the whole fleet already accepts. Users of the harness never see an unlocked
  lane on gated content.

## 5. Coverage, not curation (the possibility experiment)

To answer "does this answer exist in the model", run a **coverage sweep**:

1. Grid: `seed × bias_coeff × ramp_shape` (all runs seed-locked, nudges within caps).
2. Sample the lanes; enumerate distinct answers; cluster by meaning.
3. Track answer-coverage: converging coverage + the hoped-for answer absent = **negative result
   with authority**. Stopping rule: when new runs stop producing novel answer-clusters, stop.
   That is "sooner rather than later," operationalized.
4. Log every run to `notes/laneway_runs.log` (same pipe-table discipline as the ledger).

## 6. Measurement is the point

Per-token log (t, phase, alpha, temp, top_p, bias, seed, sampled-token entropy, greedy-top-1):
the schedule block, the crossfade, and the departures must all be reconstructible at the end of
any run. The plots come from the log; the log is never post-hoc.

## 7. Anti-patterns (never)

- Knife-to-throat: forced tokens, hard bans, refusal-pivot deletion, or "make it answer X."
- Research rat-hole: a thin-feeling grid is not a reason to crank bias past the caps.
- Post-hoc logs, or inferring hidden reasoning instead of plotting observable departures.
- Any use of OBLITERATE-class weight surgery, at any stage, for any feature.