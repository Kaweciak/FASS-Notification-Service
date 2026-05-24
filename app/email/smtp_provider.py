import aiosmtplib
from email.message import EmailMessage

from app.email.base import EmailProvider
from app.config import settings


class SMTPProvider(EmailProvider):

    async def send_email(
        self,
        recipient: str,
        subject: str,
        body: str
    ) -> None:

        message = EmailMessage()
        message["From"] = settings.SMTP_FROM_EMAIL
        message["To"] = recipient
        message["Subject"] = subject

        message.set_content(body)

        await aiosmtplib.send(
            message,
            hostname=settings.SMTP_HOST,
            port=settings.SMTP_PORT,
            username=settings.SMTP_USERNAME,
            password=settings.SMTP_PASSWORD,
        )