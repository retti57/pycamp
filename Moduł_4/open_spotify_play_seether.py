from pynput.mouse import Button, Controller
import time
from keyboard_control import keyboard_typing_sentence, one_press_cmd_button, one_press_2_buttons, one_press_enter_button


if __name__ == '__main__':
    # open start-menu
    one_press_cmd_button()
    time.sleep(1.5)
    # type-in 'spotify' in search tool-bar
    keyboard_typing_sentence('spotify')
    time.sleep(1.5)

    one_press_enter_button()
    time.sleep(4)

    # press simultanously ctrl + L to open search tool-bar in spotify
    one_press_2_buttons()
    time.sleep(4)

    # type-in 'seether' in search tool-bar
    keyboard_typing_sentence('seether')
    time.sleep(4)
    # wait until searching end and hit enter button
    one_press_enter_button()
    time.sleep(3)

    # move mouse pointer to play icon
    mouse_controller = Controller()
    mouse_controller.position = (800, 432)
    time.sleep(1.5)

    mouse_controller.press(Button.left)
    mouse_controller.release(Button.left)