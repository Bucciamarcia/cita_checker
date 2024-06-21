import unittest
from py.post_hander.post_hander import NieHander
from py.post_hander.alert_handler import AlertHandler
from py.post_hander.email_handler import EmailHandler


class TestNieHander(unittest.TestCase):

    def test_handle_nie_with_options(self):
        # Arrange
        handler = NieHander()
        options = ["option1", "option2", "option3"]

        # Act
        try:
            handler.handle_nie(options)
        except Exception as e:
            self.fail(f"handle_nie raised an exception with options: {e}")

    def test_handle_nie_without_options(self):
        # Arrange
        handler = NieHander()
        options = []

        # Act
        try:
            handler.handle_nie(options)
        except Exception as e:
            self.fail(f"handle_nie raised an exception without options: {e}")


class TestAlertHandler(unittest.TestCase):

    def test_show_notification_linux(self):
        linux_hander = AlertHandler()
        try:
            linux_hander.show_notification("Test", "Test message")
        except Exception as e:
            self.fail(f"show_notification failed on Linux: {e}")

    def test_email_sender(self):
        hander = EmailHandler("Option1 ||| Option2 ||| Option3")
        try:
            hander.send_emails()
        except Exception as e:
            self.fail(f"send_emails failed: {e}")


if __name__ == "__main__":
    unittest.main()
