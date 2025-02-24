from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/4/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    substring_title = WebDriverWait(browser, 35,0.1).until(EC.title_contains("JK8HQ"))
    if substring_title:
        print(browser.title)
#    print(browser.execute_script("return document.title;"))