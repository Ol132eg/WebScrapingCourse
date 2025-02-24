from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

url = "https://parsinger.ru/selenium/5.9/7/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    sleep(1)

    for block in browser.find_elements(By.CLASS_NAME, "container"):
        checkbox = block.find_element(By.TAG_NAME, "input")
        button = block.find_element(By.TAG_NAME, "button")
        try:
            WebDriverWait(browser, 10).until(EC.element_to_be_selected(checkbox))
            button.click()
        except TimeoutException as error:
            print(f"ОШИБКА: {error}")
            exit()

    result = browser.find_element(By.ID, "result").text
    print(result)