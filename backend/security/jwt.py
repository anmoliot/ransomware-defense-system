import base64
import hashlib
import hmac
import json
import os
import time
from typing import Any, Dict


JWT_SECRET = os.getenv("JWT_SECRET", "change-me-in-production")
JWT_EXP_SECONDS = int(os.getenv("JWT_EXP_SECONDS", "3600"))


def create_access_token(subject: str, role: str) -> str:
    now = int(time.time())
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "sub": subject,
        "role": role,
        "iat": now,
        "exp": now + JWT_EXP_SECONDS,
    }
    signing_input = f"{_b64_json(header)}.{_b64_json(payload)}"
    signature = _sign(signing_input)
    return f"{signing_input}.{signature}"


def decode_access_token(token: str) -> Dict[str, Any]:
    try:
        header_b64, payload_b64, signature = token.split(".")
    except ValueError as exc:
        raise ValueError("Invalid token format") from exc

    signing_input = f"{header_b64}.{payload_b64}"
    expected = _sign(signing_input)
    if not hmac.compare_digest(signature, expected):
        raise ValueError("Invalid token signature")

    payload = json.loads(_b64_decode(payload_b64))
    if int(payload.get("exp", 0)) < int(time.time()):
        raise ValueError("Token expired")
    return payload


def _b64_json(data: Dict[str, Any]) -> str:
    raw = json.dumps(data, separators=(",", ":"), sort_keys=True).encode()
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def _b64_decode(value: str) -> bytes:
    padding = "=" * (-len(value) % 4)
    return base64.urlsafe_b64decode(value + padding)


def _sign(signing_input: str) -> str:
    digest = hmac.new(JWT_SECRET.encode(), signing_input.encode(), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
