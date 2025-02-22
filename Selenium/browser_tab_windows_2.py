import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    for i in range(100):
        element=browser.find_element(By.XPATH,f'/html/body/div/input[{i+1}]')
        element.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        code= element.get_attribute('onclick')[-5:-1]
        # Вставляем код в текстовое поле
        text_field = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
        text_field.send_keys(code)

        # Нажимаем кнопку "Проверить"
        check_button = browser.find_element(By.XPATH, '// *[ @ id = "check"]')
        check_button.click()
        result = browser.find_element(By.ID, 'result').text
        if result != "Неверный пин-код":
            break
print(result)
print(f'Выполнили задачу за {(time.time() - current_time):.4} сек.')






