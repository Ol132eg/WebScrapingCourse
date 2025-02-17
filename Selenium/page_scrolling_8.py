import time
#from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


current_time = time.time()

options_chrome = webdriver.ChromeOptions()
#options_chrome.add_argument('--headless')
#options_chrome.add_argument('--disable-gpu')

data = []
count = []
with webdriver.Chrome(options_chrome) as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    action =ActionChains(browser)
    flag=True
    while flag:

        elements = browser.find_element(By.CSS_SELECTOR, '.scroll-container').find_elements(By.CSS_SELECTOR, 'p')
        for element in elements:
            if element.get_attribute('class') == 'last-of-list':
                flag = False
            if element not in data:
                action.scroll_to_element(element).perform()
                time.sleep(0.5)
                data.append(element)
                count.append(int(element.text))


print(f'Сумма {sum(count)}. Время выполнение {(time.time() - current_time):.3} сек')