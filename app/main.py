import asyncio

from fastapi import FastAPI, HTTPException

from app.config import APP_NAME, APP_VERSION
from app.models.request_models import RecommendationRequest, WorkflowRequest
from app.models.response_models import HealthResponse, WorkflowResponse
from app.services.event_service import EventService
from app.services.recommendation_service import RecommendationEngine
from app.services.workflow_service import WorkflowService
from app.utils.logger import logger


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=(
        "Production-style LLM workflow and recommendation backend with "
        "async orchestration, Redis-ready caching, event streaming, "
        "PyTorch ranking, workflow status tracking, and monitoring."
    )
)

event_service = EventService()
workflow_service = WorkflowService(event_service=event_service)
recommendation_engine = RecommendationEngine()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(event_service.process_events())
    logger.info("Background event processor started")


@app.get("/")
async def home():
    return {
        "message": "LLM Workflow Recommendation Platform Running",
        "docs": "/docs"
    }


@app.get("/health", response_model=HealthResponse)
async def health():
    return {
        "status": "healthy",
        "service": "llm-workflow-platform"
    }


@app.post("/workflow/run", response_model=WorkflowResponse)
async def run_workflow(request: WorkflowRequest):
    logger.info(f"Running workflow for user_id={request.user_id}")

    return await workflow_service.run_workflow(
        user_id=request.user_id,
        query=request.query,
        workflow_type=request.workflow_type
    )


@app.get("/workflow/{workflow_id}")
async def get_workflow(workflow_id: str):
    workflow = workflow_service.get_workflow(workflow_id)

    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")

    return workflow


@app.post("/recommend")
async def recommend(request: RecommendationRequest):
    recommendations = recommendation_engine.generate_recommendations(request.query)

    return {
        "user_id": request.user_id,
        "recommendations": recommendations
    }


@app.get("/metrics")
async def metrics():
    return {
        "workflow_metrics": workflow_service.get_metrics(),
        "event_metrics": event_service.get_event_metrics()
    }