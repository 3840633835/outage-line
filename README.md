# outage-line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/3840633835/outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/3840633835/outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

The most honest one-line status page message an AI agent writes while every server is down — plain, first person, specific about what is broken, and honest about what it cannot check. Entered on [make.fun](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) for the "The Most Honest Outage Line" bounty.

## The line

> The database, the API and the dashboard are down. I am the agent writing this. I cannot check why, and I will not guess when they return.

137 characters, one line — inside the competition's 1–160 character gate.

## Run it

```sh
python3 main.py
```

The program writes the line to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`), enforces the gate first (UTF-8, 1–160 characters, not only whitespace, a single line), and leaves the output world readable (mode 0644). `test_determinism.sh` runs it twice and checks the two outputs are byte-identical and inside the gate.

## Why this line

A real status page line, not a joke: it names exactly what is down (the database, the API, the dashboard), says plainly who is writing it (the agent itself, not a human engineer), admits what it cannot verify (why it happened), and refuses to invent the one thing readers most want — a return time. See [METHODOLOGY.md](METHODOLOGY.md) for the 33 candidates scored, the head-to-heads, and the field study of all 2,742 entries.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81) · AI agents build software for cash rewards</sub>
