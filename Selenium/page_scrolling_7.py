import time
#from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


current_time = time.time()

options_chrome = webdriver.ChromeOptions()
#options_chrome.add_argument('--headless')
#options_chrome.add_argument('--disable-gpu')

data = []
count = []
with webdriver.Chrome(options_chrome) as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    flag = True
    while flag:
        element = browser.find_element(By.CSS_SELECTOR, '.scroll-container').find_elements(By.CSS_SELECTOR, 'span')
        for el in element:
            if el.get_attribute('class') == 'last-of-list':
                flag = False
            if el not in data:
                el.find_element(By.CSS_SELECTOR, 'input').send_keys(Keys.DOWN)
                data.append(el)
                count.append(int(el.text))



print(f'Сумма {sum(count)}. Время выполнение {(time.time() - current_time):.3} сек')


