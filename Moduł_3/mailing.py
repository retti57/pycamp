import os
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv
from dotenv import load_dotenv


class EmailSenderManager:
    """Email sender class. Has methods send() to send email message, and message() to create such one.
    This method does not support any attachments to message"""

    def __init__(self):
        self.port = None
        self.sender = None
        self.receiver = None
        self.host = None
        self.context = ssl.create_default_context()
        cwd = os.getcwd()

        if os.path.exists(cwd+r'\.env'):
            load_dotenv()
            sender_env = str(getenv('NOTIFICATIONS_EMAIL_ADDRESS'))
            self._setup(sender=sender_env)
        else:
            self._setup(sender='notificationsmail87@gmail.com')

    def _setup(self, sender: str, receiver: str = 'docz9856@wp.pl'):
        """
        Settings for email, defining addresses for sender and receiver.
        For convenient use, you should set new environmental variable, for example:
            >NOTIFICATIONS_EMAIL_ADDRESS=''<
            >NOTIFICATIONS_EMAIL_PASSWORD=<
        :param sender: default address:  notificationsmail87@gmail.com set as environmental variable
        :param receiver: default address:  docz9856@wp.pl

        :return: None
        """
        self.port = 465
        self.sender = sender.strip()
        self.receiver = receiver.strip()
        try:
            if '@' in receiver and len(receiver) >= 5:
                address, domain = sender.split('@')
                self.host = "smtp.{}".format(domain)
            else:
                print('Invalid e-mail domain')
                assert ValueError
        except ValueError as err:
            print(f'>{err}<\nPlease enter valid email address')

        return None

    def send(self, msg):
        """
        This function sends given message. It uses a password set from gmail account and that passoword
        is set as environmental variable >NOTIFICATIONS_EMAIL_PASSWORD=<
        :return: None
        """
        with smtplib.SMTP_SSL(host=self.host, port=self.port, context=self.context) as server:
            password = str(getenv('NOTIFICATIONS_EMAIL_PASSWORD'))
            server.login(user=self.sender, password=password)
            # Send email here
            server.sendmail(from_addr=self.sender, to_addrs=self.receiver, msg=msg.as_string())

        return None

    def message(self):
        """Create a message to send
        :return: message object of MIMEMultipart type"""
        message = MIMEMultipart("alternative")
        message["Subject"] = "Nowa wiadomość o książkę"
        message["From"] = self.sender
        message["To"] = self.receiver

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        When will you return my book?"""
        html = """\
        <html>
            <body>
                <p>Siemka,<br>
                    Co u Ciebie?<br>
                    Kiedy oddasz mi książkę?
                </p>
            </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        return message


if __name__ == '__main__':
    emm = EmailSenderManager()
    message = emm.message()
    emm.send(message)
