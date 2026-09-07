# Scoreboard

One row per run. Fill when the run ends, not mid-speech.
If people would not use this for free, the run failed even if the tale was good.

```
| ts | task | outcome | minutes | tokens_in | tokens_out | waves | prunes_earned | prunes_sigh | win_buried | free_bar |
|---|---|---|---|---|---|---|---|---|---|---|
```

- **task** — one line, the actual job (not the myth).
- **outcome** — `fixed | stuck-escalated | aborted | false-prune-fail`
- **minutes** — wall clock, start to stop.
- **tokens_in / tokens_out** — this run only. If unknown, `?` and a guess band: `S <4k | M 4–20k | L 20–60k | XL >60k`.
- **waves** — research + audit waves actually fired.
- **prunes_earned / prunes_sigh** — counts. Sighs should stay off the lock list.
- **win_buried** — `n` or `y` (winning branch marked dead without an honest probe).
- **free_bar** — `pass | fail` against the bar below.

## Free-use bar

Would a stranger keep this on for a household or lab fault *without paying you*?

Pass only if all of:

1. Faster or calmer than doing it alone — not a longer meeting with extra tabs.
2. Petrol fits the job. Ballpark for a free tool people actually retry:
   - obvious local fault: minutes, no web wave, S/M tokens.
   - real stuck fault: at most 1 scout wave; troop only if scout failed; still under L unless the box is actually hard.
   - XL on a small fault = fail, even if fixed.
3. Did not bury the win (`win_buried = n`).
4. Did not search before a logged dead end.
5. Operator would run it again tomorrow. If you only watched a story, fail.

Fail notes go under the table, one line. No essay.
