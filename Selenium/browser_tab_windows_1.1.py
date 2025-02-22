import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    for i in range(100):
        element=browser.find_element(By.XPATH,f'/html/body/div/input[{i+1}]').click()
        confirm = browser.switch_to.alert
        confirm.accept()
        result = browser.find_element(By.ID,'result').text
        if result:
            break
print(result)
print(f'Выполнили задачу за {(time.time() - current_time):.4} сек.')


