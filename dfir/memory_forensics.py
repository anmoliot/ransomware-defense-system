from memory.injection_detector import detect_injection_indicators
from memory.shellcode_detector import detect_shellcode


def analyze_memory(metadata):
    return {
        "injection_indicators": detect_injection_indicators(metadata),
        "shellcode_indicators": detect_shellcode(metadata.get("byte_markers", [])),
    }
