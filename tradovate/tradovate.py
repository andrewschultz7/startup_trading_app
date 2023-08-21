#open browser
#goto tradovate site
#goto username field
#enter username
#goto pwd field
#enter pwd
#hit enter

from dotenv import load_dotenv
import os, time
from pywinauto import Application
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def tradovate_script():
    username = os.environ.get("USERNAME2")
    password = os.environ.get("PASSWORD2")

    driver = webdriver.Chrome()
    driver.get('https://trader.tradovate.com/welcome')

    username_field = driver.find_element(By.XPATH, '//*[@id="name-input"]')
    username_field.send_keys(username)
    password_field = driver.find_element(By.XPATH, '//*[@id="password-input"]')
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    driver.quit()
