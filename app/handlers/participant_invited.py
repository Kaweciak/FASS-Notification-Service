from app.email.templates import participant_invited
from app.email.service import send_email


async def handle(event, db):
    subject, body = participant_invited(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body,
        db=db
    )