import time
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    result = [int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]
    print(sum(result))