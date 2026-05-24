from abc import ABC, abstractmethod


class EmailProvider(ABC):

    @abstractmethod
    async def send_email(
        self,
        recipient: str,
        subject: str,
        body: str
    ) -> None:
        pass