import time
import uuid

from app.config import CACHE_TTL_SECONDS
from app.services.cache_service import CacheService
from app.services.event_service import EventService
from app.services.monitoring_service import MonitoringService
from app.services.recommendation_service import RecommendationEngine
from app.utils.logger import logger


class WorkflowService:
    def __init__(self, event_service: EventService):
        self.recommendation_engine = RecommendationEngine()
        self.cache_service = CacheService()
        self.event_service = event_service
        self.monitoring_service = MonitoringService()
        self.workflow_store = {}

    async def run_workflow(self, user_id: str, query: str, workflow_type: str):
        start_time = time.time()
        cache_key = f"{user_id}:{query}:{workflow_type}"

        cached_result = self.cache_service.get(cache_key)

        if cached_result:
            cached_result["cache_used"] = True
            latency_ms = int((time.time() - start_time) * 1000)
            cached_result["latency_ms"] = latency_ms
            self.monitoring_service.record_workflow(latency_ms, cache_used=True)
            return cached_result

        try:
            workflow_id = f"wf_{uuid.uuid4().hex[:8]}"

            self.workflow_store[workflow_id] = {
                "workflow_id": workflow_id,
                "status": "running",
                "recommendations": [],
                "latency_ms": 0,
                "cache_used": False
            }

            recommendations = self.recommendation_engine.generate_recommendations(query)

            latency_ms = int((time.time() - start_time) * 1000)

            result = {
                "workflow_id": workflow_id,
                "status": "completed",
                "recommendations": recommendations,
                "latency_ms": latency_ms,
                "cache_used": False
            }

            self.workflow_store[workflow_id] = result
            self.cache_service.set(cache_key, result.copy(), CACHE_TTL_SECONDS)

            await self.event_service.publish_event(
                event_type="workflow_completed",
                payload={
                    "workflow_id": workflow_id,
                    "user_id": user_id,
                    "workflow_type": workflow_type,
                    "latency_ms": latency_ms,
                    "recommendation_count": len(recommendations)
                }
            )

            self.monitoring_service.record_workflow(latency_ms, cache_used=False)

            return result

        except Exception as error:
            logger.error(f"Workflow failed: {error}")
            self.monitoring_service.record_failure()
            raise error

    def get_workflow(self, workflow_id: str):
        return self.workflow_store.get(workflow_id)

    def get_metrics(self):
        return self.monitoring_service.get_metrics()