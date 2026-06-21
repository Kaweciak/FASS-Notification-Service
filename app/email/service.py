from sqlalchemy.ext.asyncio import AsyncSession

from app.email.smtp_provider import SMTPProvider
from app.models.email_log import EmailLog

provider = SMTPProvider()


async def send_email(
    db: AsyncSession,
    recipient: str,
    subject: str,
    body: str,
):
    await provider.send_email(
        recipient=recipient,
        subject=subject,
        body=body,
    )

    email_log = EmailLog(
        recipient=recipient,
        subject=subject,
        body=body,
    )

    db.add(email_log)
    await db.commit()