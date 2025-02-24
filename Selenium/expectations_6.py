import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')

    buttons = browser.find_elements(By.CLASS_NAME, 'box_button')
    result_lst = []

    for button in buttons:
        button.click()
        if WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'ad_window'))):
            browser.find_element(By.ID, 'close_ad').click()
            WebDriverWait(browser, 30).until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
            time.sleep(5)
        result_lst.append(button.text)
    print('-'.join(result_lst))

