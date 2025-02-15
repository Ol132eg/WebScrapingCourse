from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    urls_elements =  browser.find_elements(By.CSS_SELECTOR, 'a[href]')
    urls_list=[element.get_attribute('href')for element in urls_elements]
    life_span_list = []
    page_cookie_list = []
    for url in urls_list:
        browser.get(url)
        cookies = browser.get_cookies()
        life_span_list.append(cookies[0]['expiry'])
        page_cookie =browser.find_element(By.ID, 'result').text
        page_cookie_list.append(int(page_cookie))
    x=max(life_span_list)
    print(life_span_list.index(x))
    print(page_cookie_list[1])





