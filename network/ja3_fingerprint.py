def ja3_summary(version: str, ciphers, extensions):
    return f"{version},{'-'.join(map(str, ciphers))},{'-'.join(map(str, extensions))}"
