from .interfaces import Observer


class EmailAlert(Observer):
    """Спостерігач, який імітує надсилання email."""

    def __init__(self, email: str):
        self.email = email

    def update(self, message: str) -> None:
        print(
            f'[EmailAlert] Надіслано повідомлення '
            f'"{message}" на {self.email}'
        )
