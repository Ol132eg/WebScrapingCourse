import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/2/index.html')

    time.sleep(1)
    for i in range(1,11):
        element_to_drag = driver.find_element(By.ID, f"draganddrop{i}")
        ActionChains(driver).drag_and_drop_by_offset(element_to_drag, 866, 0).release().perform()
    message = driver.find_element(By.ID,"message")
    print(message.text)

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    time.sleep(1)
    drag = browser.find_element(By.ID, 'draggable')
    actions = ActionChains(browser)
    bloks = browser.find_elements(By.CLASS_NAME, "box")
    for x in bloks:
        actions.drag_and_drop(drag, x).release().perform()
    print(browser.find_element(By.ID, 'message').text)