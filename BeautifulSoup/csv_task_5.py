import csv
import requests
from bs4 import BeautifulSoup

with open('res5.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
for t in range(5):
    url = f'https://parsinger.ru/html/index{t + 1}_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'

    for i in range(4):
        url = f'https://parsinger.ru/html/index{t + 1}_page_{i + 1}.html'
        # Всегда можно проконтролировать через print() данные, которые вы получаете
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        with open('res5.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for name, descr, price in zip(name, description, price):
                flatten = name, *[x.split(':')[1].strip() for x in descr if x], price
                writer.writerow(flatten)

print('Файл res5.csv создан')
