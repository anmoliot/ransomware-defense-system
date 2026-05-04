# Operational Workflow

1. **Initialization**:
   - The Agent starts, reads configuration (e.g., `.env`), and sets up a `watchdog` observer on the configured `MONITOR_DIR`.
   - The Canary manager creates bait files (e.g., `passwords.txt`) in the monitored directories.
   
2. **Monitoring**:
   - The `monitor.py` script captures `FileCreatedEvent`, `FileModifiedEvent`, `FileDeletedEvent`.
   - These events are pushed to an event queue.

3. **Feature Extraction & Analysis**:
   - Every `X` seconds, `features.py` calculates the file modification rate and identifies extension changes (e.g., renaming to `.enc`).
   - `entropy.py` samples recently modified files to calculate Shannon entropy. High entropy indicates encrypted content.

4. **Anomaly Detection**:
   - `anomaly.py` applies threshold logic:
     - `IF entropy > ENTROPY_THRESHOLD AND file_rate > FILE_RATE_THRESHOLD -> TRIGGER ALERT`
     - `IF canary_file modified -> TRIGGER CRITICAL ALERT`

5. **Reporting**:
   - `sender.py` creates a `DetectionPayload` and POSTs it to `http://backend-url/detect`.

6. **Backend Decision**:
   - `decision_engine.py` receives the payload. It generates a `DecisionVerdict`.
   - `state_manager.py` updates the system state and appends the alert to history.
   - `websocket_manager.py` broadcasts the alert to all connected clients.
