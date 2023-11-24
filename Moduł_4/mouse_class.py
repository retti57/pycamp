from pynput import mouse


class MyMouse:
    def __init__(self):
        self.controller = mouse.Controller()
        self.left_button = mouse.Button.left
        self.middle_button = mouse.Button.middle
        self.right_button = mouse.Button.right

    def set_pointer(self, pos_x, pos_y):
        self.controller.position = (pos_x, pos_y)

    def click_button(self, button, clicks=1):
        match button:
            case 'left':
                self.controller.click(self.left_button, clicks)
            case 'middle':
                self.controller.click(self.middle_button, clicks)
            case 'right':
                self.controller.click(self.right_button, clicks)


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
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
