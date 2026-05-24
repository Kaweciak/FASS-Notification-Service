from app.email.templates import trip_warning
from app.email.service import send_email


async def handle(event):
    subject, body = trip_warning(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body
    )