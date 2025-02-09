import time
from selenium import webdriver
from selenium.webdriver.common.by import By


current_time = time.time()

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/5/1.html')

    containers = driver.find_elements(By.XPATH, '/html/body/div/div')
    for con in containers:
        hex_code = con.find_element(By.TAG_NAME, 'span').text  # Получаем HEX цвет
        con.find_element(By.CSS_SELECTOR, f'option[value="{hex_code}"]').click()  # Выбираем цвет в выпадающем списке
        con.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()  # Ставим чекбокс
        con.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(hex_code)  # Вставляем HEX цвет в текстовое поле
        con.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_code}"]').click()   # Нажимаем на кнопку с атрибутом data-hex
        con.find_element(By.XPATH, ".//button[text()='Проверить']").click()  # Нажимаем кнопку "Проверить"

    driver.find_element(By.XPATH, "//button[text()='Проверить все элементы']").click()

    answer = driver.switch_to.alert.text

print(f'Число {answer}. Время выполнение {(time.time() - current_time):.3} сек')