from selenium import webdriver
from selenium.webdriver.common.by import By
import time
current_time = time.time()
titles_sum=0
with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/blank/3/index.html')
    buttons = browser.find_elements(By.CSS_SELECTOR, 'input[type="button"]')
    for button in buttons:
        button.click()
        tabs = browser.window_handles
        browser.switch_to.window(tabs[-1])
        title = int(browser.title)
        titles_sum += title
        browser.switch_to.window(tabs[0])
    print(titles_sum)
    print(f'Время выполнения {(time.time() - current_time): .3}сек')