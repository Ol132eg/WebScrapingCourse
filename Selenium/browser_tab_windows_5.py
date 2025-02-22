import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from itertools import product

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
    for x, y in product(window_size_x, window_size_y):
        browser.set_window_size(x + 16, y + 147)
        element = browser.find_element(By.ID, 'result')
        print(element.text)
        time.sleep(5)
