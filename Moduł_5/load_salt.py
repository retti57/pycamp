import os
from dotenv import load_dotenv


def load_salt_from_env() -> str:
    cwd = os.getcwd()
    try:
        if not os.path.exists(cwd + '\\.env'):
            raise FileExistsError

    except FileExistsError:
        with open('.env', 'w', encoding='utf8') as file:
            print("This will be saved in '.env' file in this directory")
            input_salt = input('Enter your expression to be "salt" value: ')
            salt_to_write = f"SALT='{input_salt}'"
            file.write(salt_to_write)

    finally:
        load_dotenv()

        return str(os.getenv('SALT'))

