import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'check')
    for i in input_form:
        input_field = i.click()
    send_message = browser.find_element(By.CLASS_NAME, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)
    time.sleep(5)