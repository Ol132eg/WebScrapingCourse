import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
start_time =time.time()
with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.7/5/index.html")
    elements = browser.find_elements(By.CLASS_NAME  ,'timer_button')
    for element in elements:
        actions = ActionChains(browser)
        hold_time=float(element.text)
        actions.click_and_hold(element).pause(hold_time).release(element).perform()
        time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f'Текст на странице: {alert_text}. Время выполнения {(time.time() - start_time):.3} сек.')