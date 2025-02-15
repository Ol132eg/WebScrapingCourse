import time
from selenium import webdriver
from selenium.webdriver.common.by import By
start_time =time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    elements = browser.find_elements(By.CLASS_NAME,'clickMe')
    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f'Текст на странице: {alert_text}. Время выполнения {(time.time() - start_time):.3} сек.')