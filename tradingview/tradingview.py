# open tradingview from windows apps
# if not logged in
    #click login
    #click confirm with webrowser
    #if pick-your-login-device pops up
        #select email
    #if straight to email login
    #enter username
    #enter password
    #select stay logged in
    #hit enter

from dotenv import load_dotenv
import os, time
import pyautogui
from pywinauto.application import Application

def wait_for_image(image_to_look_for=[], confidence=0.9, x=0, y=0, field=None):
    global image
    find_image = lambda: next(
        (
            (pyautogui.locateCenterOnScreen(image, confidence=confidence), image)
            for image in image_to_look_for
            if pyautogui.locateCenterOnScreen(image, confidence=confidence)
        ),
        (None, None)
    )
    image_found = None
    while not image_found:
        image_found, image = find_image()
        if image !=None and 'logged_in' in image:
            return image
        if image_found:
            pyautogui.moveTo(image_found.x-x, image_found.y-y)
            pyautogui.click()
            if field is not None and 'tv' in image:
                pyautogui.typewrite(field)
            return image

def tradingview_script():
    global image
    username = os.environ.get('TVUSERNAME')
    password = os.environ.get('TVPASSWORD')
    image = None

    os.system('start explorer shell:appsfolder\\TradingView.Desktop_n534cwy3pjxzj!TradingView.Desktop')
    time.sleep(2)
    window_title = "TradingView"
    while image == None:
        time.sleep(1)
        try:
            tv_app = Application(backend='uia').connect(title=window_title)
            window = tv_app.window(title=window_title)
            print("Tradingview 1st try window ", window)
        except:
            try:
                tv_app = Application(backend='win32').connect(title=window_title)
                window = tv_app.window(title=window_title)
                print("Tradingview 2nd try window ", window)
            except:
                pass
        wait_for_image(['screenshots\\login.PNG', 'screenshots\\logged_in.PNG'])
    if image != 'screenshots\\logged_in.PNG':
        time.sleep(1)
        window.window(title="Sign in").click_input()
        window.window(title="Sign in with browser").click_input()
        tv_unknown_loop = True
        while tv_unknown_loop:
            wait_for_image(['screenshots\\email.PNG',
                            'screenshots\\grant_access.PNG',
                            'screenshots\\tv_username.PNG',
                            'screenshots\\tv_usernameb.PNG'], 0.95, field=username)
            if 'grant_access' in image:
                tv_unknown_loop = False
                break
            wait_for_image(['screenshots\\tv_password.PNG'], 0.95, field=password)
            wait_for_image(['screenshots\\sign_in.PNG'], 0.99, 155, 35)
            wait_for_image(['screenshots\\sign_in.PNG'], 0.9)
            wait_for_image(['screenshots\\grant_access.PNG'])
            if 'grant_access' in image:
                tv_unknown_loop = False
