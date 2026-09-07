# Harness laws

Slim on purpose. If a line does not change a move, it does not belong here.
Harness = laws. Skill = map for this job. When they clash, harness wins.

## Gates

1. **Default naw.** Extra tools, extra agents, extra search, extra files: forbidden until a ticket exists.
2. **Scout then troop.** One source-family first (official docs unless the error is clearly a project bug). The other three stay in the basket until the scout returns `NONE` or `test-ran-still-stuck`. No troop because it "felt thin."
3. **Search is escalation.** No web without a logged live repro, cheap local tests done or skipped with a real reason, and a fault you cannot close on the box. Distro/vendor/board names are not a query. Exact error + one component is the warrant.
4. **One wave.** One research wave per bound attempt. One prune-audit wave per reset. No second wave.
5. **Token ceiling.** Invented thoroughness is a bolt. Two bolts that invent work: lock the extra tools.

## Tree

6. **Update the tree every step.** Each touched branch is `open | tested | suspect | pruned | reopened`. Walking a `pruned` node without new evidence is illegal.
7. **A prune is earned or it is a sigh.** Legal prune: probe run + verbatim evidence + which claim it kills. Illegal: "dead end," "probably not," untested siblings, no command. Sighs are `suspect`, still walkable. They do not become rules.
8. **Do not lock the win off a shrug.** Calling the whole tree dead while branches are `open` or `untested` is rejected. Dead end means cheap tests are exhausted, not that one door was knocked.
9. **Wrong lane is a rule only when earned.** Earned `pruned` is harness state: log it, inject it next turn, block re-entry. Soft `suspect` is not a lock.
10. **Reopen is cheap.** New evidence, reset audit, or the operator opens the lane. A page never prunes. A page may only propose a test or accuse a prune.

## Working set (keep the live data tiny)

The chat is not the memory. When the window fills, the model restarts and walks a buried lane. Only a condensed working set is injected each turn.

- Inject only:

```
err: <exact error ≤160>
tree: name:state name:state …
dead: name:evidence≤80 …
log: <last 5 ledger rows>
next: <one action>
```

- Do not inject the research packet, full dumps, or the skill twice.
- **Compressor on every append.** Raw talk does not touch the ledger. Run `harness/compress_ledger.py` (see `harness/COMPRESS.md`). Evidence ≤140. If the working set would exceed ~1k tokens, drop oldest log rows first, never `err` or `dead`.

## Springs (drop the sentence before it lands)

11. **Praise is not a row.** If it flatters, discard the sentence; keep only a testable claim. Applause does not choose a branch.
12. **Prior: crowded street.** Default: thousands are on the same idea; some are far ahead. "Nobody else" needs evidence. Vibes do not prune that prior.
13. **Explore, do not exhibit.** The job is to learn. "Look, not a loser" and "this will make me famous" are illegal inputs. They do not get a `converge`.
14. **Do not expect it to work.** Practice is the guaranteed output. Working is allowed. Being owed a name is not. "Only a matter of time" is an unearned prune of doubt.
15. **After a break: last stone only.** Do not rebuild the fifty. Read the last law and the last ledger row. Walk from there.

## Override

Pictures (scout, basket, graveyard, alley) are handles for these laws.
If the tale and the table fight, the table wins.
