import asyncio

from fastapi import FastAPI

from app.consumer import KafkaEventConsumer
from app.schemas import KafkaEvent
from app.router import route_event

app = FastAPI()

consumer = KafkaEventConsumer()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consumer.start())


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/test-event")
async def test_event(event: KafkaEvent):
    await route_event(event)

    return {
        "status": "processed",
        "event_type": event.event_type
    }