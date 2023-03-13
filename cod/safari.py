from selenium import webdriver
import time


url_site_on = "https://www.google.by/"

browser = webdriver.Safari()

try:
    browser.get(url_site_on)
    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()


