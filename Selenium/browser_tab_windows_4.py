import time
from selenium.webdriver.common.by import By
from selenium import webdriver
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
    print(browser.get_window_size())
    time.sleep(5)
    browser.set_window_size(571, 702)
    print(browser.get_window_size())
    element = browser.find_element(By.ID, 'result')
    print(element.text)
    time.sleep(5)