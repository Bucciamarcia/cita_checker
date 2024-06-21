from py.shared.logger import get_logger


class EmailHandler:
    def __init__(self, emails: list[str]):
        self.logger = get_logger(__name__)
        self.emails = emails
