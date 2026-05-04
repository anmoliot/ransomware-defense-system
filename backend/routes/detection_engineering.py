from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from detection_engineering.detection_coverage import mitre_coverage
from detection_engineering.rule_tester import test_rule
from detection_engineering.rule_validator import validate_rule


router = APIRouter()


@router.post("/validate")
async def validate(rule: dict, user: User = Depends(require_role("admin", "analyst"))):
    return validate_rule(rule)


@router.post("/test")
async def test(rule: dict, fixture: dict, user: User = Depends(require_role("admin", "analyst"))):
    return test_rule(rule, fixture)


@router.post("/coverage")
async def coverage(rules: list[dict], user: User = Depends(require_role("admin", "analyst", "viewer"))):
    return mitre_coverage(rules)
