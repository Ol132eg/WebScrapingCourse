import csv
import requests
from bs4 import BeautifulSoup

with open('res4.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
    'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])

for i in range(1, 33):
    url = f'https://parsinger.ru/html/watch/1/1_{i}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
    article = [x.text.split(':')[1].strip() for x in soup.find_all('p', class_='article')]
    description = [x.text.split('\n') for x in soup.find_all('ul', id='description')]
    stock = [x.text.split(':')[1].strip() for x in soup.find_all('span', id='in_stock')]
    price = [x.text for x in soup.find_all('span', id='price')]
    old_price = [x.text for x in soup.find_all('span', id='old_price')]
    link_card = [product_card for product_card in [url]]
    with open('res4.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for name, article,description,stock,price,old_price,link_card in zip(name, article,description,stock,price,old_price,link_card):
            flatten = name, article, *[x.split(':')[1].strip() for x in description if x],stock,price,old_price,link_card
            writer.writerow(flatten)
print('Файл res4.csv создан')