POST /detect

Payload:
{
  "file_rate": 91,
  "entropy": 7.9,
  "canary_triggered": true
}

Response:
{
  "status": "ATTACK",
  "risk_score": 96
}
