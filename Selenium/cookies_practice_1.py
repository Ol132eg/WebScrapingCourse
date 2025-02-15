import time
from selenium import webdriver
current_time = time.time()

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    sum_value=0
    for cookie in cookies:
        sum_value += int(cookie["value"])
    print(f'Число {sum_value}. Время выполнение {(time.time() - current_time):.3} сек')
