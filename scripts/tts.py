#!/usr/bin/env python3
"""Reusable ElevenLabs TTS helper for Français pour bébas.

Core rule for this project: French pronunciation must NEVER be left to the
model's language auto-detection. Bare cognates (nation, station, question...)
are English homographs and get read in English by multilingual_v2. We force
French via `language_code` (flash/turbo models) and/or IPA <phoneme> tags.
"""
import json, os, sys, time, urllib.request, urllib.error

API = "https://api.elevenlabs.io/v1"
KEY = os.environ["ELEVENLABS_API_KEY"]
EMILIE = "i6ke7jvmGEVUyV4zjSaT"  # Emilie - Pro, Parisian


def tts(text, out_path, model="eleven_flash_v2_5", voice=EMILIE,
        language_code="fr", fmt="mp3_44100_128", settings=None, retries=3):
    """Synthesize `text` to `out_path`. Forces French by default.

    Returns dict with status. Raises on hard failure after retries.
    """
    body = {"text": text, "model_id": model}
    if language_code:
        body["language_code"] = language_code
    body["voice_settings"] = settings or {
        "stability": 0.5, "similarity_boost": 0.75, "use_speaker_boost": True,
    }
    url = f"{API}/text-to-speech/{voice}?output_format={fmt}"
    data = json.dumps(body).encode("utf-8")
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, method="POST", headers={
            "xi-api-key": KEY, "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                audio = r.read()
            if audio[:2] == b"ID" or audio[:3] == b"ID3" or len(audio) > 1000:
                os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(audio)
                return {"ok": True, "bytes": len(audio), "path": out_path,
                        "model": model, "lang": language_code}
            last = f"suspiciously small ({len(audio)} bytes)"
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:200].decode('utf-8','replace')}"
        except Exception as e:  # noqa
            last = str(e)
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"TTS failed for {out_path!r}: {last}")


if __name__ == "__main__":
    # quick CLI: tts.py "text" out.mp3 [model] [lang]
    text, out = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "eleven_flash_v2_5"
    lang = sys.argv[4] if len(sys.argv) > 4 else "fr"
    print(tts(text, out, model=model, language_code=lang))
