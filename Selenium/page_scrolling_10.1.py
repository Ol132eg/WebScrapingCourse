import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start_time = time.time()

# Опции для Chrome
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')
options_chrome.add_argument('--disable-gpu')

# Запуск драйвера
with webdriver.Chrome(options=options_chrome) as driver:
    driver.get('https://parsinger.ru/selenium/5.7/4/index.html')

    # Ожидание загрузки контейнера
    wait = WebDriverWait(driver, 5)
    scroll_container = wait.until(EC.presence_of_element_located((By.ID, 'main_container')))

    # Автоматический скроллинг
    for _ in range(10):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
        time.sleep(0.1)  # Уменьшаем задержку, но оставляем для корректной подгрузки

    # Поиск элементов после загрузки всех данных
    elements = scroll_container.find_elements(By.TAG_NAME, 'input')

    # Фильтрация и клики по чётным значениям
    for i in tqdm(elements):
        if int(i.get_attribute('value')) % 2 == 0:
            i.click()

    # Ожидание и клик по кнопке
    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'alert_button')))
    button.click()

    # Ожидание появления alert и получение его текста
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()  # Закрываем alert

print(f'{alert_text}. Время выполнения: {(time.time() - start_time):.4f} сек')