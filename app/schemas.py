from pydantic import BaseModel, EmailStr
from typing import Dict, Any


class KafkaEvent(BaseModel):
    event_type: str
    user_email: EmailStr
    payload: Dict[str, Any]