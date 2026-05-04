import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from queue import Queue

class RansomwareEventHandler(FileSystemEventHandler):
    def __init__(self, event_queue: Queue):
        super().__init__()
        self.event_queue = event_queue

    def on_created(self, event):
        if not event.is_directory:
            self.event_queue.put(('created', event.src_path, time.time()))

    def on_modified(self, event):
        if not event.is_directory:
            self.event_queue.put(('modified', event.src_path, time.time()))

    def on_deleted(self, event):
        if not event.is_directory:
            self.event_queue.put(('deleted', event.src_path, time.time()))

    def on_moved(self, event):
        if not event.is_directory:
            self.event_queue.put(('moved', event.dest_path, time.time()))

def start_monitor(path: str, event_queue: Queue):
    event_handler = RansomwareEventHandler(event_queue)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    return observer
