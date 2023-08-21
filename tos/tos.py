# open tos
# input password
# hit enter

from dotenv import load_dotenv
import os, time
from pywinauto.application import Application
import pyautogui

def tos_script():
    password = os.environ.get('TOSPASSWORD')
    window_title = "Logon to thinkorswim"

    os.system('start explorer "C:\\Program Files\\thinkorswim\\thinkorswim.exe"')

    exit_loop = False
    while not exit_loop:
        time.sleep(1)
        try:
            tos_app = Application(backend='uia').connect(title=window_title)
            window = tos_app.window(title=window_title)
            print("TOS First try")
            exit_loop = True
        except:
            try:
                tos_app = Application(backend='win32').connect(title=window_title)
                window = tos_app.window(title=window_title)
                print("TOS Second try")
                exit_loop = True
            except:
                pass
    pwd_field = pyautogui.locateCenterOnScreen('screenshots\\tos_password.PNG', confidence=0.8)
    print("TOS pwd ", pwd_field)
    pyautogui.moveTo(pwd_field)
    pyautogui.click()
    pyautogui.typewrite(password)
    pyautogui.press('Enter')
    print("TOS complete")
