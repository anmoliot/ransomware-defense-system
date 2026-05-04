# API Contracts

## REST API

### 1. `POST /detect`
**Description**: Receives telemetry data from agents.
**Request Body**: `DetectionPayload` (see `backend/models/schema.py`)

Example payload:
```json
{
  "file_rate": 91,
  "entropy": 7.9,
  "canary_triggered": true
}
```

**Response**: `200 OK`
```json
{
  "status": "success",
  "verdict": {
    "state": "WARNING",
    "confidence": 0.8,
    "reason": "High file modification rate detected."
  }
}
```

### 2. `GET /alerts`
**Description**: Retrieves a history of generated alerts.
**Response**: `200 OK`
```json
[
  {
    "id": "uuid",
    "timestamp": "2023-10-01T12:00:00Z",
    "agent_id": "agent-001",
    "verdict": {
      "state": "ATTACK",
      "confidence": 1.0,
      "reason": "Canary file triggered."
    },
    "payload_snapshot": { ... }
  }
]
```

## WebSocket API

### 1. `WS /ws`
**Description**: Real-time push notifications of alerts.
**Message Format**:
```json
{
  "type": "alert",
  "data": { ... Alert object ... }
}
```
