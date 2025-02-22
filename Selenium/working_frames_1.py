import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')
    for i in range(9):
        iframe_element = driver.find_element(By.ID, f'iframe{i+1}')
        driver.switch_to.frame(iframe_element)
        iframe_content = driver.page_source
        check_button = driver.find_element(By.TAG_NAME, 'button').click()
        number=driver.find_element(By.ID, 'numberDisplay').text
        driver.switch_to.default_content()
        guess_input = driver.find_element(By.ID, 'guessInput')
        guess_input.clear()
        guess_input.send_keys(number)
        chk_button = driver.find_element(By.ID, 'checkBtn').click()

        time.sleep(1)
    alert = driver.switch_to.alert
    print(alert.text)


