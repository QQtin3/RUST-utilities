import time
from threading import Thread

import pyautogui
from pynput import keyboard

activated = False
def buy_smoke(free_space, amount):
    global activated
    pyautogui.click(1734, 895)
    pyautogui.write(str(amount), interval=0.05)
    pyautogui.click(1747, 848)
    time.sleep(2.8)
    if free_space - amount > 0 and activated:
        print(free_space)
        buy_smoke(free_space - amount, amount)
    elif free_space > 0 and activated:
        print(free_space)
        buy_smoke(0, free_space)

thread = Thread(target=buy_smoke, args=(23 * 8, 10))

def on_activate_h():
    global activated
    if not activated:
        activated = True
        print('The bot is now activated!')
        thread.start()
    else:
        activated = False
        print('The bot is now disabled!')

with keyboard.GlobalHotKeys({
        '<ctrl>+h': on_activate_h}) as h:
    h.join()