def analyze_ransom_note(text: str):
    lowered = text.lower()
    return {
        "has_tor": ".onion" in lowered or "tor" in lowered,
        "has_crypto": "bitcoin" in lowered or "monero" in lowered,
        "extortion_language": "publish" in lowered or "leak" in lowered,
    }
