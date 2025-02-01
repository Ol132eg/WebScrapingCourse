import requests
from requests.adapters import HTTPAdapter

# Создаем сессию
session = requests.Session()

# Создаем адаптер с конфигурацией по умолчанию
adapter = HTTPAdapter(pool_connections=10, pool_maxsize=20)

# Монтируем адаптер для HTTP и HTTPS
session.mount('http://', adapter)
session.mount('https://', adapter)

# Теперь можно делать запросы через эту сессию
response = session.get('https://httpbin.org/get')
print(response.status_code)  # 200