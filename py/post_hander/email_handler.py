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
        self.tls_port = self.credentials["starttls_port"]
        self.tls_wrapper_port = self.credentials["tls_wrapper_port"]
        self.user = self.credentials["smtp_username"]
        self.password = self.credentials["smtp_password"]
        self.sender = self.credentials["sender_email"]
        self.subject = self.credentials["email_subject"]
        self.body_template = self.credentials["email_body"]
        self.body = self.body_template.format(opzioni=options)

    def send_emails(self) -> None:
        msg = EmailMessage()
        msg["from"] = self.sender
        msg["to"] = ", ".join(self.emails)
        msg["subject"] = self.subject
        msg.set_content(self.body)

        try:
            with smtplib.SMTP(self.server, 465) as server:
                server.starttls()
                server.login(self.user, self.password)
                server.send_message(msg)
                self.logger.info("Email sent successfully.")
        except Exception as e:
            self.logger.error(f"Error sending email: {e}")
            raise e
