import time

from pynput import mouse
# # import logging
from json import load
# logging.basicConfig(
#     filename='mouse_pointer_on_click.txt',
#     filemode='w',
#     format='',
#     datefmt='%d-%m-%Y %H:%M:%S',
#     level=logging.INFO,
#     encoding='utf8'
# )


class MyMouse:
    def __init__(self):
        self.controller = mouse.Controller()
        self.left_button = mouse.Button.left
        self.middle_button = mouse.Button.middle
        self.right_button = mouse.Button.right
        # self.controller.position = None

    def _on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        # logging.info("{0}".format((x, y)))
        if button == self.middle_button:
            return False

    def _on_move(self, x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def _on_scroll(self,x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    def set_pointer(self, pos_x, pos_y):
        self.controller.position = (pos_x, pos_y)

    # def click_button(self, button, clicks=1):
    #     match button:
    #         case 'left':
    #             self.controller.click(self.left_button, clicks)
    #         case 'middle':
    #             self.controller.click(self.middle_button, clicks)
    #         case 'right':
    #             self.controller.click(self.right_button, clicks)


# mouse_controller = MyMouse()

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse_controller.position))
# # Set pointer position
# mouse_controller.position = (800, 432)

# print('Now we have moved it to {0}'.format(
#     mouse_controler.position))
# Move pointer relative to current position
# mouse_controler.move(105, -505)
#
# # Press and release
# mouse.press(Button.right)
# mouse.release(Button.right)
#
# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)


def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    # logging.info("{0}".format((x, y)))
    if button == mouse.Button.middle:
        return False


def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


# with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
    # listener.join()
# with open('actions.json') as file:
#     actions = load(file)
#     m = actions[0]
#     k = actions[1]
#     print(actions[0]["steps"])
#     print(m["steps"])
listener = MyMouse()
time.sleep(1)
listener.set_pointer(250,800)
