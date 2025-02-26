import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/draganddrop/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)

    # Находим элементы
    draganddrop = driver.find_element(By.ID, "field1")
    draganddrop_end = driver.find_element(By.ID, "field2")

    # Выполняем перетаскивание
    ActionChains(driver).drag_and_drop(draganddrop, draganddrop_end).perform()
    result = driver.find_element(By.ID, "result").text
    print(result)
    time.sleep(5)