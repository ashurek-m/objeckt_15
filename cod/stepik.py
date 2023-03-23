from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def zadanie_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/1/1.html')
        input_form = browser.find_elements(By.CLASS_NAME, 'form')
        input_info = [
            'Maksim',
            'Ashurek',
            'Petrovich',
            '23',
            'Minsk',
            'trooo@gmail.com'
        ]
        i = 0
        for input in input_form:
            input.send_keys(input_info[i])
            i += 1

        browser.find_element(By.ID, 'btn').click()
        time.sleep(5)


'''
browser = webdriver.Chrome()
browser.get(url)
button = browser.find_element(by=By.ID, value="sale_button").click()
time.sleep(2)
browser.close()
browser.quit()

url = 'https://parsinger.ru/selenium/1/1.html'

with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(1)
'''
