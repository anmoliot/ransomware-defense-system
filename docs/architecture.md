# System Architecture

## Overview
The Ransomware Defense System consists of two primary components:
1. **Agent**: A lightweight background process that monitors specific directories for suspicious file activity indicative of ransomware (e.g., mass encryption, high entropy changes, canary file triggers).
2. **Backend**: A central server that receives telemetry from the agents, decides the system state, and broadcasts alerts to administrators.

## Component Diagram
```mermaid
graph TD
    A[Agent: Monitor File System] -->|Extract Features| B[Agent: Feature Extractor]
    A -->|Monitor Canary| C[Agent: Canary Manager]
    A -->|Calculate Entropy| D[Agent: Entropy Calculator]
    
    B --> E[Agent: Anomaly Detector]
    C --> E
    D --> E
    
    E -->|Send Telemetry| F[Backend: POST /detect]
    
    F --> G[Backend: Decision Engine]
    G --> H[Backend: State Manager]
    G --> I[Backend: WebSocket Manager]
    
    I -->|Real-time Alerts| J[Frontend Clients]
    H -->|Historical Alerts| K[GET /alerts]
```
