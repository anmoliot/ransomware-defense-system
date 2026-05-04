from fastapi import APIRouter, HTTPException, status

from backend.models.schema import TokenRequest, TokenResponse
from backend.security.auth import authenticate_user, issue_token


router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(request: TokenRequest):
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return TokenResponse(access_token=issue_token(user), role=user.role)
