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
        # Mapping for legacy/external services that don't embed an event_type
        self.TOPIC_FALLBACK_MAP = {
            "tourist.registered": "TouristRegistered",
            # Add any other plain-payload topics here if needed
        }

    async def start(self):
        await self._connect()
        print("Kafka connected, starting message loop")
        await self._consume()

    async def _consume(self):
        print("Starting message loop...")
        try:
            async for message in self.consumer:
                print(f"Received Kafka message from topic {message.topic}")
                # Pass the topic name down so we know where it came from
                await self.process_message(message.topic, message.value)
            print("Message loop exited cleanly.")
        except Exception as exc:
            print(f"Message loop crashed: {exc}")
            raise
        finally:
            print("Stopping Kafka consumer...")
            await self.consumer.stop()

    async def _connect(self):
        topics = [t.strip() for t in settings.KAFKA_CONSUME_TOPICS.split(",")]

        while True:
            try:
                print(f"Connecting to Kafka topics: {topics}...")

                self.consumer = AIOKafkaConsumer(
                    *topics,
                    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
                    group_id=settings.KAFKA_GROUP_ID,
                    auto_offset_reset="earliest",
                )

                await self.consumer.start()

                print(f"Connected to Kafka topics: {topics}")
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

    async def process_message(self, topic: str, raw_message: bytes):
        try:
            decoded = raw_message.decode()
            print(f"RAW MESSAGE FROM {topic}: {decoded}")

            data = json.loads(decoded)

            # Strategy 1: Look for an embedded 'event_type' (e.g., Trip Service structure)
            if isinstance(data, dict) and "event_type" in data:
                event_type = data["event_type"]
                payload = data.get("payload", data)

            # Strategy 2: Fallback to the topic-to-event map (e.g., Tourist Service structure)
            else:
                event_type = self.TOPIC_FALLBACK_MAP.get(topic, "UnknownEvent")
                payload = data

            event = KafkaEvent(
                event_type=event_type,
                payload=payload
            )

            print(f"Processing event: {event.event_type}")
            await route_event(event)
            print("Event processed successfully")

        except json.JSONDecodeError as exc:
            print(f"Invalid JSON message: {exc}")

        except Exception as exc:
            print(f"Failed to process message: {exc}")