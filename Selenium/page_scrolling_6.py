import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


current_time = time.time()

options_chrome = webdriver.ChromeOptions()
#options_chrome.add_argument('--headless')
#options_chrome.add_argument('--disable-gpu')

with webdriver.Chrome(options_chrome) as driver:
    driver.get('https://parsinger.ru/scroll/2/index.html')

    items = driver.find_elements(By.CLASS_NAME, 'item')

    total = 0
    for item in tqdm(items):
        checkbox = item.find_element(By.TAG_NAME, 'input')
        ActionChains(driver).click(checkbox).perform()
        number = item.find_element(By.TAG_NAME, 'span').text
        if number:
            total += int(number)

print(f'Сумма {total}. Время выполнение {(time.time() - current_time):.3} сек')


