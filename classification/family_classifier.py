FAMILY_SIGNATURES = {
    "LockBit": ["lockbit", ".lockbit", "restore-my-files"],
    "BlackCat": ["blackcat", "alphv", ".alphv"],
    "WannaCry": ["wannacry", ".wncry", "wanadecryptor"],
    "Conti": ["conti", "recover-files.txt"],
}


def classify_family(text: str):
    lowered = text.lower()
    for family, markers in FAMILY_SIGNATURES.items():
        if any(marker in lowered for marker in markers):
            return {"family": family, "confidence": 0.85}
    return {"family": "Unknown", "confidence": 0.0}
