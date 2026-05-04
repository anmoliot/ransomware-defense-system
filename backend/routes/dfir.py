from fastapi import APIRouter, Depends

from backend.security.auth import User, require_role
from dfir.disk_artifacts import analyze_disk_artifacts
from dfir.malware_artifact_extractor import extract_artifact_indicators
from dfir.memory_forensics import analyze_memory
from dfir.persistence_analyzer import detect_persistence
from dfir.ransom_note_analysis import analyze_ransom_note


router = APIRouter()


@router.post("/memory")
async def memory(metadata: dict, user: User = Depends(require_role("admin", "analyst"))):
    return analyze_memory(metadata)


@router.post("/disk")
async def disk(paths: list[str], user: User = Depends(require_role("admin", "analyst"))):
    return {"artifacts": analyze_disk_artifacts(paths)}


@router.post("/persistence")
async def persistence(entries: list[str], user: User = Depends(require_role("admin", "analyst"))):
    return {"matches": detect_persistence(entries)}


@router.post("/ransom-note")
async def ransom_note(text: str, user: User = Depends(require_role("admin", "analyst"))):
    return {**analyze_ransom_note(text), "indicators": extract_artifact_indicators(text)}
