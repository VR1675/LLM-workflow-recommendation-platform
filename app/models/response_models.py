from pydantic import BaseModel
from typing import List


class WorkflowResponse(BaseModel):
    workflow_id: str
    status: str
    recommendations: List[str]
    latency_ms: int
    cache_used: bool


class HealthResponse(BaseModel):
    status: str
    service: str