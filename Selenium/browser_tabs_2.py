from selenium import webdriver
from selenium.webdriver.common.by import By
import time
current_time = time.time()
with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/blank/3/index.html')
    buttons = driver.find_elements(By.CLASS_NAME, 'buttons')
    for button in buttons:
        button.click()
        time.sleep(1)
        handles = driver.window_handles
        sum_title=0
    for handle in handles:
        driver.switch_to.window(handle)
        title = driver.execute_script("return document.title;")
        if title !='alert':
            sum_title+=int(title)
    print(sum_title)
    print(f'Время выполнения {(time.time() - current_time): .3}сек')