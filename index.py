# pip3 install seleniumbase
import os
from dotenv import load_dotenv
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

load_dotenv()

userEmail = os.environ.get('USER_CREDENTIALS')
userPassword = os.environ.get('USER_PASSWORD')
driver = Driver(uc=True)
# initialize the driver in GUI mode with UC enabled



# set the target URL

url = "https://www.pathofexile.com/trade2/search/poe2/Standard"



# open URL with a 6-second reconnect time to bypass the initial JS challenge
driver.uc_open_with_reconnect(url, reconnect_time=6)
WebDriverWait(driver, 5)

# POE part
driver.find_element(By.CLASS_NAME, 'splash__continue').click()

WebDriverWait(driver, 5)
usernameTextBox = driver.find_element(By.NAME, 'login_email')
usernameTextBox.send_keys(userEmail)
passwordTextBox = driver.find_element(By.NAME, 'login_password')
passwordTextBox.send_keys(userPassword)

WebDriverWait(driver, 2)
driver.find_element(By.CLASS_NAME, 'sign-in__submit').click()
html = driver.page_source
print(html)

# driver.implicitly_wait(20) 
# test = driver.find_element(By.CSS_SELECTOR, 'input.multiselect__input')
# print(test)
breakpoint()

