import math
import os

def calculate_shannon_entropy(data: bytes) -> float:
    """Calculate the Shannon entropy of a byte array."""
    if not data:
        return 0.0

    entropy = 0.0
    length = len(data)
    
    # Count frequency of each byte
    counts = [0] * 256
    for byte in data:
        counts[byte] += 1
        
    for count in counts:
        if count == 0:
            continue
        p = count / length
        entropy -= p * math.log2(p)
        
    return entropy

def get_file_entropy(filepath: str, sample_size=1024*10) -> float:
    """Read a sample of the file and calculate entropy."""
    try:
        with open(filepath, 'rb') as f:
            data = f.read(sample_size)
        return calculate_shannon_entropy(data)
    except Exception:
        # Cannot read file (locked or deleted)
        return 0.0
