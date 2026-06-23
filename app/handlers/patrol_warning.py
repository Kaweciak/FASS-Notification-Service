from app.email.templates import patrol_warning
from app.email.service import send_email


async def handle(event, db):
    subject, body = patrol_warning(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body,
        db=db
    )