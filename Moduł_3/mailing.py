import os
import ssl
import smtplib
from collections import namedtuple
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv
from dotenv import load_dotenv


def config_to_email():
    cwd = os.getcwd()
    if os.path.exists(cwd + r'\.env'):
        load_dotenv()
        first_name = str(getenv('FIRST_NAME'))
        last_name = str(getenv('LAST_NAME'))
        sender_email = str(getenv('NOTIFICATIONS_EMAIL_ADDRESS'))
        password = str(getenv('NOTIFICATIONS_EMAIL_PASSWORD'))
        port = int(getenv('PORT'))

        em_config = namedtuple('email_config_from_env', 'first_name last_name sender_email password port ')
        return em_config(first_name, last_name, sender_email, password, port)


class EmailConfiguration:
    """ Settings for email, defining addresses for sender and receiver.
        For convenient use, you should set new environmental variables define in file '.env'.
    """
    def __init__(self):
        email_config = config_to_email()
        self.first_name = email_config.first_name
        self.last_name = email_config.last_name
        self.port = email_config.port
        self.sender = email_config.sender_email
        _, domain = self.sender.split('@')
        self.password = email_config.password
        self.host = "smtp.{}".format(domain)


class EmailSenderManager(EmailConfiguration):
    """Email sender class. Has methods send() to send email message, and message() to create such one.
    This method does not support any attachments to message"""
    def __init__(self, ssl_enable=False):
        super().__init__()
        self.connection = None
        self.ssl_enable = ssl_enable

    def __enter__(self):
        if not self.ssl_enable:
            self.connection = smtplib.SMTP(self.host, self.port)
        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(self.host, self.port, context=context)
            self.connection.login(self.sender, self.password)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def send_mail(self, receiver, msg):
        """
        This function sends given message. It uses a password set from gmail account and that password
        is set as environmental variable >NOTIFICATIONS_EMAIL_PASSWORD=<
        :return: None
        """

        self.connection.sendmail(self.sender, receiver, msg)

    def create_message(self, receiver_name, receiver_email, receiver_book, receiver_lent_date):
        """Create a message to send
        :return: message object of MIMEMultipart type"""

        message = MIMEMultipart("alternative")
        message["Subject"] = "Nowa wiadomość o książkę"
        message["From"] = self.sender
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        # text = """\
        # Hi,
        # How are you?
        # When will you return my book?"""
        html = f"""\
            <html>
                <body>
                    <p>Siemka,{receiver_name}<br>
                        Pamiętasz, że pożyczałeś ode mnie książkę "{receiver_book}"?<br>
                        W dniu {receiver_lent_date} umówiliśmy się, że oddasz mi dzisiaj.<br>
                        Czekam na kontakt w tej sprawie :)
                        Trzymaj się!
                    </p>
                </body>
            </html>
            """

        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        # message.attach(part1)
        message.attach(part2)

        return message.as_string()


