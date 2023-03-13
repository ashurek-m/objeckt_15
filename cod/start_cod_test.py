from selenium import webdriver


url_site_on = "https://www.google.by/"

browser = webdriver.Chrome(executable_path='src\\chromedriver.exe')
browser.get(url_site_on)

