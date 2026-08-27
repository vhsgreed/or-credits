#!/usr/bin/env python3
"""or-credits.py — print OpenRouter credit balance (paid spend is visible via /api/v1/credits).

Usage:
  python3 scripts/or-credits.py            # human line: "$114.70 balance / $2.30 used / $117.00 total"
  python3 scripts/or-credits.py --json     # raw JSON of the credits payload

Key: ~/.openclaw/secrets/openrouter-key (sk-or-v1-...), or $OR_KEY_FILE.
"""
import json
import os
import re
import sys
import urllib.request

KEY_FILE = os.environ.get("OR_KEY_FILE", os.path.expanduser("~/.config/openrouter/key"))


def load_key():
    with open(KEY_FILE) as f:
        m = re.search(r"sk-or-v1-[A-Za-z0-9_-]+", f.read())
    if not m:
        sys.exit("or-credits: no key found in " + KEY_FILE)
    return m.group(0)


def main():
    key = load_key()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/credits",
        headers={"Authorization": "Bearer " + key},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    if "--json" in sys.argv:
        print(json.dumps(data, indent=2))
        return
    d = data.get("data", {})
    total = d.get("total_credits")
    usage = d.get("total_usage")
    balance = d.get("total_balance")
    if balance is None and total is not None and usage is not None:
        balance = total - usage
    if total is None:
        print("or-credits: unexpected payload:", json.dumps(data)[:300])
        sys.exit(1)
    print(f"${balance:.2f} balance / ${usage:.2f} used / ${total:.2f} total credits")


if __name__ == "__main__":
    main()
