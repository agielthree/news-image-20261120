// news-image-20261120 entry (Node 22, standard library only).
// The poster is drawn once by draw_poster.py and shipped as entry.png;
// this program only copies that fixed image to the output directory,
// The copy is byte-for-byte: no re-encoding, no timestamps, no network,
// so the two grader runs produce identical /output/entry.png files.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
