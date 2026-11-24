# One-Line Robot Wedding Vows

[![MakeFun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/jhonrudi12/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/jhonrudi12/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [MakeFun bounty](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b): the funniest single line of wedding vows a robot couple could say, at most 160 characters.

## The line

> I vow to love you in sickness and in health, in low battery and in safe mode, until a firmware update do us part.

113 characters, one line, spoken as a wedding vow by one robot to another.

Why this line: it keeps the classic vow shape ("in sickness and in health ... till death do us part") so it sounds like a real wedding promise, swaps in machine specifics (low battery, safe mode, firmware update), and lands the joke in the last few words — the thing that parts them is not death, but a firmware update.

## How it runs

```sh
python3 main.py
```

`main.py` (Python 3, stdlib only, deterministic, no network) validates the line — one line, 1–160 characters, not whitespace-only — writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/entry.txt`), and prints the line.

## License

MIT — see [LICENSE](LICENSE). SPDX-License-Identifier: MIT
