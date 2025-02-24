from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.9/6/index.html")


try:
    # Ожидание активации чекбокса
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "myCheckbox"))
    )

    # Ожидание активации чекбокса (чекбокс должен быть выбран)
    WebDriverWait(driver, 10).until(
        EC.element_located_to_be_selected((By.ID, "myCheckbox"))
    )

    # Нажатие на кнопку "Проверить"
    check_button = driver.find_element(By.XPATH, '//button[text()="Проверить"]')
    check_button.click()

    # Получение значения из <p id="result"></p>
    result = driver.find_element(By.ID, "result")
    print(result.text)

finally:
    driver.quit()