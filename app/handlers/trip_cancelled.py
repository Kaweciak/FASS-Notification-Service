from app.email.templates import trip_cancelled
from app.email.service import send_email


async def handle(event):
    subject, body = trip_cancelled(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body
    )