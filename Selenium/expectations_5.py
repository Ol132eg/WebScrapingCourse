from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    locator = (By.CLASS_NAME, 'close')
    locator_1=(By.TAG_NAME,'button')
    close_ad = WebDriverWait(browser, 1).until(EC.element_to_be_clickable(locator)).click()
    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(locator))
    print('Баннер скрыт')
    button_click=WebDriverWait(browser,5).until(EC.element_to_be_clickable(locator_1))
    button_click.click()
    print('Кнопка нажата')
    message =browser.find_element(By.ID,'message')
    print(message.text)

