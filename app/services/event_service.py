import asyncio
from datetime import datetime

from app.utils.logger import logger


class EventService:
    def __init__(self):
        self.event_queue = asyncio.Queue()
        self.total_events_published = 0
        self.total_events_processed = 0

    async def publish_event(self, event_type: str, payload: dict):
        event = {
            "event_type": event_type,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }

        await self.event_queue.put(event)
        self.total_events_published += 1

        logger.info(f"Kafka-style event published: {event}")
        return event

    async def process_events(self):
        while True:
            event = await self.event_queue.get()

            logger.info(f"Processing workflow event: {event}")
            await asyncio.sleep(0.05)

            self.total_events_processed += 1
            self.event_queue.task_done()

    def get_event_metrics(self):
        return {
            "events_published": self.total_events_published,
            "events_processed": self.total_events_processed,
            "queue_size": self.event_queue.qsize(),
            "event_streaming_enabled": True
        }