from py.shared.logger import get_logger


class NieHander:
    def __init__(self):
        self.logger = get_logger(__name__)

    def handle_nie(self, options: list[str]):
        if options:
            pass
        else:
            self.logger.info("No NIE options found.")
