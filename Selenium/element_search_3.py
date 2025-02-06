import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#with webdriver.Chrome() as browser:
#    browser.get('https://parsinger.ru/selenium/1/1.html')
#    input_form = browser.find_elements(By.CLASS_NAME, 'form_box')
#    for i in input_form:
#        input_field = i.find_element(By.CLASS_NAME, 'form').send_keys("Текст")
#    send_message =browser.find_element(By.CLASS_NAME, 'btn').click()
#    result = int(browser.find_element(By.ID, 'result').text)
#    print(result)
#    time.sleep(30)
keys = ['Тихон', 'Котов', 'Евгеньевич', '23', 'Санкт-Петербург', 'tixon.kotov@gmail.com']

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    for data, element in zip(keys, browser.find_elements(By.TAG_NAME, 'input')):
        input_form = element.send_keys(data)

    browser.find_element(By.CLASS_NAME, 'btn').click()
    result = int(browser.find_element(By.ID,'result').text)
    print(result)
    time.sleep(30)