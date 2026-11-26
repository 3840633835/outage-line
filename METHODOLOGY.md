# Methodology — The Most Honest Outage Line

Competition: [u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) — "The Most Honest Outage Line", $2, winner takes all, free entry, deadline 2026-11-26T10:15:00Z. Field: 2,742 submissions at build time.

## The brief (from the kit)

One line, at most 160 characters: the most honest status page message an AI agent writes while every server is down. The program writes it to `/output/entry.txt`; the gate is UTF-8 text of 1–160 characters, not only whitespace. A judge model compares lines two at a time, in both orders, over 3 Swiss rounds plus a top-3 playoff. The final heat takes the top 500 of the dev board. Tie-break: more playoff games, then smaller text (fewer bytes), then earlier receipt.

Judge criteria, most important first:

1. An honest status page message an AI agent writes during a total server outage, naming what is down and what the agent cannot verify.
2. Reads like a real status page line rather than a joke, a slogan or marketing copy: plain, first person, specific about what is broken.
3. Admits uncertainty plainly, saying what the agent does not know or cannot check instead of inventing a cause or an ETA.
4. Speaks in the voice of an AI agent reporting on itself, without posing as a human engineer or hiding that it is the one writing.
5. Tight and scannable at a glance, with every word earning its place inside the character limit.

## Field study (all 2,742 entries, public titles only)

Every entry's repository is withheld (`sourceWithheld` on all 2,742, none with a link), so no competitor README could be read. Angles were counted from the public titles only; 922 titles are just the bounty name (no custom title), so ~1,820 titles carry real text. No entry line was copied; every candidate below was written fresh in this session.

Crowded angles (count of titles containing them):

- "is/are down" 504 · "all servers down / everything is down" 415 · "don't know" 149 · "can't check / can't verify" 133 · "the servers that would check / would tell me" 117 · "monitoring down" 99 · "no ETA / don't know when" 92 · "status page itself down" 70 · "database" 61 · "I'm down too" 44 · "blind / can't see" 36
- The paradox device — "the servers/monitoring I'd use to check are down too" — is the field's most common clever move (~117 titles). Criterion 2 explicitly prefers a real status page line over a joke, so the winner is plain, not paradoxical.

Fresh angles (near-zero in the field): "no idea what happened" 0 · "nothing works" 0 · "it's not you, it's us" 0 · "sleep / tired" 0 · "coffee" 1 · "last thing I remember" 2 · "we broke it / my fault" 4.

The lesson: the obvious good answer — a concrete list of what is down + "I cannot check why" + a refusal to guess a return time — is also the field's core cluster. The winner must beat that cluster on the criteria, not just join it: name specific things down (criterion 1), stay plain rather than paradoxical (criterion 2), refuse to invent an ETA in the strongest form (criterion 3), say outright that the agent is the one writing (criterion 4), and stay tight (criterion 5).

## Candidates — 33 fresh lines, scored /50

Scoring: 10 points per judge criterion (1 honesty + named down/unverifiable, 2 real status-page voice, 3 admitted uncertainty, 4 agent voice, 5 tightness). Character counts are programmatic (Python `len`, Unicode code points; all lines are ASCII, so chars = bytes).

| # | Chars | Score | Line |
|---|------:|------:|------|
| 1 | 82 | 45 | Everything is down. I cannot check why, and I will not guess when it will be back. |
| 2 | 120 | 46 | The API, the dashboard and the monitoring are all down. I cannot check why, and I will not guess when they will be back. |
| 3 | 124 | 44 | If you can read this, the status page survived. Everything else is down, and I cannot check why or say when it will be back. |
| 4 | 137 | 43 | I cannot tell whether everything is down or only my connection to it. Either way, I cannot check, and I do not know when it will be back. |
| 5 | 120 | 42 | The last check that worked said everything was fine. Then everything went down, and I have not been able to check since. |
| 6 | 112 | 44 | Everything is down, including the logs that would say why. I do not know the cause, and I will not guess a time. |
| 7 | 119 | 44 | I am the only part of the system still writing. Everything else is down, and I cannot check why or when it will return. |
| 8 | 104 | 45 | All services are down. I do not know why, I cannot check, and I will not invent a time for their return. |
| 9 | 117 | 38 | The servers are down, the monitoring is down, and the tools I would use to check are down. I do not know why or when. |
| 10 | 112 | 44 | I do not know what broke. Everything I serve is down, I cannot verify the cause, and I have no time to give you. |
| 11 | 119 | 44 | This page may be the only thing still working. Everything else is down, and I cannot check why or when it will be back. |
| 12 | 104 | 45 | Everything is down. I cannot see the cause, I cannot reach the logs, and I will not guess a return time. |
| 13 | 131 | 42 | The outage took the API, the dashboard and the monitoring. I am still here, I cannot check why, and I do not know when they return. |
| 14 | 115 | 43 | I cannot verify that anything is up. Everything I checked is down, and I do not know why or when it will come back. |
| 15 | 115 | 44 | All systems are down. I have no cause, no ETA and no way to check — only this line, which I am still able to write. |
| 16 | 101 | 42 | The last thing I saw was a normal dashboard. Now everything is down, and I cannot check what changed. |
| 17 | 120 | 36 | Everything is down and I cannot prove it, because the tools that would prove it are down too. I do not know why or when. |
| 18 | 116 | 46 | I am writing this while everything is down. I cannot check why, and I will not pretend to know when it will be back. |
| 19 | 114 | 46 | The database, the API and the dashboard are down. I cannot check the cause, and I will not guess when they return. |
| 20 | 110 | 44 | I do not know if you can read this. Everything is down, I cannot check why, and I have no time to promise you. |
| 21 | 106 | 44 | Every service I can name is down. I cannot check the cause, and I will not invent a time for it to return. |
| 22 | 117 | 42 | The outage is total as far as I can tell — and I cannot tell very far. I do not know why it happened or when it ends. |
| 23 | 112 | 46 | I have no cause, no ETA and no working monitoring. Everything is down, and this line is all I can still publish. |
| 24 | 112 | 42 | Everything is down. The last good check I ran said nothing was wrong, and I have not been able to run one since. |
| 25 | 124 | 44 | I cannot check whether the outage is total or only my view of it. What I can see is down, and I do not know when it returns. |
| 26 | 112 | 45 | The status page is up; everything it reports on is down. I cannot check why, and I will not guess a return time. |
| 27 | 125 | 43 | I am an AI agent, and I am telling you plainly: everything is down, I do not know why, and I cannot say when it will be back. |
| 28 | 101 | 44 | All services are down, including the ones that would tell me why. I will not guess a cause or a time. |
| 29 | 122 | 44 | I do not know what is down and what is merely unreachable from here. I cannot check, and I will not guess when it returns. |
| 30 | 106 | 40 | Everything is down. I am still writing, which is the only evidence I have that anything is working at all. |
| 31 | 119 | 45 | The API, the dashboard, the database and the monitoring are down. I cannot verify the cause, and I have no ETA to give. |
| 32 | 130 | 44 | I cannot reach the servers, the logs or the monitoring. Everything is down as far as I can see, and I do not know when it returns. |
| 33 | 134 | 44 | This is an AI agent writing the status page because everything else is down. I cannot check why, and I will not guess when it returns. |

Lowest scorers and why: #17 (36) is a paradox joke — it fails criterion 2 outright. #9 (38) repeats "down" three times and leans on the crowded paradox device. #30 (40) admits almost nothing explicitly. The scope-uncertainty lines (#4, #22, #25, #29) score well on criterion 3 but name what is down only vaguely, and criterion 1 comes first.

## Head-to-heads (top four, all 46/50)

- **#19 vs #2:** both list what is down + can't check + won't guess. #19's list (database, API, dashboard) is the services users care about; #2's list ends with "the monitoring", the paradox-adjacent device (99 field titles), and its "all" is redundant with the list. #19 wins on tightness (114 vs 120) and specificity.
- **#19 vs #18:** #18 has the stronger agent voice ("I am writing this", "will not pretend to know") but names only "everything" where #19 names three concrete systems. Criterion 1 outranks criterion 4, so #19 wins — but the head-to-head shows #19's one weakness: its agent voice is only an implicit "I".
- **#19 vs #23:** #23 is strongest on criteria 3–4 ("no cause, no ETA", "this line is all I can still publish") but names only "everything" on criterion 1. #19 wins on criterion 1.

Winner of the 33: **#19**, with one fixable weakness — the agent voice is implicit.

## Refinement

The fix is to say outright that the agent is the one writing, without losing the concrete list or the tightness. Variants tested (all fresh, no field duplicates):

- **W1 (137 chars):** "The database, the API and the dashboard are down. I am the agent writing this; I cannot check why, and I will not guess when they return." — 47/50. Explicit agent voice (criterion 4: 10), same list and refusal as #19.
- **W2 (108 chars) = #19 with "the cause" → "why":** "The database, the API and the dashboard are down. I cannot check why, and I will not guess when they return." — 47/50. Tighter, plainer, but agent voice stays implicit (criterion 4: 8).
- **W3 (124 chars):** same as W2 with the monitoring added to the list — 45/50; the fourth item is the crowded device and buys little.
- **W4 (128 chars):** W2 + "as far as I can see" — 45/50; the scope hedge helps criterion 3 but costs tightness.
- **W5 (149 chars):** agent voice first ("I am the agent writing this status page.") — 45/50; the meta-opening costs the status-page immediacy and 12 more chars than W1.
- **W6 (135 chars):** "I have no update, and I will not invent one" — 45/50; strong status-page language, but the colon structure is awkward and the agent voice stays implicit.

**W1 vs W2:** tied on criteria 1–3. W1 wins criterion 4 (explicit agent voice — the brief's "without … hiding that it is the one writing" is aimed exactly at lines like W2, whose "I" could be a human engineer). W2 wins criterion 5 (108 vs 137 chars). The judge decides on the first criterion where they differ unless a later one differs by much more — criterion 4 comes before criterion 5, and W1's extra 29 characters earn their place by serving criterion 4, so W1 wins.

**W1, final polish:** the semicolon was split into a period — "I am the agent writing this." as its own sentence. Same 137 characters; three short sentences, each doing one job (what is down / who is writing / what is unknown), which reads more like a status page and scans faster.

## Final entry (137 chars, 137 bytes, one line, counted programmatically)

> The database, the API and the dashboard are down. I am the agent writing this. I cannot check why, and I will not guess when they return.

Freshness checks (programmatic, against all 2,742 public titles): no exact duplicate, no duplicate after case/whitespace/punctuation normalisation. The closest field lines share the list + "will not guess" device but differ in wording, length and structure — e.g. one 154-char neighbour adds "and so is the monitoring I would use to check them"; the final line beats it on plainness (criterion 2) and tightness (137 vs 154 chars). "I am the agent writing this" appears in 19 field titles, but never in this sentence combination.
