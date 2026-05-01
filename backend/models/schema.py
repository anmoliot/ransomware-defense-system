from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class SystemState(str, Enum):
    """System states for the ransomware defense mechanism."""
    NORMAL = "NORMAL"
    WARNING = "WARNING"
    ATTACK = "ATTACK"


class DetectionPayload(BaseModel):
    """
    Payload sent by the agent to the backend /detect endpoint.
    Contains behavioral features, entropy, and canary bait status.
    """
    agent_id: str = Field(..., description="Unique identifier for the reporting agent")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Time of the detection event")
    
    # Behavioral Features
    file_rate: float = Field(..., description="Rate of file modifications per second")
    extension_changes: int = Field(default=0, description="Number of suspicious file extension changes")
    suspicious_patterns: List[str] = Field(default_factory=list, description="List of suspicious patterns matched")
    
    # Entropy & Anomaly
    entropy: float = Field(..., description="Calculated entropy of recently modified files")
    anomaly_score: Optional[float] = Field(None, description="Behavioral anomaly score calculated by the agent")
    
    # Canary System
    canary_triggered: bool = Field(..., description="True if a canary/bait file was modified or deleted")


class DecisionVerdict(BaseModel):
    """
    Verdict returned or emitted by the Decision Engine.
    """
    state: SystemState = Field(..., description="The resulting system state based on the payload")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score of the verdict (0.0 to 1.0)")
    reason: str = Field(..., description="Explanation for the given verdict")


class Alert(BaseModel):
    """
    Alert schema returned by the /alerts endpoint.
    """
    id: str = Field(..., description="Unique alert identifier")
    timestamp: datetime = Field(..., description="Time the alert was generated")
    agent_id: str = Field(..., description="Agent that triggered the alert")
    verdict: DecisionVerdict = Field(..., description="The decision verdict associated with this alert")
    payload_snapshot: Optional[DetectionPayload] = Field(None, description="Snapshot of the payload that triggered the alert")
