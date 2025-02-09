from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time

current_time = time.time()


def main():
    with webdriver.Chrome() as driver:
        driver.get("https://parsinger.ru/selenium/5.5/5/1.html")

        divs = driver.find_elements(By.CSS_SELECTOR, "#main-container > div")

        for div in divs:
            # Получаем HEX цвет
            color_span = div.find_element(By.TAG_NAME, "span")
            hex_color = color_span.text

            # Выбираем цвет в выпадающем списке
            dropdown = Select(div.find_element(By.TAG_NAME, "select"))
            dropdown.select_by_visible_text(hex_color)

            # Нажимаем на кнопку с атрибутом data-hex
            button = div.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]')
            button.click()

            # Ставим чекбокс
            checkbox = div.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
            checkbox.click()

            # Вставляем HEX цвет в текстовое поле
            text_field = div.find_element(By.CSS_SELECTOR, "input[type='text']")
            text_field.send_keys(hex_color)

            # Нажимаем кнопку "Проверить"
            check_button = div.find_element(By.XPATH, ".//button[text()='Проверить']")
            check_button.click()

        # Нажимаем кнопку "Проверить все элементы"
        check_all_button = driver.find_element(By.XPATH, "//button[text()='Проверить все элементы']")
        check_all_button.click()

        # Получаем и выводим текст алерта
        alert = Alert(driver)
        print(alert.text)
        alert.accept()
        print(f"Время выполнения скрипта: {time.time() - current_time} сек")


if __name__ == "__main__":
    main()