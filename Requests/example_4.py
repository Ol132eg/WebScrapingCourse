# Импорт библиотеки
import requests

# Параметры запроса: ищем книги по программированию
params = {'text': 'WEB Парсинг на python'}

# Отправка запроса
response = requests.get('https://yandex.ru/search/', params=params)

# Вывод результатов
print(response.text)