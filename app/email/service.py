from app.email.smtp_provider import SMTPProvider

provider = SMTPProvider()


async def send_email(recipient: str, subject: str, body: str):
    await provider.send_email(
        recipient=recipient,
        subject=subject,
        body=body
    )