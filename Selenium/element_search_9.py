import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    code_room_keys = browser.find_elements(By.TAG_NAME, 'option')
    adding_key = 0
    for k in code_room_keys:
        adding_key += int(k.text)
    input_field = browser.find_element(By.ID, 'input_result').send_keys(f"{adding_key}")
    send_message = browser.find_element(By.CLASS_NAME, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(f'Наш конечный результат -это число:{result}.Выполнили задачу за {(time.time() - current_time):.4} сек.')


