import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.10/4/index.html')
    driver.maximize_window()
    time.sleep(1)
    actions = ActionChains(driver)

    for ball in driver.find_elements(By.CLASS_NAME, 'ball_color'):
        ball_color = ball.get_attribute('class').split()[1].replace('_ball', '')
        basket = driver.find_element(By.CLASS_NAME, ball_color)
        actions.drag_and_drop(ball, basket).perform()

    time.sleep(3)
    print(driver.find_element(By.CLASS_NAME, 'message').text)