
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    substring_title = WebDriverWait(browser, 60).until(EC.title_contains("345FDG3245SFD"))
    print(substring_title)
    if substring_title:
        print(browser.find_element(By.ID, 'result').text)

