import time

from pynput.mouse import Button, Controller
# from pynput import mouse
import logging

logging.basicConfig(
    filename='mouse_pointer1.txt',
    filemode='w',
    format='',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.INFO,
    encoding='utf8'
)


mouse_controler = Controller()

# Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))
# Set pointer positionq
mouse_controler.position = (800, 432)

# print('Now we have moved it to {0}'.format(
#     mouse_controler.position))
# Move pointer relative to current position
mouse_controler.move(105, -505)
#
# # Press and release
# mouse.press(Button.right)                    #####
# mouse.release(Button.right)
#
# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     logging.info("{0}".format((x, y)))
# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))
#
#
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))
#
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()