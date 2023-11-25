import time

from pynput.keyboard import Key, Controller


class MyKeyboard:
    def __init__(self):
        self.controller = Controller()

    @staticmethod
    def _get_value(button_str):
        return getattr(Key, button_str)

    def type_sentence(self, sentence, sleep_time):
        for letter in sentence:
            time.sleep(sleep_time)
            self.controller.type(letter)

    def one_press_button(self, key, sleep_time):
        try:
            self.controller.tap(self._get_value(key))
        except AttributeError:
            self.controller.tap(key)
        finally:
            time.sleep(sleep_time)

    def one_press_2_buttons(self, spec_key, norm_key, sleep_time):
        try:
            self.controller.press(self._get_value(spec_key))
            self.controller.tap(self._get_value(norm_key))
            self.controller.release(self._get_value(spec_key))

        except AttributeError:
            self.controller.tap(norm_key)
            self.controller.release(self._get_value(spec_key))
        finally:
            time.sleep(sleep_time)
