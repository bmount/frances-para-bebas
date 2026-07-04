#!/usr/bin/env python3
"""Voice registry for Français pour bébas.

Every voice carries a grammatical `gender`. This is load-bearing: a voice may
only speak first-person self-descriptions that agree with its gender (enforced
by gender_guard). We diversify male/female across the curriculum.
"""

VOICES = {
    "emilie": {
        "voice_id": "i6ke7jvmGEVUyV4zjSaT",
        "name": "Émilie",
        "gender": "f",
        "accent": "parisian",
        "note": "clear young female, default female narrator",
    },
    "oris": {
        "voice_id": "BilXxxvRLrA8YTteM2sl",
        "name": "Oris",
        "gender": "m",
        "accent": "standard",
        "note": "conversational male narrator",
    },
}

# canonical default per gender
BY_GENDER = {"f": "emilie", "m": "oris"}


def voice_for_gender(gender):
    return VOICES[BY_GENDER[gender]]


def get_voice(key):
    return VOICES[key]
