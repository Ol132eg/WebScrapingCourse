import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')

    element = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    element.click()
    result = int(browser.find_element(By.ID, 'result').text)
    print(result)
