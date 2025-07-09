import pyautogui
import pyperclip
import time
import re
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController
import subprocess
import tempfile


def read_discord_message():
    pyautogui.moveTo(2043, 1289)
    pyautogui.rightClick()
    pyautogui.moveTo(2116, 1076)
    pyautogui.leftClick()

    time.sleep(.2)

    message = pyperclip.paste()
    return message




def buy_seed(scroll_amnt):
    

    ahk_code = f"""
    #Requires AutoHotkey v2.0

    CoordMode("Mouse", "Screen")
    CoordMode("Pixel", "Screen")
    CoordMode("ToolTip", "Screen")

    Click(395, 151)
    Sleep(500)
    Click(395, 151)
    Sleep(500)
    Send("e")
    Sleep(1000)
    MouseMove(1000, 618)
    Sleep(200)
    MouseMove(1002, 620)
    Sleep(200)
    MouseMove(1000, 618)
    Sleep(400)
    Loop {scroll_amnt} {{
        Click("WheelDown")
    }}
    Sleep(700)
    Click()
    Sleep(600)
    MouseMove(417, 830)
    Sleep(300)
    MouseMove(419, 832)
    Sleep(300)
    Loop 5 {{
        Click()
        sleep(400)
    }}
    Sleep(700)
    MouseMove(1000, 618)
    Sleep(300)
    MouseMove(1002, 620)
    Sleep(700)
    Click()
    Sleep(400)
    Loop 60 {{
        Click("WheelUp")
    }}
    Sleep(700)
    MouseMove(1030, 400)
    MouseMove(1032, 402)
    Click()
    """

    with tempfile.NamedTemporaryFile(suffix=".ahk", delete=False, mode='w') as f:
        f.write(ahk_code)
        temp_path = f.name

    # Run the temporary script
    subprocess.run(["C:\\Program Files\\AutoHotkey\\v2\\AutoHotkey.exe", temp_path])






message = read_discord_message()

role_map = {
    '1391308760655593494': 28, #-  grape
    '1391308831203528714': 32, #-  pepper
    '1391308905736310814': 34, #-  cacao
    '1391308945515216916': 36, #-  beanstalk
    '1391308986757939300': 38, #-  ember lily
    '1386133051578253506': 40, #-  sugar apple
    '1391309039048196127': 42 #-  burning bud

}

watchlist_ids = [
    '1391308760655593494',  #-  grape
    '1391308831203528714',  #-  pepper
    '1391308905736310814',  #-  cacao
    '1391308945515216916',  #-  beanstalk
    '1391308986757939300',  #-  ember lily
    '1391309039048196127',  #-  burning bud
    '1386133051578253506'   #-  sugar apple
]


while True:
    message = read_discord_message()
    found_ids = re.findall(r"<@&(\d+)>", message)
    for role_id in watchlist_ids:
        if role_id in found_ids:
            print(role_id + " is in stock!")
            buy_seed(role_map[role_id])
        else:
            print(role_id + " is NOT in stock.")
    pyautogui.moveTo(300, 500)
    time.sleep(1)
    pyautogui.click()
    pyautogui.click()
    time.sleep(300)