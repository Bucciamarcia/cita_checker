from py.shared.logger import get_logger
import smtplib
from email.message import EmailMessage
from py.shared.data_reader import DataReader


class EmailHandler:
    def __init__(self, options: str):
        self.logger = get_logger(__name__)
        self.options = options
        self.secrets = DataReader("data_secret.json").read_json()
        self.emails: list[str] = self.secrets["emails"]
        self.credentials = self.secrets["ses_credentials"]
        self.server = self.credentials["smtp_endpoint"]
        self.tls_port = self.credentials["tls_wrapper_port"]
        self.user = self.credentials["smtp_user"]
        self.password = self.credentials["smtp_password"]
        self.sender = self.credentials["sender_email"]
        self.subject = self.credentials["email_subject"]
        self.body_template = self.credentials["email_body"]
        self.body = self.body_template.format(opzioni=options)
    
    def send_emails(self) -> None:
