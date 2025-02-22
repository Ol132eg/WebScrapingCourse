from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/4/index.html')

    # Переключаемся на iframe
    iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_element)

    # Извлекаем HTML содержимое из iframe
    iframe_content = driver.page_source
    el=driver.find_elements(By.TAG_NAME,'li')
    print(el[0].text)

#    print(iframe_content)