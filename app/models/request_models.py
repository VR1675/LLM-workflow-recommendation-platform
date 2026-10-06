from pydantic import BaseModel


class WorkflowRequest(BaseModel):
    user_id: str
    query: str
    workflow_type: str


class RecommendationRequest(BaseModel):
    user_id: str
    query: str