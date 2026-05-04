from collections import defaultdict
from typing import DefaultDict, Dict, List


class TimeSeriesStore:
    def __init__(self):
        self.points: DefaultDict[str, List[Dict]] = defaultdict(list)

    def write(self, metric: str, point: Dict) -> None:
        self.points[metric].append(point)

    def read(self, metric: str, limit: int = 100) -> List[Dict]:
        return self.points[metric][-limit:]


timeseries_store = TimeSeriesStore()
