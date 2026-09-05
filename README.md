# or-credits

Print your OpenRouter credit balance from the command line.

```
python3 or-credits.py            # human line: "$114.70 balance / $2.30 used / $117.00 total"
python3 or-credits.py --json     # raw JSON of the credits payload
```

## Key location

Reads your OpenRouter API key from:

1. `OR_KEY_FILE` env var, or
2. `~/.config/openrouter/key` (default)

The key file should contain your `sk-or-v1-...` key on one line.

## Why

The OpenRouter usage API only shows *billed* spend — free-tier usage is
invisible. This gives you the actual account balance and total credits
so you know where you stand.

## Links

Part of the [vhsgreed](https://vhsgreed.win) toolset: data, code, and methods in the open.
