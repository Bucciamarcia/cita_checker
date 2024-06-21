from py.shared.logger import get_logger
from py.post_hander.email_handler import EmailHandler
from py.post_hander.alert_handler import AlertHandler
from py.shared.data_reader import DataReader


class NieHander:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.secrets = DataReader("data_secret.json").read_json()

    def handle_nie(self, options: list[str]) -> None:
        if options:
            alert_hander = AlertHandler()
            alert_hander.show_notification("Opzioni NIE trovate!", f"Opzioni disponibili: {" ||| ".join(options)}")
            email_hander = EmailHandler(" ||| ".join(options))
        else:
            self.logger.info("No NIE options found.")
