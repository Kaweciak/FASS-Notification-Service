from app.email.templates import employee_activation
from app.email.service import send_email


async def handle(event, db):
    subject, body = employee_activation(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body,
        db=db
    )