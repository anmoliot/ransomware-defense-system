import hashlib
import os
from dataclasses import dataclass
from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.security.jwt import create_access_token, decode_access_token


security = HTTPBearer(auto_error=False)


@dataclass(frozen=True)
class User:
    username: str
    role: str


DEFAULT_USERS = {
    os.getenv("ADMIN_USERNAME", "admin"): {
        "password_hash": hashlib.sha256(os.getenv("ADMIN_PASSWORD", "admin123").encode()).hexdigest(),
        "role": "admin",
    },
    os.getenv("ANALYST_USERNAME", "analyst"): {
        "password_hash": hashlib.sha256(os.getenv("ANALYST_PASSWORD", "analyst123").encode()).hexdigest(),
        "role": "analyst",
    },
}


def authenticate_user(username: str, password: str) -> Optional[User]:
    record = DEFAULT_USERS.get(username)
    if not record:
        return None
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash != record["password_hash"]:
        return None
    return User(username=username, role=record["role"])


def issue_token(user: User) -> str:
    return create_access_token(subject=user.username, role=user.role)


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> User:
    require_auth = os.getenv("REQUIRE_AUTH", "false").lower() == "true"
    if not credentials:
        if require_auth:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token")
        return User(username="anonymous", role="admin")

    try:
        payload = decode_access_token(credentials.credentials)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

    return User(username=payload["sub"], role=payload.get("role", "viewer"))


def require_role(*roles: str):
    async def dependency(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient role")
        return user

    return dependency
