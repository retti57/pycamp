import base64
import pathlib

from load_salt import load_salt_from_env
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EncryptDecrypt:
    """ Common data and function for encryption or decryption of file"""
    verbosity = None

    def __init__(self, path: pathlib.Path):
        self.path = path

    @staticmethod
    def create_key(password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=bytes(load_salt_from_env().encode('utf8')),
            iterations=390000
        )

        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf8')))
        return key


class Decryption(EncryptDecrypt):
    def execute(self, password):
        with open(self.path, 'r') as file:
            data_to_decrypt = file.read()

        fernet = Fernet(self.create_key(password))
        decrypted_content = fernet.decrypt(data_to_decrypt.encode('utf8'))

        with open(self.path.rename(self.path.with_suffix('.txt')), 'w') as file:
            file.write(decrypted_content.decode('utf8'))


class Encryption(EncryptDecrypt):

    def execute(self, password):
        with open(self.path, 'r') as file:
            data_to_encrypt = file.read()

        fernet = Fernet(self.create_key(password))
        encrypted_content = fernet.encrypt(data_to_encrypt.encode('utf8'))

        with open(self.path.rename(self.path.with_suffix('.dokodu')), 'w') as file:
            file.write(encrypted_content.decode('utf8'))


class Append(EncryptDecrypt):
    def __init__(self, path: pathlib.Path, text):
        self.text = text
        super().__init__(path)

    def execute(self, password):
        with open(self.path, 'r') as file:
            data = file.read()

        fernet = Fernet(self.create_key(password))
        encrypted_content = fernet.decrypt(data).decode('utf8')

        encrypted_content += '\n'
        encrypted_content += self.text

        decrypted_content = fernet.encrypt(encrypted_content.encode('utf8'))

        with open(self.path, 'w') as file:
            file.write(decrypted_content.decode('utf8'))
