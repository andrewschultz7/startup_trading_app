# open tos
# input password
# hit enter

from dotenv import load_dotenv
import os, time
from pywinauto.application import Application
import pyautogui

def tos_script():
    password = os.environ.get('TOSPASSWORD')
    os.system('start explorer "C:\\Program Files\\thinkorswim\\thinkorswim.exe"')
    window_title = "Logon to thinkorswim"
    exit_loop = False
    while not exit_loop:
        time.sleep(1)
        try:
            Application(backend='uia').connect(title=window_title)
            exit_loop = True
        except:
            try:
                Application(backend='win32').connect(title=window_title)
                exit_loop = True
            except:
                pass
    pwd_entered = None
    time.sleep(3)
    while not pwd_entered:
        pwd_field = pyautogui.locateCenterOnScreen('screenshots\\tos_password.PNG', confidence=0.94)
        time.sleep(2)
        while pwd_field:
            pyautogui.moveTo(pwd_field)
            pyautogui.click(pwd_field)
            pyautogui.typewrite(password)
            pwd_entered = pyautogui.locateCenterOnScreen('screenshots\\tos_passwordEntered.PNG', confidence=0.92)
            if pwd_entered:
                pyautogui.press('Enter')
                pwd_field = None
