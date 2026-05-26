import json
import asyncio

from aiokafka import AIOKafkaConsumer
from aiokafka.errors import GroupCoordinatorNotAvailableError, KafkaConnectionError

from app.config import settings
from app.schemas import KafkaEvent
from app.router import route_event


class KafkaEventConsumer:

    def __init__(self):
        self.consumer = None

    async def start(self):
        await self._connect()

        try:
            async for message in self.consumer:
                print(f"Received Kafka message from topic {message.topic}")
                await self.process_message(message.value)
        finally:
            print("Stopping Kafka consumer...")
            await self.consumer.stop()

    async def _connect(self):
        while True:
            try:
                print("Connecting to Kafka...")

                self.consumer = AIOKafkaConsumer(
                    settings.KAFKA_TOPIC,
                    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                    group_id=settings.KAFKA_GROUP_ID,
                    auto_offset_reset="earliest",
                )

                await self.consumer.start()

                print(f"Connected to Kafka topic: {settings.KAFKA_TOPIC}")
                return

            except (GroupCoordinatorNotAvailableError, KafkaConnectionError) as exc:
                print(f"Kafka not ready yet ({type(exc).__name__}), retrying in 5s...")
                await self._safe_stop()
                await asyncio.sleep(5)

            except Exception as exc:
                print(f"Unexpected error connecting to Kafka: {exc}, retrying in 5s...")
                await self._safe_stop()
                await asyncio.sleep(5)

    async def _safe_stop(self):
        if self.consumer is not None:
            try:
                await self.consumer.stop()
            except Exception:
                pass
            self.consumer = None

    async def process_message(self, raw_message: bytes):
        try:
            decoded = raw_message.decode()
            print(f"RAW MESSAGE: {decoded}")

            payload = json.loads(decoded)
            event = KafkaEvent(**payload)

            print(f"Processing event: {event.event_type}")
            await route_event(event)
            print("Event processed successfully")

        except json.JSONDecodeError as exc:
            print(f"Invalid JSON message: {exc}")

        except Exception as exc:
            print(f"Failed to process message: {exc}")