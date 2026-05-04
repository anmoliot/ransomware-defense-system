import os
import time
from queue import Queue
from threading import Thread
from dotenv import load_dotenv

from .monitor import start_monitor
from .features import FeatureExtractor
from .entropy import get_file_entropy
from .canary import CanaryManager
from .anomaly import AnomalyDetector
from .sender import Sender

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
AGENT_ID = os.getenv("AGENT_ID", "agent-001")
MONITOR_DIR = os.getenv("MONITOR_DIR", "./test_monitor_dir")
FILE_RATE_THRESHOLD = float(os.getenv("FILE_RATE_THRESHOLD", "5.0"))
ENTROPY_THRESHOLD = float(os.getenv("ENTROPY_THRESHOLD", "7.5"))

def main():
    print(f"Starting Ransomware Defense Agent {AGENT_ID}")
    print(f"Monitoring Directory: {MONITOR_DIR}")
    
    event_queue = Queue()
    
    # Initialize components
    canary = CanaryManager(MONITOR_DIR)
    canary.deploy()
    
    extractor = FeatureExtractor()
    anomaly = AnomalyDetector(ENTROPY_THRESHOLD, FILE_RATE_THRESHOLD)
    sender = Sender(BACKEND_URL, AGENT_ID)
    
    # Start filesystem observer
    observer = start_monitor(MONITOR_DIR, event_queue)
    
    try:
        while True:
            # Process events
            canary_triggered = False
            last_entropy = 0.0
            
            # Consume all currently available events
            while not event_queue.empty():
                event_type, path, ts = event_queue.get()
                extractor.add_event(event_type, path, ts)
                
                if canary.is_canary(path):
                    print(f"CRITICAL: Canary file touched! {path}")
                    canary_triggered = True
                
                # Sample entropy for the latest modified file
                if event_type in ('created', 'modified'):
                    ent = get_file_entropy(path)
                    if ent > last_entropy:
                        last_entropy = ent
            
            # Calculate features
            current_rate = extractor.get_file_rate()
            ext_changes = extractor.get_extension_changes()
            score = anomaly.evaluate(last_entropy, current_rate, canary_triggered)
            
            # Send payload if suspicious or periodically
            if score > 0.0 or int(time.time()) % 10 == 0:
                sender.send_payload(
                    file_rate=current_rate,
                    entropy=last_entropy,
                    canary_triggered=canary_triggered,
                    extension_changes=ext_changes,
                    anomaly_score=score
                )
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("Stopping Agent...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
