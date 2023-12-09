""" Main script for running password validator based on given passwords in text file"""
import logging
from hashlib import sha1
from password_validators.validators import PasswordValidator, ValidationError

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(asctime)s : %(process)d-%(levelname)s-%(message)s ',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG
)


def main(input_filename: str = 'passwords.txt'):
    """Function checks given password"""

    with (open(input_filename, encoding='utf8') as input_file,
          open('bezpieczne.txt', 'a', encoding='utf8') as output_file):
        for password in input_file:
            print('Sprawdzam : ', password)
            try:
                strip_password = password.strip()

                logging.info(f'Checking - {strip_password}')
                validator = PasswordValidator(strip_password)
                validator.is_valid()

                logging.info('** Safe and valid **')
                hashed = sha1(strip_password.encode('utf8')).hexdigest()
                output_file.write(hashed + '\n')
                print('zapisano')
                logging.info(f'Very unsafe action: ## {hashed} ##')
            except ValidationError as error:
                logging.warning(error)
                print(strip_password, error)


if __name__ == '__main__':

    logging.debug('Executing PassValid.py')
    main()
