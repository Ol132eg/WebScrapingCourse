import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    text_fields =browser.find_elements(By.TAG_NAME, 'input')
    for text_field in text_fields:
        if not text_field.get_attribute('disabled'):
            text_field.clear()
    verification_button = browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f'Текст на странице: {alert_text}. Время выполнения {(time.time() - current_time):.3} сек.')
    time.sleep(10)