from selenium import webdriver
import time

url_site_on = "https://zyfra:8001"

browser = webdriver.Chrome(executable_path='src\\chromedriver.exe')


def enter():
    try:
        browser.get(url_site_on)
        login_xpath = "/html/body/div/div/div/div/form/div[3]/div/div/div/input"
        password_path = "/html/body/div/div/div/div/form/div[4]/div/div/div/span/input"
        buttom = "/html/body/div/div/div/div/form/button"
        time.sleep(10)
        browser.find_element(by='xpath', value=login_xpath).send_keys('Ошурек М.П.')
        browser.find_element(by='xpath', value=password_path).send_keys(1900)
        browser.find_element(by='xpath', value=buttom).click()

        time.sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()
