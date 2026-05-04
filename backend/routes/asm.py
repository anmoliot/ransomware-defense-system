from fastapi import APIRouter, Depends

from asm.asset_discovery import discover_assets
from asm.exposure_scanner import scan_exposure
from asm.service_mapper import map_services
from backend.security.auth import User, require_role


router = APIRouter()


@router.post("/scan")
async def scan(seed_hosts: list[str], open_ports: list[int], user: User = Depends(require_role("admin", "analyst"))):
    services = map_services(open_ports)
    return {"assets": discover_assets(seed_hosts), "services": services, "exposures": scan_exposure(services)}
