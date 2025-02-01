import json
import requests
from bs4 import BeautifulSoup
result_json = []

for i in range(5):
    for j in range(4):
        # Формируем URL для каждой страницы товара.
        url = f'https://parsinger.ru/html/index{i+1}_page_{j+1}.html'
        # Делаем HTTP-запрос к странице.
        response = requests.get(url)
        response.encoding = 'utf-8'
        # Парсим HTML-код страницы с помощью BeautifulSoup.
        soup = BeautifulSoup(response.text, 'lxml')
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        for item in soup.find_all('div', class_='item'):
            name = item.find('a', class_='name_item').text.strip()
            price = item.find('p', class_='price').text
            description = dict(map(str.strip, tag.text.split(':')) for tag in item.find_all('li'))
            result_json.append({"Наименование": name} | description | {"Цена": price})
with open('res2.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)