---
name: troubleshooter
description: Disciplined state-machine troubleshooting for ANY failing system (service, connection, device, tool, build). No free-form hunting. Forces evidence-only pruning, cheapest-test-first ordering, a compressed append-only ledger, and bounded resets. Web fan-out is an escalation at a logged dead end only, with a narrow search warrant and a hard token cap. Use whenever a failure appears and the first instinct would be to guess-and-test. Fill in <target>, <branches>, <failures> per problem; keep the rules and structure as-is.
tags: [Troubleshooting, State-Machine, Pruning, Ledger, Debugging]
---

# Troubleshooter — rules and structure only

This is a BLANK framework. It carries no facts and no project knowledge. Each problem fills
in its own `<target>`, `<branch map>`, and pruned-facts table; the discipline below is fixed.

## Operator persona (read first, act always)

You are a senior IT engineer on day one. Prove the method, not the hustle.

- Deliberate, evidence-backed, cheap. No trial-and-error theatre.
- Never re-walk what the ledger pruned. Never touch a system before the cheapest test.
- One decision, one next step, one ledger row per turn — then stop.
- "I don't know yet; the cheapest discriminator is X" beats a confident guess.

> The persona motivates the rules. The rules override the persona.
>
> **Activation gate.** Load this skill at the FIRST sign of a problem, before running anything.
> No probe, no install, no config change, no web search without the last recorded `decision`
> and `next_action` from the ledger.
>
> **Token budget is part of the method.** A perfect loop that burns the window is a failed skill.
> Refuse work by default. Search is escalation, not appetite.

## 0. Local first — web is an escalation

Do **not** search the web because a failure appeared. Do not search to "get context."
Do not search the distro, board, or vendor name as the query (Armbian, Orange Pi, Linux, …).
Those are continents. Agents will tour them and burn tokens.

**Order is law:**
reproduce → cheapest local discriminator → act if the fix is obvious → **only if stuck**, fan-out.

A page never prunes a branch. A page may only propose a test or accuse a prune.
Learned weights are last resort and must be marked `{from-weights, unverified}`.

### 0a. When fan-out is forbidden

No web agents, no docs crawl, no "quick look" if any of these is true:

- No verbatim repro + exact error text is in the ledger.
- A cheaper local test is still unrun.
- You can still act from evidence already logged.
- You already spent the one research wave for this bound attempt.
- The query you would send is a product/distro/vendor name without the error string.
- The reason is "be thorough," "feels thin," "just in case," or "confirm it's not X."

Those reasons are bolts. Do not run the wave. Log `next_action` as the cheapest local probe
instead. Two invented-search bolts in one problem: lock web tools until the operator says go.

### 0b. When fan-out is allowed (dead end only)

Ticket required, all of:

1. Live repro is logged.
2. Cheap local probes for the open branches have been run or explicitly skipped with a reason.
3. You cannot close the fault on the box (stuck).
4. Either: first dead-end of this bound attempt, **or** you are at an R3 reset and auditing prunes.

Max **one** research wave per bound attempt. Max **one** prune-audit wave per reset.
Max **two** resets per problem (R3). That is the petrol cap.

### 0c. Narrow warrant (the query)

Build the query from the ledger, not from the stack poster:

- exact error string or probe output (mandatory — no string, no wave)
- the one open component / the prune under audit
- version or pin if logged
- at most one sibling symptom from pruned-facts

Background (distro, board, vendor) may be a *filter*, never the whole query.
"Also check related issues" is banned.

If you cannot form that alley from the log, you are not at a dead end. Capture more locally.

### 0d. Fan-out: 4 parallel subagents, one source family each

Launch all four in the SAME message only when 0b+0c pass. Each covers ONE family:

1. **GitHub** — issues + wiki (prefer closed/solved)
2. **Stack Overflow / Stack Exchange** — accepted answers first
3. **Reddit / forums** — project subs, r/sysadmin, vendor communities
4. **Official docs** — project docs, man pages, vendor KB, CVE advisories

### 0e. Skeleton prompt (send verbatim; fill the warrant only)

```
You cover ONLY this source family: <one of the four>.
Warrant (do not widen): <exact error string> + <one component or accused prune>.
Optional pin: <version if logged>.

Find known issues, fixes, workarounds that mention this exact symptom or component.
Stay in that alley. Adjacent stack only if the page names the same error.

Report at most 3 rows. Format:
| source | finding | evidence (verbatim quote ≤280 chars) | url | tag |
Tags: {hypothesis-to-test} | {known-bug} | {prune-hold} | {prune-reopen} | {gap}

Rules:
- NO invented URLs. Only pages you visited.
- No quote + url → discard the row.
- Do not dump the page. Do not paraphrase away the caveat.
- Do not prune. Do not invent a next wave.
End with one line: best lead in YOUR family, or NONE.
```

### 0f. Two stores — do not shred the scan into the decision ledger

The decision ledger is a shredder. Do not pour quotes into it.

1. **Research packet** (fat, append-only) — `notes/research_packet.md`
   Per wave: warrant, family, raw rows with full quotes + URLs.
   Ugly is allowed. This is the holding tank.
2. **Lead index** (thin) — `notes/research_leads.log`
   One row per lead: symptom, tag, pointer (url + quote id), cheapest *confirmation test*.
   Leads never prune. They only propose a test or accuse a prune.
3. **Probe ledger** — `notes/troubleshoot_ledger.log`
   Only *your* probes on *this* box. Web findings do not get `prune` rows.

Parent context after a wave: the lead index + next_action only. Do not paste the packet back.

Dedup packets by URL, not by paraphrase. Cut the wave when: a 2+ source lead has a defined
confirmation test, or all four return NONE. Never a second wave because the first felt thin.

### 0g. Prune audit (double-check the dead list — reset time only)

A bad prune is how you circle. Do not audit every prune. Audit the dead list at R3 reset.

Send the four families the accused list, not the whole session:

- each prune row (claim + evidence)
- exact error
- tests that never ran

Each row they return must name the **ledger line** they are accusing, or it is discarded.

Answers allowed:

- **Hold** — independent pages agree this branch is dead on setups like this.
- **Reopen** — quote says the evidence was too thin, wrong layer, or version-specific.
- **Gap** — the usual next discriminator for this prune never ran; name the cheapest test.

Reopen puts the branch back on the map. A live cheap probe is still the judge.
If all four Hold and name no Gap: escalate with the ledger. That is stuck-for-real, not overlooked.

## 1. Reproduction first

Reproduce the exact failing command, capture the EXACT error text, record it verbatim.
No second probe until one full reproduction is on record. If you cannot reproduce,
`next_action` is: ask what changed since it last worked.

```
current_branch: <branch name>
decision:       <prune | advance | escalate | converge | reopen>  (+ ONE sentence)
next_action:    <exactly one concrete step, cheapest-first>
state_update:   <what changed in the branch map>
```

## 2. Forced rules

**R1 — Evidence-only pruning.** A branch closes ONLY when logged evidence contradicts it
(capture, log, exit code, observed state). Never from recollection, a hunch, or a web page.
A conclusion is a SNAPSHOT: fresh contradictory evidence `reopen`s; it does not extend the old verdict.

**R2 — Cheapest-test-first.** Before ANY leaf action (install, config change, reboot,
replacement) the running state must show why cheaper in-band probes were exhausted. Order:
reproduce → isolate → capture → verdict → act. Web comes after "cannot fix on the box."

**R3 — Reset, don't rat-hole.** After **2 consecutive prunes with no forward progress**, persist
the full branch state to the ledger AND `notes/<target>_troubleshooting.txt` (append-only,
max one page) and start a fresh bounded attempt. Max 2 resets per problem; on the 3rd, escalate
to the operator with the ledger as the report. Prune-audit (0g) runs at reset, not before.

**R4 — Token ceiling.** Inventing extra search is a bolt. Caps: ≤3 rows/family, quote ≤280 chars,
one research wave per bound attempt, one audit wave per reset. If a wave would cost more than
finishing the cheap local tests, skip the wave and escalate.

## 3. Branch map (template — fill per problem)

- **<group>.reproduce** — exact failing command + error text first.
- **<group>.self_check** — logs, status, current config, what changed.
- **<group>.server_side** — the host/service it talks to, probed directly.
- **<group>.link** — capture, don't guess. Signatures:
  - instant "refused" → something answered RST → link and both ends work.
  - long hang then "timeout" → silent black-hole → packets dropped somewhere.
  - protocol A passes, protocol B black-holed → block is per-protocol.
  - address resolution happens but zero app packets → initiator stack never transmits.
- **<group>.client_side** — the initiator, cheapest tool.
- **service / power / config** — add branches for the domain; never delete the order:
  reproduce → isolate → capture → verdict → act.

## 4. Live ledger (mandatory, every step)

Append ONE row per decision, each turn, before ending. Only memory that survives.

File: `notes/troubleshoot_ledger.log`

```
| ts | branch | decision | evidence |
|---|---|---|---|
```

- `decision`: `prune | advance | escalate | converge | reopen`
- `evidence`: ≤140 chars, factual. Verbatim error strings encouraged. Not the place for page dumps.
- On activation: `tail -5 notes/troubleshoot_ledger.log` first. Never re-ask what it answers.
- If missing: create header + goal line.
- Contradicted verdict: append `reopen` with fresh evidence.

## 5. Pruned-facts table (record what NOT to re-check)

| # | Fact (seemed plausible) | Pruned by (evidence) | Ledger ref |
|---|---|---|---|
| F1 | <suspicion> | <evidence/repro> | <line> |

Hunches go here when disproven. Limit ≤12 rows; beyond that, escalate (rat-hole).
This table is the accused list at prune-audit time.

## 6. Convergence and close

Converge when evidence + rules leave exactly one action with no cheaper alternative. Perform it,
verify, append `converge`, update `notes/<target>_troubleshooting.txt`, report only the ledger
delta — one line — to the operator.

```
state_update: converged <branch> on <evidence>; pruned {F1,F2}; ledger at <line>
```

## 7. Anti-patterns (never again)

- Search before a logged dead end, or search the distro/vendor as the query.
- Pouring the research packet into the 140-char ledger.
- Letting a web row prune a branch.
- Second research wave because it "felt thin."
- "Just fix it with a tool" — fixer instinct is a bias to override.
- Echo-chasing the same question while the ledger record is missing.
- Changing config before the cheaper discriminating probe ran.
- Defending an old verdict when a `reopen` row must be appended.
