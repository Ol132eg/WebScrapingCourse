from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Используем контекстный менеджер 'with', чтобы драйвер закрылся автоматически
with webdriver.Chrome() as driver:
    # Открыть страницу по старой ссылке
    driver.get("https://parsinger.ru/selenium/5.5/3/temp/index.html")

    # Ждем, пока все элементы прогрузятся
    time.sleep(2)

    # Список для хранения собранных чисел
    collected_numbers = []

    # Находим все элементы-обёртки (аналог 'parent', но теперь 'field-wrapper')
    wrappers = driver.find_elements(By.CLASS_NAME, 'field-wrapper')

    # Проходимся по каждому найденному элементу
    for wrapper in wrappers:
        # Находим чекбокс внутри обёртки
        checkbox = wrapper.find_element(By.CSS_SELECTOR, "input.field-checkbox")
        # Находим поле, откуда нужно взять значение (аналог textarea, но теперь input с классом 'field')
        field_value_elem = wrapper.find_element(By.CSS_SELECTOR, "input.field")

        # Проверяем, включен ли чекбокс
        if checkbox.is_selected():
            # Получаем число из атрибута value и добавляем в список
            value_str = field_value_elem.get_attribute("value")
            collected_numbers.append(int(value_str))

    # Выводим собранные числа и их сумму
    print(f"Собранные числа: {collected_numbers}")
    print(f"Сумма чисел: {sum(collected_numbers)}")