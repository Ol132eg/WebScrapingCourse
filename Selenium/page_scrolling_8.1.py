import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


current_time = time.time()

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')
options_chrome.add_argument('--disable-gpu')

with webdriver.Chrome(options_chrome) as driver:
    driver.get('https://parsinger.ru/infiniti_scroll_2/')

    time.sleep(2)

    scroll_container = driver.find_element(By.CLASS_NAME, 'scroll-container')

    scrolls = 10
    while scrolls > 0:
        scroll_container.send_keys(Keys.END)
        scrolls -= 1
        time.sleep(1)

    total = 0
    p_elements = scroll_container.find_elements(By.TAG_NAME, 'p')
    for p in tqdm(p_elements):
        total += int(p.text)

print(f'Сумма {total}. Время выполнение {(time.time() - current_time):.3} сек')