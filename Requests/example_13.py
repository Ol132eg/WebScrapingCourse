import requests

# Отправляем GET-запрос
r = requests.get('https://parsinger.ru/3.4/2/index.html')
r.encoding = 'utf-8'
# Получаем текст ответа
print("Текущая кодировка:", r.encoding)
print("Содержимое ответа:")
print(r.text)