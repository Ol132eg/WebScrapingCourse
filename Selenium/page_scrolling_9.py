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
    driver.get('https://parsinger.ru/infiniti_scroll_3/')

    time.sleep(2)

    total = 0
    for i in range(1, 6):
        scroll_container = driver.find_element(By.ID, f'scroll-container_{i}')

        scrolls = 10
        while scrolls > 0:
            scroll_container.send_keys(Keys.END)
            scrolls -= 1
            time.sleep(0.5)

        span_elements = scroll_container.find_elements(By.TAG_NAME, 'span')
        for span in tqdm(span_elements):
            total += int(span.text)

print(f'Сумма {total}. Время выполнение {(time.time() - current_time):.3} сек')