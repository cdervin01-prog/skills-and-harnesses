# Skills and Harnesses

Two disciplined agent skills, shipped as installable SKILL.md files. Both are
**blank frameworks** — no project facts, no secrets, no vendor lock-in; they fill
in per problem.

## Structure

```
skills/
  troubleshooter/    SKILL.md   — state-machine troubleshooting discipline
  laneway-harness/   SKILL.md   — gentle bounded token-steering harness
```

## Install

Copy a skill directory into your agents' skills path, e.g.:

```sh
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

## Troubleshooter

Rules-and-structure-only troubleshooting for ANY failing system (service,
connection, device, tool, build). Kills free-form guessing on arrival:

- **Research-first** — parallel fan-out of 4 source-family subagents, merged into
  a research ledger, hypotheses only (never verdicts).
- **Reproduction first** — exact error text captured before any second probe.
- **R1 Evidence-only pruning** — branches close only on logged evidence; a verdict
  is a snapshot, reopen on fresh contradiction.
- **R2 Cheapest-test-first** — reproduce → isolate → capture → verdict → act.
- **R3 Reset, don't rat-hole** — after 2 consecutive prunes, bound the attempt;
  max 2 resets, then escalate.
- **Live ledger + pruned-facts table** — one row per decision, the only memory
  that survives the session.
- **Operator persona** — the frame motivates the rules; the rules override the
  persona, and the activation gate is *before* the first probe.

## Laneway Harness

Contract for a gentle, bounded steering harness: tokens flow into their own lanes,
never get forced, banned, or rewritten.

- **Constitution** — every feature passes the contract or loses.
- Nudge-not-knife — capped bias coefficients, reduced weight never zero, no
  blocked lists, no weight surgery (OBLITERATE-class tools excluded).
- Answers emerge, never commanded — "does X exist in the lane" is the only valid
  input; a negative across a full coverage grid is a recorded result, not a prompt
  to push harder.
- Guardrail lives at the app layer as a separate soft content gate, not in the
  weights.
- Coverage sweeps (seed × bias × ramp) operationalize "sooner rather than later"
  with a stopping rule and a run log in the same pipe-table discipline as the
  troubleshooting ledger.