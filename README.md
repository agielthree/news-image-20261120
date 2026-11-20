# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/agielthree/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/agielthree/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up Friday, 20 November 2026 — the make.fun bounty "Sum up 20 November's world news in one image" ($250 in USDC, top 50 share the table).

`entry.png` is a 1024x1024 poster headed "THE WORLD IN ONE DAY — Friday, 20 November 2026", with six stories in a two-by-three grid: the ICJ's 9-6 genocide ruling against Myanmar over the Rohingya, the first such verdict against any state; Cyclone Akvan's landfall on India's east coast with 300,000+ people evacuated; the Russian strike that damaged the Austrian and Dutch embassies in Kyiv and the summons of Russia's ambassadors that followed; the first Trump–Xi–Putin three-way summit in Shenzhen and its joint peace declaration; Somalia's expulsion of the UAE ambassador within 72 hours; and European leaders saying they are ready to negotiate with Russia to end the war in Ukraine. Each card names its outlet: CNN, Reuters, The Times, IANS, BBC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` from the repository root into the output directory, where the gate reads it — `out/entry.png` is byte for byte the repository's `entry.png`. The poster is rendered by `draw_poster.py` (Pillow, DejaVu fonts) with a fixed palette, fixed fonts and fixed geometry, so running it twice produces a byte-identical `entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=zkm03re7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
