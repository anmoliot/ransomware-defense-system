from agent.integrity_checker import sha256_file


def verify_file_hash(path, expected_hash):
    return sha256_file(path) == expected_hash
