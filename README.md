# Ransomware Defense System

A distributed agent-backend architecture to detect ransomware-like behavior (high file modification rates, abnormal extensions, high entropy) and provide real-time alerts.

## Project Structure

- `agent/`: Python-based endpoint agent to monitor file system activities.
- `backend/`: FastAPI application to process telemetry, determine system state, and serve alerts.
- `docs/`: System architecture and API contracts.

## Getting Started

### Backend
1. Go to the `backend` directory.
2. Install dependencies: `pip install -r requirements.txt` (or manually install `fastapi uvicorn pydantic`).
3. Run the server: `uvicorn main:app --reload`.

### Agent
1. Ensure the backend is running.
2. Configure `.env` variables if necessary.
3. Run the agent: `python -m agent.monitor` (or equivalent entry point).

### Docker
Run `docker-compose up -d` to launch the backend in a container.
