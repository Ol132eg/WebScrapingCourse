import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        button= browser.find_element(By.ID, 'result').text
        if button!='refresh page':
            print(button)
            break
        browser.refresh()
    time.sleep(5)
