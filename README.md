# Ransomware Defense System

A distributed EDR-style ransomware defense platform. The MVP detects ransomware-like behavior with file telemetry, entropy, anomaly scores, and canary files. The next phase adds process telemetry, network signals, threat intelligence, YARA scanning, JWT auth, audit logs, MITRE ATT&CK mapping, risk scoring, and SIEM export.

## Project Structure

- `agent/`: Python-based endpoint agent to monitor file system activities.
- `detection/`: Risk scoring and behavioral detection logic.
- `threat_intel/`: IOC matching, YARA rules, and reputation helpers.
- `network/`: Endpoint network connection and DNS anomaly helpers.
- `mitre/`: MITRE ATT&CK mapping data.
- `integrations/`: SIEM export formats.
- `backend/`: FastAPI application to process telemetry, determine system state, and serve alerts.
- `docs/`: System architecture and API contracts.

## Getting Started

### Backend
1. Go to the `backend` directory.
2. Install dependencies: `pip install -r requirements.txt` (or manually install `fastapi uvicorn pydantic`).
3. From the repository root, run the server: `uvicorn backend.main:app --reload`.

### Authentication
Auth is available at `POST /auth/login`. By default local development keeps `REQUIRE_AUTH=false`, so existing demos continue working. Set `REQUIRE_AUTH=true` and configure `JWT_SECRET`, `ADMIN_USERNAME`, and `ADMIN_PASSWORD` for protected deployments.

### SIEM Export
Export alerts through:

- `GET /integrations/siem?format=json`
- `GET /integrations/siem?format=cef`
- `GET /integrations/siem?format=syslog`

### Enterprise Backend Surfaces

- `GET /correlation/incidents` and `GET /graph/attack` for XDR incident and graph correlation.
- `POST /pipeline/events` and `POST /pipeline/consume` for queued telemetry processing.
- `POST /agents/enroll` and `POST /agents/{agent_id}/heartbeat` for multi-agent management.
- `POST /response/playbooks/ransomware/{alert_id}` for dry-run SOAR containment.
- `POST /sandbox/detonate` for safe sandbox detonation planning.
- `GET /analytics/stream-summary` and `GET /compliance/report` for SOC metrics and audit reporting.

### Final-Tier SOC APIs

- `POST /incident-response/cases/{incident_id}/assign` for case ownership.
- `POST /dfir/memory`, `/dfir/disk`, `/dfir/persistence`, and `/dfir/ransom-note` for forensic analysis helpers.
- `POST /detection-engineering/validate`, `/test`, and `/coverage` for detection-as-code workflows.
- `POST /adversary/plan` for safe adversary emulation planning.
- `GET /ai-assistant/alerts/{alert_id}/explain` for analyst-facing alert explanations.
- `POST /attack-path/reconstruct` for path reconstruction and graph output.
- `POST /hunt/parse` and `/hunt/execute` for the SOC hunting DSL.
- `POST /asm/scan` and `/range/build` for attack surface and cyber range workflows.

### Agent
1. Ensure the backend is running.
2. Configure `.env` variables if necessary.
3. Run the agent: `python -m agent.monitor` (or equivalent entry point).

### Docker
Run `docker-compose up -d` to launch the backend in a container.
