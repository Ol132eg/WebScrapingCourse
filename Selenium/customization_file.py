import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)