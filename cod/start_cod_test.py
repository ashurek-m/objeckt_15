from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://zyfra:8001"

#browser = webdriver.Chrome(executable_path='src\\chromedriver.exe')

'''
def enter():
    try:
        browser.get(url_site_on)
        buttom_dop = "/html/body/div/div[2]/button[3]"
        browser.find_element(by='xpath', value=buttom_dop).click()
        small_link = "/html/body/div/div[3]/p[2]/a"
        browser.find_element(by='xpath', value=small_link).click()
        login_xpath = "/html/body/div/div/div/div/form/div[3]/div/div/div/input"
        password_path = "/html/body/div/div/div/div/form/div[4]/div/div/div/span/input"
        buttom = "/html/body/div/div/div/div/form/button"
        browser.find_element(by='xpath', value=login_xpath).send_keys('Ошурек М.П.')
        browser.find_element(by='xpath', value=password_path).send_keys(1900)
        browser.find_element(by='xpath', value=buttom).click()
        time.sleep(5)
        #contr_proizv = "/html/body/div[3]/div/div/ul/li"
        #browser.find_element(by='xpath', value=contr_proizv)
        #chek_order = "/html/body/div[1]/div/section/aside/div/div[2]/div[1]/div/div[1]/div[2]/div/ul/li[5]/ul/li[2]"
        #browser.find_element(by='xpath', value=chek_order).click()

        time.sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()
'''

with webdriver.Chrome() as browser:
    browser.get(url)
    buttom_dop = "/html/body/div/div[2]/button[3]"
    browser.find_element(by='xpath', value=buttom_dop).click()
    small_link = "/html/body/div/div[3]/p[2]/a"
    browser.find_element(by='xpath', value=small_link).click()
    login_xpath = "/html/body/div/div/div/div/form/div[3]/div/div/div/input"
    password_path = "/html/body/div/div/div/div/form/div[4]/div/div/div/span/input"
    buttom = "/html/body/div/div/div/div/form/button"
    browser.find_element(by=By.ID, value='login').send_keys('Ошурек М.П.')
    browser.find_element(by=By.ID, value='password').send_keys(1900)
    #browser.find_element(by='xpath', value=buttom).click()
    time.sleep(2)
