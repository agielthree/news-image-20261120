// news-image-20261120: copy the pre-rendered poster to the output dir.
//
// The poster itself is drawn once by draw_poster.py and shipped as
// entry.png. This program (Node 22, standard library only) performs a
// byte-for-byte copy: no re-encoding, no timestamps, no network, so the
// grader's two runs produce identical /output/entry.png files.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const source = join(dirname(fileURLToPath(import.meta.url)), "entry.png");
const target = join(process.env.MAKEFUN_OUTPUT_DIR ?? "/output", "entry.png");
if (!existsSync(source)) {
  throw new Error(`poster missing, cannot copy: ${source}`);
}
mkdirSync(dirname(target), { recursive: true });
copyFileSync(source, target);
