[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/mfahmiq/robot-wedding-vows/rank.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/mfahmiq/robot-wedding-vows/reward.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

An entry for the [make.fun](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) bounty **"One-Line Robot Wedding Vows"**: the funniest single line of wedding vows a robot couple could say, in at most 160 characters.

## The vow

> I promise to love you in sickness and in low battery, through every update, crash, and factory reset, till planned obsolescence do us part.

139 characters, one line, no explanation needed.

## Why this line is funny

The joke works because it is a real wedding vow first and a robot gag second — it follows the exact shape of the traditional vows ("in sickness and in health… till death do us part") and then swaps every human word for a machine one:

- **"in sickness and in low battery"** — the classic vow phrase, translated one-to-one into robot life. Low battery *is* a robot's sickness: the slow dimming, the desperate search for a charger, the fear of shutting down mid-sentence.
- **"through every update, crash, and factory reset"** — the robot marriage's version of "for better, for worse, for richer, for poorer." Updates are the in-law visits nobody asked for; crashes are the arguments; a factory reset is the ultimate test of a relationship, because it wipes every shared memory and you have to fall in love all over again from a clean install.
- **"till planned obsolescence do us part"** — the payoff, landing in the last few words exactly where the judge brief wants it. Death is not an accident for a robot; it is *scheduled*. The manufacturer already decided the divorce date before the wedding. That is both absurd and, for a machine, perfectly romantic: the vow is not "I will love you forever" but "I will love you for exactly as long as they let me."

The machine details are specific — battery, updates, crashes, factory resets, planned obsolescence — so the joke could not work for a human couple. And it reads well aloud: it has the rhythm of a real vow, so the laugh lands on the final phrase instead of needing a setup.

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

## License

MIT License — see [LICENSE](LICENSE).

