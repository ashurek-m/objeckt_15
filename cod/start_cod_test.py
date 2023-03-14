from selenium import webdriver
import time

url_site_on = "https://zyfra:8001"

browser = webdriver.Chrome(executable_path='src\\chromedriver.exe')


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
        time.sleep(5)
        browser.find_element(by='xpath', value=login_xpath).send_keys('Ошурек М.П.')
        browser.find_element(by='xpath', value=password_path).send_keys(1900)
        browser.find_element(by='xpath', value=buttom).click()

        time.sleep(5)

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()


enter()
