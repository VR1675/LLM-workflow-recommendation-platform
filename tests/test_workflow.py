import asyncio

from app.services.event_service import EventService
from app.services.workflow_service import WorkflowService


def test_run_workflow():
    async def run_test():
        event_service = EventService()
        workflow_service = WorkflowService(event_service)

        result = await workflow_service.run_workflow(
            user_id="test_user",
            query="test workflow automation",
            workflow_type="automation"
        )

        assert result["status"] == "completed"
        assert len(result["recommendations"]) == 3

    asyncio.run(run_test())