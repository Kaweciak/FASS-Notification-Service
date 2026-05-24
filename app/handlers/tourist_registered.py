from app.email.templates import tourist_registered
from app.email.service import send_email


async def handle(event):
    subject, body = tourist_registered(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body
    )