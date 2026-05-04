import hashlib
import hmac
import json


def sign_payload(payload: dict, secret: str) -> str:
    body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


def verify_signature(payload: dict, secret: str, signature: str) -> bool:
    return hmac.compare_digest(sign_payload(payload, secret), signature)
