from app.email.templates import patrol_created
from app.email.service import send_email


async def handle(event):
    subject, body = patrol_created(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body
    )