from app.email.templates import assignment_created
from app.email.service import send_email


async def handle(event,db):
    subject, body = assignment_created(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body,
        db=db
    )