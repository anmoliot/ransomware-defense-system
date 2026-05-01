import os
from collections import deque
import time

class FeatureExtractor:
    def __init__(self, window_size=60):
        # Keeps track of events in the last 'window_size' seconds
        self.events = deque()
        self.window_size = window_size
        self.suspicious_extensions = ['.enc', '.locked', '.crypto', '.crypt']
    
    def add_event(self, event_type, path, timestamp):
        self.events.append((event_type, path, timestamp))
        self._cleanup_old_events(timestamp)

    def _cleanup_old_events(self, current_time):
        while self.events and current_time - self.events[0][2] > self.window_size:
            self.events.popleft()

    def get_file_rate(self, current_time=None):
        if not current_time:
            current_time = time.time()
        self._cleanup_old_events(current_time)
        # file modifications per second in the window
        return len(self.events) / float(self.window_size)

    def get_extension_changes(self):
        count = 0
        for event in self.events:
            _, path, _ = event
            _, ext = os.path.splitext(path)
            if ext in self.suspicious_extensions:
                count += 1
        return count
