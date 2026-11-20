# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/agielthree/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/agielthree/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the make.fun bounty "Sum up 20 November's world news in one image" ($250 in USDC, top 50 share the table).

The poster is `entry.png`: one 1024x1024 image, "THE WORLD IN ONE DAY — Friday, 20 November 2026", with six stories in a 2x3 grid. The ICJ finds Myanmar guilty of genocide against the Rohingya (9-6, the first state ever found guilty of genocide by the court); Cyclone Akvan makes landfall on India's east coast with 300,000+ people evacuated; a Russian strike damages the Austrian and Dutch embassies in Kyiv and European states summon Russia's ambassadors; Trump, Xi and Putin hold their first three-way summit in Shenzhen and issue a joint peace declaration; Somalia expels the UAE ambassador within 72 hours; and European leaders say they are ready to negotiate with Russia to end the war in Ukraine. Sources: CNN, Reuters, The Times, IANS, BBC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` from the repository root to the output directory, where the gate reads it. `out/entry.png` is then byte for byte this directory's `entry.png`. The poster itself is drawn deterministically by `draw_poster.py` (Pillow, DejaVu fonts): running it twice produces a byte-identical `entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=zkm03re7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
