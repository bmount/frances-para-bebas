#!/usr/bin/env python3
"""Guarded synthesis: the ONLY sanctioned way to make audio in this project.

Two hard safeguards run before every ElevenLabs call:
  1. FRENCH  — model must be one that enforces `language_code`, and we always
     pass language_code="fr". No English default can leak in.
  2. GENDER  — assert_gender_ok(text, voice.gender) must pass, or we refuse.

If either safeguard fails we raise, we do NOT emit audio.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tts import tts as _raw_tts          # noqa: E402
from voices import get_voice             # noqa: E402
from gender_guard import assert_gender_ok  # noqa: E402
from google_tts import google_tts, GOOGLE_VOICES  # noqa: E402

# Only these ElevenLabs models actually honor language_code. multilingual_v2
# IGNORES it and must never be used for French-forced output.
ENFORCING_MODELS = {"eleven_turbo_v2_5", "eleven_flash_v2_5"}
DEFAULT_MODEL = "eleven_turbo_v2_5"
BACKENDS = ("elevenlabs", "google")


def synth(text, out_path, voice_key, backend="elevenlabs", model=DEFAULT_MODEL):
    """Generate one clip via the chosen backend. Both safeguards run first:
    FRENCH (enforced per-backend) and GENDER (assert_gender_ok)."""
    if backend not in BACKENDS:
        raise ValueError(f"backend must be one of {BACKENDS}, got {backend!r}")
    v = get_voice(voice_key)
    gender = v["gender"]
    # SAFEGUARD(gender): refuse mismatched self-descriptions (backend-agnostic)
    assert_gender_ok(text, gender)

    if backend == "google":
        # SAFEGUARD(french): fr-FR voice can't speak another language
        res = google_tts(text, out_path, GOOGLE_VOICES[gender])
    else:
        if model not in ENFORCING_MODELS:
            raise ValueError(
                f"SAFEGUARD(french): model {model!r} does not enforce language_code")
        res = _raw_tts(text, out_path, model=model, voice=v["voice_id"], language_code="fr")
        res["backend"] = "elevenlabs"
    res.update({"voice": voice_key, "voice_gender": gender, "text": text})
    return res


if __name__ == "__main__":
    text, out, vk = sys.argv[1], sys.argv[2], sys.argv[3]
    print(synth(text, out, vk))
