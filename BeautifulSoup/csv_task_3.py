import csv
import requests
from bs4 import BeautifulSoup

with open('res3.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
url_chunks = (tag['href'] for tag in soup.find('div', {'class': 'pagen'}).find_all('a'))
for c in url_chunks:
    response = requests.get(url=f'https://parsinger.ru/html/{c}')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')


    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]

    with open('res3.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item, descr,price in zip(name,description, price):

            flatten = item, *[x.split(':')[1].strip() for x in descr if x],price
            writer.writerow(flatten)

print('Файл res3.csv создан')