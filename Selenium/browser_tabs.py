import time
from selenium.webdriver import Chrome
pages = ["http://parsinger.ru/blank/0/1.html",
         "http://parsinger.ru/blank/0/2.html",
         "http://parsinger.ru/blank/0/3.html",
         "http://parsinger.ru/blank/0/4.html",
         "http://parsinger.ru/blank/0/5.html",
         "http://parsinger.ru/blank/0/6.html"
         ]
with Chrome() as browser:
    for page in pages:
        browser.switch_to.new_window("tab")
        browser.get(page)
    time.sleep(2)
    for page in browser.window_handles:
        browser.switch_to.window(page)
        time.sleep(1)
        # Получаем title вкладки
        title = browser.execute_script("return document.title;")
        print(title, page)