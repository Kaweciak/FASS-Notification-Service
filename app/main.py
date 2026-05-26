import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.consumer import KafkaEventConsumer
from app.schemas import KafkaEvent
from app.router import route_event

consumer = KafkaEventConsumer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Lifespan startup fired")
    await consumer._connect()
    print("Kafka connected, starting message loop")
    task = asyncio.create_task(consumer._consume())
    task.add_done_callback(
        lambda t: print(f"Consumer task ended: {t.exception()}")
        if not t.cancelled() and t.exception() else None
    )
    yield
    print("Lifespan shutdown")
    await consumer._safe_stop()

app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/test-event")
async def test_event(event: KafkaEvent):
    await route_event(event)
    return {"status": "processed", "event_type": event.event_type}