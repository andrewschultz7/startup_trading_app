#open browser
#goto tradovate site
#goto username field
#enter username
#goto pwd field
#enter pwd
#hit enter

from dotenv import load_dotenv
import os, time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def tradovate_script():
    try:
        username = os.environ.get("USERNAME2")
        password = os.environ.get("PASSWORD2")
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        global driver
        driver = webdriver.Chrome(
            options=chrome_options,
            service=ChromeService(ChromeDriverManager().install())
            )
        driver.maximize_window()
        driver.get('https://trader.tradovate.com/welcome')
        WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="name-input"]')))
        username_field = driver.find_element(By.XPATH, '//*[@id="name-input"]')
        username_field.send_keys(username)
        password_field = driver.find_element(By.XPATH, '//*[@id="password-input"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        time.sleep(2)
    except Exception as e:
        print("TRADOVATE error ", str(e))
