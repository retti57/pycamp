import time

from pynput.keyboard import Key, Controller


class MyKeyboard:
    def __init__(self):
        self.controller = Controller()

    @staticmethod
    def _get_val(button_str):
        return getattr(Key, button_str)

    def type_sentence(self, sentence, sleep_time):
        for letter in sentence:
            time.sleep(sleep_time)
            self.controller.type(letter)

    def one_press_button(self, key, sleep_time):
        self.controller.tap(self._get_val(key))
        time.sleep(sleep_time)

    def one_press_2_buttons(self, spec_key, norm_key, sleep_time):

        self.controller.press(self._get_val(spec_key))
        self.controller.tap(norm_key)
        self.controller.release(self._get_val(spec_key))

        time.sleep(sleep_time)

