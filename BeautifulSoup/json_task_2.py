import json
import requests
from bs4 import BeautifulSoup
result_json = []
for i in range(4):
    url = f'https://parsinger.ru/html/index4_page_{i+1}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.find_all('div', class_='item'):
        name = item.find('a', class_='name_item').text.strip()
        price = item.find('p', class_='price').text
        description = [value.text.split(':')[1].strip() for value in item.find_all('li')]
        dict_ = {
            'Наименование': name,
            'Бренд': description[0],
            'Форм-фактор': description[1],
            'Ёмкость': description[2],
            'Объем буферной памяти': description[3],
            'Цена': price
        }
        result_json.append(dict_)
    with open('res1.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)