from py.shared.logger import get_logger
import os
import boto3
from botocore.exceptions import ClientError
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
        os.environ["AWS_ACCESS_KEY_ID"] = self.secrets["aws_credentials"]["id"]
        os.environ["AWS_SECRET_ACCESS_KEY"] = self.secrets["aws_credentials"]["key"]
        self.region = self.secrets["aws_credentials"]["region"]

    def send_emails(self) -> None:
        client = boto3.client("ses", region_name=self.region)
        try:
            response = client.send_email(
                Destination={
                    "ToAddresses": self.emails,
                },
                Message={
                    "Body": {
                        "Text": {
                            "Charset": "UTF-8",
                            "Data": self.body,
                        },
                    },
                    "Subject": {
                        "Charset": "UTF-8",
                        "Data": self.subject,
                    },
                },
                Source=self.sender,
            )
            self.logger.info(f"Email sent! Message ID: {response['MessageId']}")
        except ClientError as e:
            self.logger.error(e.response["Error"]["Message"])
            raise e
