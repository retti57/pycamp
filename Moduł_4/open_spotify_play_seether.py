import time
from keyboard_class import MyKeyboard
from mouse_class import MyMouse
from json import load


if __name__ == '__main__':
    with open('actions.json') as file:
        actions = load(file)
        m = actions[0]
        k = actions[1]
        print(m["steps"])
        # open start-menu
        keyboard = MyKeyboard()
        keyboard.one_press_button("cmd", 2)
        # type-in 'spotify' in search tool-bar
        keyboard.type_sentence('spotify',0.25)

        keyboard.one_press_button("enter", 5)

        # press simultanously ctrl + L to open search tool-bar in spotify
        keyboard.one_press_2_buttons('ctrl_l', 'l',4)

        # type-in 'seether' in search tool-bar
        keyboard.type_sentence('nirvana',0.45)

        # wait until searching end and hit enter button
        keyboard.one_press_button('enter',4)

        time.sleep(1)

        # move mouse pointer to play icon
        mouse_controller = MyMouse()
        time.sleep(1.5)
        mouse_controller.set_pointer(800, 432)
        mouse_controller.click_button(mouse_controller.right_button, 1)
