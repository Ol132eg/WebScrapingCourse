import time
from selenium import webdriver
from selenium.webdriver.common.by import By
current_time = time.time()
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    wrappers = browser.find_elements(By.CLASS_NAME, 'parent')
    for wrapper in wrappers:
        color_gray = wrapper.find_element(By.XPATH, "./textarea[1]").text
        new_color_text = int(color_gray)
        wrapper.find_element(By.XPATH, "./textarea[1]").clear()
        color_blue = wrapper.find_element(By.XPATH, "./textarea[2]").send_keys(f'{new_color_text}')
        verification_button = wrapper.find_element(By.TAG_NAME, 'button').click()
    verification_all_button = browser.find_element(By.ID, 'checkAll').click()
    result = browser.find_element(By.ID, 'congrats').text
    print(f'Наш конечный результат -это число:{result}.Выполнили задачу за {(time.time() - current_time):.4} сек.')
    time.sleep(15)


