import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')
    time.sleep(2)
    for source in browser.find_elements(By.CLASS_NAME, 'draganddrop'):
        color_source = source.value_of_css_property('background-color')
        for target in browser.find_elements(By.CLASS_NAME, 'draganddrop_end'):
            color_target = target.value_of_css_property('border-left-color')
            if color_source == color_target:
                ActionChains(browser).drag_and_drop(source, target).perform()
                time.sleep(1)
                break
        time.sleep(2)
    print(browser.find_element(By.ID, 'message').text)