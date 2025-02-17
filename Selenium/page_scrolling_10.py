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
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')
    time.sleep(1)
    scroll_container = driver.find_element(By.ID, 'main_container')
    scrolls = 10
    while scrolls > 0:
        scroll_container.send_keys(Keys.END)
        scrolls -= 1
        time.sleep(0.3)
    p_elements = scroll_container.find_elements(By.TAG_NAME, 'input')
    for p in tqdm(p_elements):
        if int(p.get_attribute('value')) % 2 == 0:
            p.click()
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME,'alert_button').click()
    alert=driver.switch_to.alert
    alert_text = alert.text
    time.sleep(1)

print(f'{alert_text}. Время выполнение {(time.time() - current_time):.4} сек')