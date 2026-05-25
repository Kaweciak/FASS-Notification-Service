from pydantic import BaseModel, EmailStr
from typing import Dict, Any, Optional


class KafkaEvent(BaseModel):
    event_type: str
    user_email: Optional[EmailStr] = None
    payload: Dict[str, Any]