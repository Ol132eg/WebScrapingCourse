import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/temp/index.html')
    text_fields =browser.find_elements(By.CSS_SELECTOR, '.field.active-field')
    results =0
    for checkbox_states in text_fields:
        number=int(checkbox_states.get_attribute('value'))
        results+=number
    print(f'Сумма чисел: {results}. Время выполнения {(time.time() - current_time):.3} сек.')
    time.sleep(5)




#        print(checkbox_states.is_selected())

#        print(checkbox_states.get_attribute('field active-field'))

