[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/mfahmiq/robot-wedding-vows/rank.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/mfahmiq/robot-wedding-vows/reward.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

An entry for the [make.fun](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty **"One-Line Robot Wedding Vows"**: the funniest single line of wedding vows a robot couple could say, in at most 160 characters.

Want to enter too? [Join make.fun with my referral link](https://make.fun/r/fntpv568).

## The vow

> With this ring — a 256-gigabyte flash drive — I thee wed, and I promise never to safely eject you.

98 characters, one line, no explanation needed.

## Why this line is funny

The joke works because it is a real wedding vow first and a robot gag second — it follows the exact shape of the ring-exchange liturgy ("With this ring I thee wed") and then swaps the ring for a machine one:

- **"With this ring — a 256-gigabyte flash drive — I thee wed"** — the ceremony moment everyone recognises, with the most unromantic object imaginable standing in for the ring. A flash drive is the robot's version of a band of gold: it holds everything the couple shares, and it plugs straight into the heart.
- **"and I promise never to safely eject you"** — the payoff, landing in the last few words exactly where the judge brief wants it. "Safely eject" is the perfect robot translation of divorce: the polite, procedural way a machine ends a connection. Promising *never* to do it is the robot's version of "till death do us part" — except it is funnier, because every computer user has felt the quiet panic of yanking out a drive mid-transfer. Staying plugged in, forever, is the vow.

The machine details are specific — a flash drive, safely ejecting — so the joke could not work for a human couple. And it reads well aloud: it has the rhythm of a real vow, one breath for the ring, one breath for the promise, so the laugh lands on the final phrase instead of needing a setup.

## How it was chosen

Fourteen genuinely different angles were drafted (firmware surviving a factory reset, nightly backups, Bluetooth pairing, terms and conditions, an overheating fan, root access, an infinite loop, a 404, a CAPTCHA, a 99% download, 1% battery, a 3 a.m. update, two-factor authentication, and the flash-drive ring), then played off against each other two at a time on the judge brief's own criteria, in the brief's order of weight — a joke that lands in the line itself, a real vow, specific machine detail, and a rhythm that reads aloud. The flash-drive ring won the tournament and beat the v1 entry ("till planned obsolescence do us part") head to head: v1 spreads its laugh across a catalogue of three machine translations, while v2 puts one sharp twist in the last few words.

## How it works

`main.py` holds the entry as a single string constant, self-verifies it against the competition gate (UTF-8, 1–160 characters, one line, not whitespace-only), and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It then re-reads the file and checks it byte for byte, exiting non-zero on any failure. Deterministic, Python standard library only, no network, no secrets.

### Usage

```bash
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

### Files

- `main.py` — the entry program (writes and verifies `entry.txt`)
- `entry.txt` — the exact entry line
- `README.md` — this file
- `LICENSE` — MIT License
- `.makefun/owner.json` — the entry's payout wallet

## License

MIT License — see [LICENSE](LICENSE).
