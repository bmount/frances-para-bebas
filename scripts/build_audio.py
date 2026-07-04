#!/usr/bin/env python3
"""Generate all lesson audio through the guarded synth pipeline.

Emits audio_build/<id>.mp3 and data/audio_manifest.json. Every clip passes the
FRENCH and GENDER safeguards or the build fails loudly (we never ship a clip
that skipped a guard).

Voice assignment rules:
  - gendered variants: fr_m -> male voice (oris), fr_f -> female voice (emilie)
  - everything else:    explicit `voice` field, else alternate for diversity
"""
import concurrent.futures as cf
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from synth import synth               # noqa: E402
from gender_guard import GenderAgreementError  # noqa: E402

ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "audio_build")
LESSONS = sorted(glob.glob(os.path.join(ROOT, "data", "curriculum", "lesson_*.json")))
os.makedirs(OUT, exist_ok=True)

ALT = ["emilie", "oris"]


def conj_text(pron, form):
    p = pron.split("/")[0].strip()
    return p + form if p.endswith("'") else f"{p} {form}"


def collect():
    """Yield (audio_id, text, voice_key) for every clip across all lessons."""
    jobs = []
    for i, path in enumerate(LESSONS):
        with open(path, encoding="utf-8") as f:
            L = json.load(f)
        # conjugation
        for j, row in enumerate(L["grammar"]["conjugation"]["present"]):
            jobs.append((row["audio"], conj_text(row["pron"], row["form"]), ALT[j % 2]))
        # vocab
        for it in L["vocab"]:
            if "fr_m" in it:
                jobs.append((it["audio_m"], it["fr_m"], "oris"))
                jobs.append((it["audio_f"], it["fr_f"], "emilie"))
            else:
                jobs.append((it["audio"], it["fr"], it.get("voice", "emilie")))
        # sentences
        for it in L["sentences"]:
            if "fr_m" in it:
                jobs.append((it["audio_m"], it["fr_m"], "oris"))
                jobs.append((it["audio_f"], it["fr_f"], "emilie"))
            else:
                jobs.append((it["audio"], it["fr"], it.get("voice", "emilie")))
    return jobs


def run_one(job, force=False):
    aid, text, voice = job
    out = os.path.join(OUT, f"{aid}.mp3")
    if os.path.exists(out) and not force and os.path.getsize(out) > 800:
        return {"id": aid, "text": text, "voice": voice, "file": f"{aid}.mp3", "cached": True}
    res = synth(text, out, voice)  # guards run inside; raises on violation
    return {"id": aid, "text": text, "voice": voice, "voice_gender": res["voice_gender"],
            "file": f"{aid}.mp3", "bytes": res["bytes"]}


def main():
    force = "--force" in sys.argv
    jobs = collect()
    ids = [j[0] for j in jobs]
    dupes = {x for x in ids if ids.count(x) > 1}
    if dupes:
        raise SystemExit(f"DUPLICATE audio ids: {sorted(dupes)}")
    print(f"{len(jobs)} clips across {len(LESSONS)} lessons")

    results, errors = [], []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(run_one, j, force): j for j in jobs}
        for fut in cf.as_completed(futs):
            j = futs[fut]
            try:
                r = fut.result()
                results.append(r)
                tag = "cache" if r.get("cached") else f'{r.get("bytes","?")}B'
                print(f"  ✓ {r['id']:18} [{r['voice']:6}] {tag}  {r['text']}")
            except GenderAgreementError as e:
                errors.append((j, f"GENDER: {e}"))
                print(f"  ✗ {j[0]:18} BLOCKED {e}")
            except Exception as e:  # noqa
                errors.append((j, str(e)))
                print(f"  ✗ {j[0]:18} ERROR {e}")

    if errors:
        print(f"\n{len(errors)} FAILURES — no manifest written:")
        for j, e in errors:
            print(f"  {j[0]}: {e}")
        raise SystemExit(1)

    results.sort(key=lambda r: r["id"])
    manifest = {"audio_base": "", "count": len(results),
                "clips": {r["id"]: r["file"] for r in results}}
    with open(os.path.join(ROOT, "data", "audio_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\nwrote data/audio_manifest.json ({len(results)} clips)")


if __name__ == "__main__":
    main()
