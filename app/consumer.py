import json
import asyncio

from aiokafka import AIOKafkaConsumer

from app.config import settings
from app.schemas import KafkaEvent
from app.router import route_event


class KafkaEventConsumer:

    def __init__(self):
        self.consumer = AIOKafkaConsumer(
            settings.KAFKA_TOPIC,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            group_id=settings.KAFKA_GROUP_ID,
            auto_offset_reset="earliest",
        )

    async def start(self):

        connected = False

        while not connected:
            try:
                print("Connecting to Kafka...")

                await self.consumer.start()

                connected = True

                print(
                    f"Connected to Kafka topic: {settings.KAFKA_TOPIC}"
                )

            except Exception as exc:
                print(f"Kafka not ready yet: {exc}")

                await asyncio.sleep(5)

        try:
            async for message in self.consumer:
                print(
                    f"Received Kafka message from topic "
                    f"{message.topic}"
                )

                await self.process_message(message.value)

        finally:
            print("Stopping Kafka consumer...")

            await self.consumer.stop()

    async def process_message(self, raw_message: bytes):

        try:
            decoded = raw_message.decode()

            print(f"RAW MESSAGE: {decoded}")

            payload = json.loads(decoded)

            event = KafkaEvent(**payload)

            print(
                f"Processing event: {event.event_type}"
            )

            await route_event(event)

            print("Event processed successfully")

        except json.JSONDecodeError as exc:
            print(f"Invalid JSON message: {exc}")

        except Exception as exc:
            print(f"Failed to process message: {exc}")