import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    a = ((12434107696 * 3) * 2) + 1
    browser.get('https://parsinger.ru/selenium/6/6.html')
    element = browser.find_element(By.XPATH, "//*[@id='selectId']")
    element.send_keys(f'{a}')
    send_message = browser.find_element(By.CLASS_NAME, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(f'{result}.Выполнили задачу за {(time.time() - current_time):.4} сек.')
    time.sleep(5)

