#!/usr/bin/env python3
"""Generate a pronunciation-method comparison matrix for judging by ear.

For each test word we render several methods so we can pick the one that
reliably produces correct FRENCH pronunciation of English-homograph cognates.
"""
import json, os
from tts import tts

OUT = "compare_audio"
os.makedirs(OUT, exist_ok=True)

# The nastiest cases: identical (or near) spelling in English, must sound French.
WORDS = [
    {"fr": "nation",      "es": "nación",      "ipa": "nasjɔ̃",       "carrier": "la nation"},
    {"fr": "station",     "es": "estación",    "ipa": "stasjɔ̃",      "carrier": "la station"},
    {"fr": "question",    "es": "pregunta",    "ipa": "kɛstjɔ̃",      "carrier": "la question"},
    {"fr": "table",       "es": "mesa",        "ipa": "tabl",         "carrier": "la table"},
    {"fr": "information", "es": "información", "ipa": "ɛ̃fɔʁmasjɔ̃",  "carrier": "une information"},
]

# method_id -> (label, function producing (text, model, language_code))
METHODS = {
    "A_ml_plain":  ("multilingual_v2 · plain (current/broken)",
                     lambda w: (w["fr"], "eleven_multilingual_v2", None)),
    "B_flash_fr":  ("flash_v2_5 · language_code=fr",
                     lambda w: (w["fr"], "eleven_flash_v2_5", "fr")),
    "C_turbo_fr":  ("turbo_v2_5 · language_code=fr",
                     lambda w: (w["fr"], "eleven_turbo_v2_5", "fr")),
    "D_flash_ipa": ("flash_v2_5 · IPA phoneme tag",
                     lambda w: (f'<phoneme alphabet="ipa" ph="{w["ipa"]}">{w["fr"]}</phoneme>',
                                "eleven_flash_v2_5", "fr")),
    "E_ml_carrier":("multilingual_v2 · French carrier «la …»",
                     lambda w: (w["carrier"], "eleven_multilingual_v2", None)),
}

manifest = {"methods": {k: v[0] for k, v in METHODS.items()}, "words": []}

for w in WORDS:
    entry = {"fr": w["fr"], "es": w["es"], "ipa": w["ipa"], "clips": {}}
    for mid, (label, fn) in METHODS.items():
        text, model, lang = fn(w)
        fname = f"{OUT}/{w['fr']}__{mid}.mp3"
        res = tts(text, fname, model=model, language_code=lang)
        entry["clips"][mid] = os.path.basename(fname)
        print(f"  {w['fr']:14} {mid:14} {res['bytes']:6}B  <- {text}")
    manifest["words"].append(entry)

with open(f"{OUT}/manifest.json", "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("wrote", f"{OUT}/manifest.json")
