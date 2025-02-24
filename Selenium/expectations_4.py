from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH',
    'axhUiw2I','jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    for id_to_find in ids_to_find:
        locator = (By.ID, id_to_find)
        block =WebDriverWait(browser, 100,0.1).until(EC.visibility_of_element_located(locator))
        block.click()
    alert_text=browser.switch_to.alert.text
    print(alert_text)