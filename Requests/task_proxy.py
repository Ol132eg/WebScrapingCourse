import requests
from itertools import cycle

# Список прокси
proxies_list = [
    {'http': 'http://61.216.156.222:60808', 'https': 'http://35.178.104.4:1080'}
]

proxy_pool = cycle(proxies_list)

url = "https://jsoneditoronline.org/#right=local.jexupu&left=local.zuseti"

# Создание сессии
session = requests.Session()

for i in range(1, 6):  # Попробуем сделать 5 запросов
    proxy = next(proxy_pool)
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")