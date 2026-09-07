# Ledger compressor

Runs **every time** a row would hit the ledger. Not optional. Not a model.
A model-compressor spends the tokens this exists to save.

```sh
python harness/compress_ledger.py \
  --branch ssh.link \
  --decision prune \
  --evidence 'nc: connect to 192.168.1.8 port 22: Connection refused' \
  --file notes/troubleshoot_ledger.log
```

Rules the script already applies:

- one line, pipe table
- `decision` must be `prune|advance|escalate|converge|reopen|suspect` — else `suspect`
- evidence ≤140 chars, branch ≤40, whitespace squashed, `|` stripped
- no essays, no stack traces in the live row (those stay in packet/disk if needed)

Harness law: raw chat does not append. Only compressor output appends.
Working-set inject uses the compressed file, never the conversation.
