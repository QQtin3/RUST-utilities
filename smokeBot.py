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


# Offset 1 : 100
# Offset 2 : 100
# Case 1 : 700 1000

activated2 = False
unavailable = []

def recycle_smoke(unavailable):
    global activated
    unavailable = [nb - 1 for nb in unavailable]
    for nb_case in range(0, 30):
        if nb_case not in unavailable:
            if nb_case < 6:
                pyautogui.rightClick(700 + 100 * (nb_case % 6), 1000)
                time.sleep(4.5)
            else:
                pyautogui.rightClick(700 + 100 * (nb_case % 6), 1000 - 100 * (nb_case // 6))
                time.sleep(4.5)


thread2 = Thread(target=recycle_smoke, args=[unavailable])


def on_activate_j():
    global activated2
    if not activated2:
        activated2 = True
        print('The bot is now activated!')
        thread2.start()
    else:
        activated2 = False
        print('The bot is now disabled!')


with keyboard.GlobalHotKeys({
    '<ctrl>+j': on_activate_j}) as j:
    j.join()
