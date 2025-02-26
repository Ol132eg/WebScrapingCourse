import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    browser.implicitly_wait(10)
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    time.sleep(1)
    elements = browser.find_elements(By.CSS_SELECTOR, '.piece')
    target = browser.find_elements(By.CSS_SELECTOR, '.range')
    for el, tar in zip(elements, target):
        actions.drag_and_drop(el, tar).perform()
    time.sleep(2)
    print(browser.find_element(By.ID, 'message').text)