from selenium import webdriver
from selenium.webdriver.common.by import By
import time
current_time = time.time()
code_sum=0
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]
with webdriver.Chrome() as browser:
    for site in sites:
        browser.switch_to.new_window("tab")
        browser.get(site)
        checkbox=browser.find_element(By.CSS_SELECTOR, 'input[class="checkbox_class"]').click()
        code=browser.find_element(By.ID, 'result').text
        code_sum+=int(code)**0.5

    print(round(code_sum,9))
    print(f'Время выполнения {(time.time() - current_time): .3}сек')
    time.sleep(3)



