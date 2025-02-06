import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    links = browser.find_elements(By.CLASS_NAME, 'text')
    adding_fragments =0
    for link in links:
        keys_treasure = sum(list(map(int, link.text.split('\n'))))
        adding_fragments +=keys_treasure
print(f'Сумма {adding_fragments}. Время выполнение {(time.time() - current_time):.3} сек')
