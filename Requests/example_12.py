import requests

# Диапазон страниц
base_url = "https://parsinger.ru/3.3/4/"
start_page = 1
end_page = 100

# Переменные для хранения первой и последней доступных страниц
first_available = None
last_available = None

# Перебор страниц в заданном диапазоне
for page in range(start_page, end_page + 1):
    url = f"{base_url}{page}.html"
    response = requests.get(url)

    if response.status_code == 200:
        if first_available is None:
            first_available = f"{page}.html"
        last_available = f"{page}.html"

# Вывод результатов
print(f"Первая доступная страница: {first_available}")
print(f"Последняя доступная страница: {last_available}")
