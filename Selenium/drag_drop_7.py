from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.10/6/index.html")

# Находим все слайдеры и их целевые значения
sliders = driver.find_elements(By.TAG_NAME, "input")
targets = driver.find_elements(By.CLASS_NAME, "target-value")

for slider, target in zip(sliders, targets):
    target_value = int(target.text)  # Получаем значение справа от слайдера
    current_value = int(slider.get_attribute("value"))  # Узнаем текущее положение

    while current_value < target_value:
        slider.send_keys(Keys.ARROW_RIGHT)
        current_value = int(slider.get_attribute("value"))

    while current_value > target_value:
        slider.send_keys(Keys.ARROW_LEFT)
        current_value = int(slider.get_attribute("value"))

# Ждем появления кода после установки слайдеров
secret_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "message"))).text
print(f"Тайный код: {secret_code}")

# Закрываем браузер
driver.quit()