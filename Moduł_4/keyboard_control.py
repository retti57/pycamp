import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

def keyboard_typing_sentence(sentence):
    for letter in sentence:
        time.sleep(0.05)
        keyboard.type(letter)

def one_press_cmd_button():
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)

def one_press_2_buttons():
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release(Key.ctrl)
    keyboard.release('l')
def one_press_enter_button():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

