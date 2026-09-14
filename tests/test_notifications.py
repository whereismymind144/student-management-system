import unittest
from unittest import mock

from student_system.notifications import EmailAlert


class TestEmailAlert(unittest.TestCase):

    def setUp(self):
        self.alert = EmailAlert(
            email="student@example.com"
        )

    def test_update(self):
        with mock.patch("builtins.print") as mock_print:
            self.alert.update("Нова оцінка: 95")

            mock_print.assert_called_once_with(
                '[EmailAlert] Надіслано повідомлення '
                '"Нова оцінка: 95" на student@example.com'
            )


if __name__ == "__main__":
    unittest.main()