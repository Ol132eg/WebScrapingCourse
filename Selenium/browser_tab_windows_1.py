import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    elements = browser.find_elements(By.CSS_SELECTOR,'input')
    for element in elements:
        element.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        if browser.find_element(By.ID,'result').text is not None:
            a=browser.find_element(By.ID,'result').text
        print(a)
        time.sleep(1)


