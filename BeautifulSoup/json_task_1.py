import json
import requests
from bs4 import BeautifulSoup

# 1 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

result_json = []
# 2 ------------------------------------------------------
for item in soup.find_all('div', class_='item'):
    name = item.find('a', class_='name_item').text.strip()
    price = item.find('p', class_='price').text
    description = [value.text.split(':')[1].strip() for value in item.find_all('li')]
    dict_ = {
        'name': name,
        'brand': description[0],
        'type': description[1],
        'connect': description[2],
        'game': description[3],
        'price': price
    }
    result_json.append(dict_)
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)