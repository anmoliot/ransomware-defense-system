from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
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

    # Endpoint Process Telemetry
    processes: List["ProcessEvent"] = Field(
        default_factory=list,
        description="Observed process activity from the endpoint agent"
    )

    # Network Telemetry
    network_connections: List["NetworkConnection"] = Field(
        default_factory=list,
        description="Observed endpoint network connections"
    )

    # Threat Intelligence
    file_hashes: List[str] = Field(default_factory=list, description="File hashes observed by the agent")
    domains: List[str] = Field(default_factory=list, description="Domains observed by the agent")
    ips: List[str] = Field(default_factory=list, description="IP addresses observed by the agent")
    urls: List[str] = Field(default_factory=list, description="URLs observed by the agent")
    yara_matches: List[str] = Field(default_factory=list, description="YARA rule names matched by the agent")
    ioc_matches: List[str] = Field(default_factory=list, description="IOC values matched by the agent")


class DecisionVerdict(BaseModel):
    """
    Verdict returned or emitted by the Decision Engine.
    """
    state: SystemState = Field(..., description="The resulting system state based on the payload")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score of the verdict (0.0 to 1.0)")
    reason: str = Field(..., description="Explanation for the given verdict")
    risk_score: int = Field(default=0, ge=0, le=100, description="Enterprise-style risk score")
    mitre_techniques: List["MitreTechnique"] = Field(
        default_factory=list,
        description="MITRE ATT&CK techniques associated with the verdict"
    )
    signals: List[str] = Field(default_factory=list, description="Normalized detection signals behind the verdict")


class Alert(BaseModel):
    """
    Alert schema returned by the /alerts endpoint.
    """
    id: str = Field(..., description="Unique alert identifier")
    timestamp: datetime = Field(..., description="Time the alert was generated")
    agent_id: str = Field(..., description="Agent that triggered the alert")
    verdict: DecisionVerdict = Field(..., description="The decision verdict associated with this alert")
    payload_snapshot: Optional[DetectionPayload] = Field(None, description="Snapshot of the payload that triggered the alert")


class ProcessEvent(BaseModel):
    """Endpoint process telemetry collected by the agent."""
    pid: Optional[int] = Field(None, description="Process ID")
    ppid: Optional[int] = Field(None, description="Parent process ID")
    name: str = Field(..., description="Process executable name")
    command_line: str = Field(default="", description="Full command line when available")
    parent_name: Optional[str] = Field(None, description="Parent process executable name")
    username: Optional[str] = Field(None, description="Owning user")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class NetworkConnection(BaseModel):
    """Endpoint network connection telemetry."""
    process_name: Optional[str] = Field(None, description="Owning process name")
    local_address: Optional[str] = None
    local_port: Optional[int] = None
    remote_address: Optional[str] = None
    remote_port: Optional[int] = None
    protocol: str = Field(default="tcp")
    state: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class MitreTechnique(BaseModel):
    """MITRE ATT&CK mapping for a detection signal."""
    tactic: str
    technique_id: str
    technique: str


class TokenRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str


class AuditEvent(BaseModel):
    id: str
    timestamp: datetime
    actor: str
    action: str
    target: str
    outcome: str
    details: Dict[str, Any] = Field(default_factory=dict)


class GraphNode(BaseModel):
    id: str
    label: str
    type: str
    risk: int = 0


class GraphEdge(BaseModel):
    source: str
    target: str
    label: str


class ThreatGraph(BaseModel):
    nodes: List[GraphNode] = Field(default_factory=list)
    edges: List[GraphEdge] = Field(default_factory=list)


class TimelineEvent(BaseModel):
    id: str
    timestamp: datetime
    event_type: str
    title: str
    description: str
    severity: str = "info"
    mitre_technique: Optional[str] = None


class Incident(BaseModel):
    id: str
    title: str
    state: str = "open"
    severity: str
    risk_score: int
    alert_ids: List[str] = Field(default_factory=list)
    techniques: List[MitreTechnique] = Field(default_factory=list)
    timeline: List[TimelineEvent] = Field(default_factory=list)
    graph: ThreatGraph = Field(default_factory=ThreatGraph)


class HuntQuery(BaseModel):
    query: str
    limit: int = Field(default=50, ge=1, le=1000)


class ResponseActionResult(BaseModel):
    action: str
    target: str
    status: str
    detail: str


class ResponseExecution(BaseModel):
    playbook: str
    alert_id: str
    dry_run: bool = True
    results: List[ResponseActionResult] = Field(default_factory=list)


DetectionPayload.update_forward_refs()
DecisionVerdict.update_forward_refs()
