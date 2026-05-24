from app.email.templates import assignment_rejected
from app.email.service import send_email


async def handle(event):
    subject, body = assignment_rejected(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body
    )