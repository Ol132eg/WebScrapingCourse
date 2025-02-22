import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    pin_codes = browser.find_elements(By.CSS_SELECTOR,'span')
    for pin in pin_codes:
        extracted_text = pin.text
        check_button = browser.find_element(By.XPATH, '// *[ @ id = "check"]')
        check_button.click()
        time.sleep(0.2)
        prompt = browser.switch_to.alert
        prompt.send_keys(extracted_text)
        prompt.accept()
        result = browser.find_element(By.ID, 'result').text
        if result != "Неверный пин-код":
            break
    print(result)
    print(f'Выполнили задачу за {(time.time() - current_time):.4} сек.')





