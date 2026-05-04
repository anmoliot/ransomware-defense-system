from dataclasses import dataclass
from typing import Iterable, List, Set

from backend.models.schema import DetectionPayload


@dataclass(frozen=True)
class IOCMatch:
    indicator_type: str
    value: str
    source: str = "local"


class IOCMatcher:
    """Local IOC matcher with room for external feed hydration."""

    def __init__(self):
        self.hashes: Set[str] = set()
        self.domains: Set[str] = {
            "malicious.example",
            "ransomware-c2.example",
        }
        self.ips: Set[str] = {
            "10.255.255.66",
            "203.0.113.99",
        }
        self.urls: Set[str] = set()

    def load_indicators(
        self,
        hashes: Iterable[str] = (),
        domains: Iterable[str] = (),
        ips: Iterable[str] = (),
        urls: Iterable[str] = (),
    ) -> None:
        self.hashes.update(item.lower() for item in hashes)
        self.domains.update(item.lower() for item in domains)
        self.ips.update(ips)
        self.urls.update(item.lower() for item in urls)

    def match_payload(self, payload: DetectionPayload) -> List[IOCMatch]:
        matches: List[IOCMatch] = []
        matches.extend(self._match("hash", payload.file_hashes, self.hashes))
        matches.extend(self._match("domain", payload.domains, self.domains))
        matches.extend(self._match("ip", payload.ips, self.ips))
        matches.extend(self._match("url", payload.urls, self.urls))

        for connection in payload.network_connections:
            if connection.remote_address in self.ips:
                matches.append(IOCMatch("ip", connection.remote_address or ""))

        return matches

    def _match(self, indicator_type: str, values: Iterable[str], known: Set[str]) -> List[IOCMatch]:
        results = []
        for value in values:
            normalized = value.lower()
            if normalized in known:
                results.append(IOCMatch(indicator_type, value))
        return results


ioc_matcher = IOCMatcher()
