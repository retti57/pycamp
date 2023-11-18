from unittest.mock import patch
from mailing import EmailSenderManager


@patch('smtplib.SMTP_SSL')
def test_sendmail_SSL(mock_smtp):

    with EmailSenderManager(ssl_enable=True) as server:

        server.send_mail('docz9856@wp.pl', 'abv')
        mock_smtp.assert_called()


@patch('smtplib.SMTP')
def test_sendmail_noSSL(mock_smtp):

    with EmailSenderManager(ssl_enable=False) as server:

        server.send_mail('docz9856@wp.pl', 'abv')
        mock_smtp.assert_called()
