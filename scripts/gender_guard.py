#!/usr/bin/env python3
"""RIGID grammatical-gender safeguard.

Hard rule: a voice may NEVER speak a first-person self-description whose
grammatical gender disagrees with the voice's gender. A male voice must never
say "je suis fatiguée / américaine / allée"; a female voice must never say
"je suis fatigué / américain / allé".

Defense in depth (three layers), mirroring the English-prevention safeguard:

  L1 (structure) — authored data provides gendered variants fr_m / fr_f; the
     build assigns fr_m to a male voice and fr_f to a female voice. Handled by
     the build script, not here.
  L2 (lexicon)   — assert_gender_ok() checks the actual text against a curated
     table of gendered self-descriptive forms. Hard error on mismatch.
  L3 (morphology)— a conservative suffix net catches unlisted feminine forms in
     first-person context so an authoring slip can't slip through silently.

Only FIRST-PERSON self-reference is constrained. "Elle est américaine" or
"Tu es contente" spoken by a male voice are perfectly correct and must pass.
"""
import json, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "gendered_forms.json")


class GenderAgreementError(Exception):
    pass


# --- L2: curated gendered self-descriptive forms (ground truth) -------------
# form -> "m" | "f". Extend via data/gendered_forms.json (merged in at import).
GENDERED_FORMS = {
    # states / feelings
    "content": "m", "contente": "f",
    "fatigué": "m", "fatiguée": "f",
    "prêt": "m", "prête": "f",
    "heureux": "m", "heureuse": "f",
    "désolé": "m", "désolée": "f",
    "occupé": "m", "occupée": "f",
    "perdu": "m", "perdue": "f",
    "sûr": "m", "sûre": "f",
    "malade": None,  # epicene: explicitly safe
    # nationalities / origin
    "américain": "m", "américaine": "f",
    "mexicain": "m", "mexicaine": "f",
    "français": "m", "française": "f",
    "espagnol": "m", "espagnole": "f",
    "italien": "m", "italienne": "f",
    # traits
    "grand": "m", "grande": "f",
    "petit": "m", "petite": "f",
    "fort": "m", "forte": "f",
    "intelligent": "m", "intelligente": "f",
    "patient": "m", "patiente": "f",
    "sérieux": "m", "sérieuse": "f",
    "curieux": "m", "curieuse": "f",
    "nerveux": "m", "nerveuse": "f",
    "gentil": "m", "gentille": "f",
    # participles (passé composé with être / states)
    "allé": "m", "allée": "f",
    "venu": "m", "venue": "f",
    "arrivé": "m", "arrivée": "f",
    "resté": "m", "restée": "f",
    "né": "m", "née": "f",
    "assis": "m", "assise": "f",
}

# epicene adjectives we may use to describe oneself — explicitly SAFE, never flag
EPICENE = {
    "rouge", "jaune", "facile", "difficile", "possible", "impossible",
    "jeune", "sympathique", "célèbre", "riche", "pauvre", "calme", "timide",
    "honnête", "propre", "tranquille", "agréable", "formidable", "magnifique",
    "pratique", "nécessaire", "responsable", "aimable", "capable", "sociable",
    "optimiste", "réaliste", "moderne",
}

# --- first-person self-reference detection ---------------------------------
# Constrain agreement ONLY when the adjective is a predicate of "je".
FIRST_PERSON = re.compile(
    r"(je\s+suis|je\s+me\s+sens|je\s+me\s+sentais|j['’]?étais|je\s+serai|je\s+serais|"
    r"j['’]?ai\s+été|je\s+suis\s+allée?|je\s+deviens|je\s+reste|je\s+resterais|"
    r"moi[,\s]+je\s+suis)",
    re.IGNORECASE,
)

# --- L3: conservative feminine-suffix net (unambiguous endings only) --------
FEMININE_SUFFIXES = ("ée", "euse", "trice", "aine", "ienne", "onne", "elle")

# common non-adjective words ending in those suffixes (so the net won't misfire
# in a rare first-person sentence that happens to contain one).
MORPH_SAFE = {
    "elle", "personne", "semaine", "capitaine", "fontaine", "douzaine",
    "centaine", "chose", "année", "journée", "matinée", "idée", "musée",
    "poupée", "colonne", "couronne", "téléphone", "zone", "aucune",
}


def _norm(s):
    return unicodedata.normalize("NFC", s).lower()


def _tokens(text):
    return re.findall(r"[a-zà-öø-ÿ'’]+", _norm(text))


def _load_extra():
    if os.path.exists(DATA):
        try:
            with open(DATA, encoding="utf-8") as f:
                for k, v in json.load(f).get("forms", {}).items():
                    GENDERED_FORMS[_norm(k)] = v
        except Exception:  # noqa - never let a bad data file crash a check
            pass


_load_extra()


def assert_gender_ok(text, voice_gender):
    """Raise GenderAgreementError if `text` self-describes in a gender that
    conflicts with `voice_gender` ("m" or "f"). Passes silently when safe.
    """
    if voice_gender not in ("m", "f"):
        raise ValueError(f"voice_gender must be 'm' or 'f', got {voice_gender!r}")

    if not FIRST_PERSON.search(text):
        return  # no first-person self-description -> any voice is fine

    toks = _tokens(text)
    tokset = set(toks)

    # L2: curated lexicon (ground truth, both directions)
    for tok in toks:
        g = GENDERED_FORMS.get(tok)
        if g in ("m", "f") and g != voice_gender:
            raise GenderAgreementError(
                f"[gender] voice={voice_gender} but self-description uses "
                f"{g!r}-form {tok!r} in: {text!r}"
            )

    # L3: morphology net — unlisted feminine forms spoken by a male voice.
    if voice_gender == "m":
        for tok in toks:
            if not tok.endswith(FEMININE_SUFFIXES):
                continue
            if tok in EPICENE or tok in MORPH_SAFE or GENDERED_FORMS.get(tok) == "m":
                continue
            raise GenderAgreementError(
                f"[gender-morph] male voice, likely feminine self-form "
                f"{tok!r} (unlisted) in: {text!r}. Add it to GENDERED_FORMS "
                f"or fix the sentence."
            )
    return True


if __name__ == "__main__":
    # self-test
    ok = [
        ("Je suis américain.", "m"),
        ("Je suis américaine.", "f"),
        ("Je suis fatigué.", "m"),
        ("Elle est américaine.", "m"),      # 3rd person -> fine for male voice
        ("Tu es contente ?", "m"),          # 2nd person -> fine
        ("Je suis malade.", "m"),           # epicene -> fine
        ("Je suis sympathique.", "m"),      # epicene -> fine
        ("C'est important.", "m"),
    ]
    bad = [
        ("Je suis américaine.", "m"),
        ("Je suis fatiguée.", "m"),
        ("Je suis allée à Nice.", "m"),
        ("Je suis américain.", "f"),
        ("Je suis heureuse.", "m"),
        ("Je suis vénézuélienne.", "m"),    # unlisted -> caught by morphology
    ]
    fails = 0
    for t, g in ok:
        try:
            assert_gender_ok(t, g); print(f"PASS ok  [{g}] {t}")
        except GenderAgreementError as e:
            fails += 1; print(f"XXXX should-pass FAILED [{g}] {t} :: {e}")
    for t, g in bad:
        try:
            assert_gender_ok(t, g); fails += 1
            print(f"XXXX should-block PASSED [{g}] {t}")
        except GenderAgreementError:
            print(f"PASS block[{g}] {t}")
    print("ALL GOOD" if not fails else f"{fails} FAILURES")
