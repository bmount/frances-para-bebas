#!/usr/bin/env python3
"""Google Cloud Text-to-Speech backend (Chirp3-HD, highest quality).

Uses the REST API with a gcloud access token (user creds + quota project).
French is enforced by the voice's languageCode (fr-FR), so a fr-FR voice
cannot speak another language — the French safeguard holds structurally.
"""
import base64, json, os, subprocess, time, urllib.request, urllib.error

PROJECT = "bmount-public-share"
ENDPOINT = "https://texttospeech.googleapis.com/v1/text:synthesize"

# Highest-quality fr-FR voices, one per grammatical gender (mirrors Émilie/Oris).
GOOGLE_VOICES = {"f": "fr-FR-Chirp3-HD-Aoede", "m": "fr-FR-Chirp3-HD-Charon"}

_token = None


def _reset_token():
    global _token
    _token = None


def _get_token():
    global _token
    if not _token:
        _token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()
    return _token


def google_tts(text, out_path, voice_name, retries=3):
    body = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": "fr-FR", "name": voice_name},
        "audioConfig": {"audioEncoding": "MP3"},
    }).encode("utf-8")
    last = None
    for attempt in range(retries):
        req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
            "Authorization": "Bearer " + _get_token(),
            "x-goog-user-project": PROJECT,
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.load(r)
            audio = base64.b64decode(d["audioContent"])
            if len(audio) < 500:
                last = f"suspiciously small ({len(audio)} bytes)"
            else:
                os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(audio)
                return {"ok": True, "bytes": len(audio), "path": out_path,
                        "backend": "google", "voice_name": voice_name}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:200].decode('utf-8','replace')}"
            if e.code in (401, 403):
                _reset_token()   # token may have expired
        except Exception as e:  # noqa
            last = str(e)
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"google_tts failed for {out_path!r}: {last}")


if __name__ == "__main__":
    import sys
    text, out, g = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "f")
    print(google_tts(text, out, GOOGLE_VOICES[g]))
