import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    elements = browser.find_elements(By.CLASS_NAME, 'btn')
    sum_results =0
    for element in elements:
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        result = browser.find_element(By.ID,'result')
        sum_results += int(result.text)
        time.sleep(1)
    print (sum_results)