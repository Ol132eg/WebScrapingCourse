import json
import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# Словарь для соответствия индексов категорий и их названий.
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
result_json = list()
errors_occurred = False  # Флаг для отслеживания ошибок.
data_added = False  # Флаг для проверки добавления данных.

# Используем сессию для повторного использования соединений.
with requests.Session() as session:
    # Внешний цикл перебирает категории товаров (всего 5 категорий).
    for i in range(5):
        # Вложенный цикл перебирает страницы товаров в текущей категории (всего 32 страницы).
        for j in range(32):

            # Формируем link для каждой страницы товара.
            link = f"https://parsinger.ru/html/{index_labels[i + 1]}/{i + 1}/{i + 1}_{j + 1}.html"

            # Делаем HTTP-запрос к странице.
            response = session.get(url=link,headers=headers,timeout=10)
            response.encoding = 'utf-8'

            # Парсим HTML-код страницы с помощью BeautifulSoup.
            soup = BeautifulSoup(response.text, 'lxml')
            collector = dict()  # тут собираем данные с каждой категории
            name = soup.find('p', id='p_header').text
            article = soup.find('p', class_='article').text.split(':')[1].strip()
            description = {i['id']: i.text.split(':')[1].strip() for i in soup.find_all('li')}
            count = soup.find('span', id='in_stock').text.split(':')[1].strip()
            price = soup.find('span', id='price').text
            old_price = soup.find('span', id='old_price').text
            # добавляем данные
            collector['categories'] = index_labels[i + 1]
            collector['name'] = name
            collector['article'] = article
            collector['description'] = description
            collector['count'] = count
            collector['price'] = price
            collector['old_price'] = old_price
            collector['link'] = link
            result_json.append(collector)

    with open('res4.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
print('Файл res4.json создан и заполнен данными.')