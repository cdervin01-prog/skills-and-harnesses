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

```sh
mkdir -p ~/.agents/skills
cp -r skills/* ~/.agents/skills/
```

## Troubleshooter

Rules-and-structure-only troubleshooting for ANY failing system (service,
connection, device, tool, build). Kills free-form guessing on arrival.

- **Local first** — reproduce, cheapest discriminator, act if obvious.
- **Web is an escalation** — four source-family agents only at a *logged dead end*,
  with a narrow warrant (exact error + one component). Distro/vendor names are
  not a query. One research wave per bound attempt.
- **Two stores** — fat research packet keeps quotes; thin lead index proposes
  tests; the probe ledger only records live probes. Pages never prune.
- **Prune audit at reset** — the four agents prosecute the dead list so a bad
  prune cannot loop the session. Reopen still needs a live cheap probe.
- **R1 Evidence-only pruning** — branches close only on logged evidence.
- **R2 Cheapest-test-first** — reproduce → isolate → capture → verdict → act.
- **R3 Reset, don't rat-hole** — 2 consecutive empty prunes → bound reset;
  max 2 resets, then escalate.
- **R4 Token ceiling** — invented search is a bolt; row/quote caps; skip the wave
  if it costs more than finishing local tests.
- **Live ledger + pruned-facts table** — one row per decision.

## Laneway Harness

Contract for a gentle, bounded steering harness: tokens flow into their own lanes,
never get forced, banned, or rewritten.

- **Constitution** — every feature passes the contract or loses.
- Nudge-not-knife — capped bias coefficients, reduced weight never zero.
- Answers emerge, never commanded — "does X exist in the lane" is the only valid
  input; a negative across a full coverage grid is a recorded result.
- Guardrail lives at the app layer as a separate soft content gate.
- Coverage sweeps (seed × bias × ramp) with a stopping rule and a run log.
