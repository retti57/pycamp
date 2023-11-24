import time

from pynput.keyboard import Key, Controller


class MyKeyboard:
    def __init__(self):
        self.controller = Controller()

    def type_sentence(self, sentence, sleep_time):
        for letter in sentence:
            time.sleep(sleep_time)
            self.controller.type(letter)

    def one_press_cmd_button(self, sleep_time):
        self.controller.tap(Key.cmd)
        time.sleep(sleep_time)

    def one_press_2_buttons(self, spec_key, norm_key, sleep_time):
        kbrd_special_keys = {'ctrl': Key.ctrl, 'alt': Key.alt, 'cmd': Key.cmd_l, 'enter': Key.enter}
        if spec_key in kbrd_special_keys.keys():
            # with keyboard.pressed(kbrd_special_keys[spec_key]):
            #     keyboard.release(norm_key)
            self.controller.press(kbrd_special_keys[spec_key])
            self.controller.press(norm_key)
            self.controller.release(kbrd_special_keys[spec_key])
            self.controller.release(norm_key)
        time.sleep(sleep_time)

    def one_press_enter_button(self, sleep_time):
        self.controller.tap(Key.enter)
        time.sleep(sleep_time)




