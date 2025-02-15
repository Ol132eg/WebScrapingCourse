import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/selenium/5.7/3/test/index.html")

    list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:  # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.TAG_NAME, 'input')

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                # Вариант 1 Клавиша вниз
                tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"

                # Вариант 2 Скроллинг к элементу перед кликом
                # browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)

                # Использование небольшой задержки для исключения ошибки недоступности элемента
                time.sleep(0.1)
                tag_input.click()  # Кликаем на элемент
                list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов