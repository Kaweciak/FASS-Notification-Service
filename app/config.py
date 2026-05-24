from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "fass-notification-service"

    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"
    KAFKA_TOPIC: str = "user-events"
    KAFKA_GROUP_ID: str = "email-notification-group"

    SMTP_HOST: str = "mailhog"
    SMTP_PORT: int = 1025
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@example.com"

    class Config:
        env_file = ".env"


settings = Settings()