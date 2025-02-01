import json
import requests
from bs4 import BeautifulSoup
result_json = []
with requests.Session() as session:

        # цикл перебирает страницы товаров в текущей категории (всего 32 страницы).
    for i in range(32):
        # Формируем URL для каждой страницы товара.
        url = f"https://parsinger.ru/html/mobile/2/2_{i + 1}.html"
        # Делаем HTTP-запрос к странице.
        response = session.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        for item in soup.find_all('div', class_='description'):
            name = item.find('p', id='p_header').text.strip()
            article = item.find('p', class_='article').text.split(':')[1].strip()
            stock = item.find('span', id='in_stock').text.split(':')[1].strip()
            price = item.find('span', id='price').text.strip()
            old_price = item.find('span', id='old_price').text.strip()
            link=f"https://parsinger.ru/html/mobile/2/2_{i + 1}.html"
            description = [value.text.split(':')[1].strip() for value in item.find_all('li')]
            dict = {
        "categories": "mobile",
        "name": name,
        "article": article,
        "description": {
            "brand": description[0],
            "model": description[1],
            "type": description[2],
            "material": description[3],
            "type_display": description[4],
            "diagonal": description[5],
            "size": description[6],
            "weight": description[7],
            "resolution": description[8],
            "site": description[9]
        },
        "count": stock,
        "price": price,
        "old_price": old_price,
        "link": link
}
            result_json.append(dict)
    with open('res3.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)