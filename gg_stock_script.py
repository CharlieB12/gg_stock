import pyautogui
import pyperclip
import time
import re
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController
import pydirectinput
import random


def read_discord_message():
    human_like_move(2043, 1289)
    pyautogui.rightClick()
    human_like_move(2116, 1076)
    pyautogui.leftClick()

    time.sleep(.2)

    message = pyperclip.paste()
    return message

def human_like_move(x, y, steps=30):
    start_x, start_y = pyautogui.position()
    for i in range(steps):
        # Calculate incremental step with small random jitter
        new_x = start_x + (x - start_x) * (i / steps) + random.randint(-3, 3)
        new_y = start_y + (y - start_y) * (i / steps) + random.randint(-3, 3)
        pyautogui.moveTo(new_x, new_y, duration=0.01)
        time.sleep(0.005)






#python edits ahk script to scroll and click. saves file and runs.









def buy_seed(scroll_amnt):
    mouse = MouseController()
    time.sleep(.5)
    keyboard = Controller()
    time.sleep(.5)

    
    human_like_move(403, 150)
    time.sleep(.4)
    pydirectinput.click()
    time.sleep(.3)
    pydirectinput.click()


    keyboard.press('e')
    keyboard.release('e')
    time.sleep(3)

    time.sleep(3)

    human_like_move(656, 607)
    time.sleep(.4)
    pydirectinput.click()

    time.sleep(1)
    
    mouse.scroll(0, scroll_amnt)
    time.sleep(1)

    pydirectinput.click()
    time.sleep(1)

    human_like_move(422, 823)
    time.sleep(.4)
    pydirectinput.click()

    human_like_move(656, 607)
    time.sleep(.4)
    pydirectinput.click()

    mouse.scroll(0, 60)

    time.sleep(1)
    human_like_move(1025, 402)
    time.sleep(.4)
    pydirectinput.click()

    return






message = read_discord_message()

role_map = {
    '1386133051578253511': 0,
    '1391308588932137043': -20, #-  coconut
    '1391308636898328656': -22, #-  cactus
    '1391308688987521074': -24, #-  dragon fruit
    '1391308728954912778': -26, #-  mango
    '1391308760655593494': -28, #-  grape
    '1391308792255479910': -30, #-  mushroom
    '1391308831203528714': -32, #-  pepper
    '1391308905736310814': -34, #-  cacao
    '1391308945515216916': -36, #-  beanstalk
    '1391308986757939300': -38, #-  ember lily
    '1386133051578253506': -40, #-  sugar apple
    '1391309039048196127': -42 #-  burning bud

}

watchlist_ids = [
    '1386133051578253511',
    '1391308588932137043',  #-  coconut
    '1391308636898328656',  #-  cactus
    '1391308688987521074',  #-  dragon fruit
    '1391308728954912778',  #-  mango
    '1391308760655593494',  #-  grape
    '1391308792255479910',  #-  mushroom
    '1391308831203528714',  #-  pepper
    '1391308905736310814',  #-  cacao
    '1391308945515216916',  #-  beanstalk
    '1391308986757939300',  #-  ember lily
    '1391309039048196127',  #-  burning bud
    '1386133051578253506'   #-  sugar apple
]

found_ids = re.findall(r"<@&(\d+)>", message)
for role_id in watchlist_ids:
    if role_id in found_ids:
        print(role_id + " is in stock!")
        buy_seed(role_map[role_id])
    else:
        print(role_id + " is NOT in stock.")