import requests
import time

url = 'http://example.com/pages/'


# Создание объекта сессии
session = requests.Session()

# Измерение времени выполнения запросов с использованием сессии
start_time = time.time()
for i in range(1000, 1050):
    resp = session.get(url + str(i))
end_time = time.time()
print(f'Время выполнения с использованием сессии: {end_time - start_time}')

# Измерение времени выполнения запросов без использования сессии
start_time = time.time()
for i in range(1000, 1050):
    response = requests.get(url + str(i))
end_time = time.time()
print(f'Время выполнения без использования сессии: {end_time - start_time}')

# использование контекстного менеджера для управления сессией
start_time = time.time()
with requests.Session() as session:
    for i in range(1000, 1050):
        resp = session.get(url + str(i))
end_time = time.time()
print(f'Время выполнения с использованием контекстного менеджера для управления сессией: {end_time - start_time}')