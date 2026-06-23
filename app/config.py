from typing import Union

from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "fass-notification-service"

    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"
    KAFKA_CONSUME_TOPICS: str = "tourist.registered"
    KAFKA_GROUP_ID: str = "email-notification-group"

    SMTP_HOST: str = "mailhog"
    SMTP_PORT: int = 1025
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@example.com"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
