from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(1)

'''
browser = webdriver.Chrome()
browser.get(url)
button = browser.find_element(by=By.ID, value="sale_button").click()
time.sleep(2)
browser.close()
browser.quit()
'''
