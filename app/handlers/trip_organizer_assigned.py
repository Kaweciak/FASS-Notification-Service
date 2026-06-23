from app.email.templates import trip_organizer_assigned
from app.email.service import send_email


async def handle(event, db):
    subject, body = trip_organizer_assigned(event.payload)

    await send_email(
        recipient=event.user_email,
        subject=subject,
        body=body,
        db=db
    )