from keyboard_class import MyKeyboard
from mouse_class import MyMouse
from json import load


class Process:
    def __init__(self, filename):
        self.filename = filename
        self.steps = []
        self.keyboard_controller = MyKeyboard()
        self.mouse_controller = MyMouse()

    def load_steps(self):
        with open('actions.json') as jf:
            self.steps = load(jf)

    def start(self):
        options = {
            'set_pointer': self.mouse_controller.set_pointer,
            'one_press_button': self.keyboard_controller.one_press_button,
            'type_sentence': self.keyboard_controller.type_sentence,
            'one_press_2_buttons': self.keyboard_controller.one_press_2_buttons,
            'click_button': self.mouse_controller.click_button
        }

        for step in self.steps:
            for key, value in step.items():
                if key in options.keys():
                    options[key](**value)


if __name__ == '__main__':

    process = Process('actions.json')
    process.load_steps()
    process.start()
