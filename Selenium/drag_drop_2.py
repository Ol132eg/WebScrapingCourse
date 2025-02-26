import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/3/index.html')
    slider = driver.find_element(By.ID,'block1')
    width = slider.size['width']
    print(width)
    # Вычислите смещение для 1 единицы
    offset = width*2.45
    actions = ActionChains(driver)
    # Нажмите на ползунок и удерживайте кнопку мыши
    actions.click_and_hold(slider).perform()
    # В цикле перемещайте ползунок на 1 единицу
    for _ in range(5):
        actions.move_by_offset(offset, 0).perform()
        time.sleep(0.1)
    # Отпустите кнопку мыши
    actions.release(slider).perform()
    locator = (By.ID, "message")
    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    if message:
        print(message.text)