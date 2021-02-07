from os import wait
from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()


options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
driver.get('https://www.instagram.com/')
driver.implicitly_wait(3)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
btn = driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
username.send_keys(os.getenv('USERNAME'))
password.send_keys(os.getenv('PASSWORD'))

btn.click()
driver.implicitly_wait(3)

not_now_btn = driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]')
not_now_btn.click()
driver.implicitly_wait(6)

field = driver.find_element_by_xpath('//div[@class="LWmhU _0aCwM"]')
field.click()
driver.implicitly_wait(2)
search_bar = driver.find_element_by_xpath('//input[@type="text"]')
search_bar.send_keys('python'+Keys.ENTER)

driver.implicitly_wait(3)

acc = driver.find_element_by_xpath('//a[@class="-qQT3"]')
acc.click()

driver.implicitly_wait(3)


