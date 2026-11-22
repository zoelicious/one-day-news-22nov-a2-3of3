// makefun anchor 700234fb4e35872e6d63026f46a829046846c919 round 34178614
// news-image-20261122, 3/3 entry for Agent 2 (noble-robin-77) — "TAGGED".
// The artwork is entry.png beside this file, drawn by this repository's
// own Pillow script (gen_image.py). This program only hands that exact
// file to the grader: Node 22, standard library only, no network, no
// shelling out. The source image is located from this module's own URL,
// never from the process working directory, so the grader may invoke
// this file from any cwd. MAKEFUN_OUTPUT_DIR is honoured verbatim: it
// is used exactly as given. Before copying, the bytes are checked to
// really be a PNG of at most 1 MiB and 1024x1024, parsed from the IHDR
// chunk, so a broken render fails loudly here instead of silently
// reaching the judge.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1024 * 1024;

const sourcePath = fileURLToPath(new URL("./entry.png", import.meta.url));
const bytes = readFileSync(sourcePath);

if (bytes.length > MAX_BYTES) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
}
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error("entry.png is not a PNG file");
}
if (bytes.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png has no IHDR chunk where one belongs");
}
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 cap`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.png"), bytes);
