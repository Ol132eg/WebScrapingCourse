import csv
import requests
from bs4 import BeautifulSoup
# Создаем и открываем CSV файл для записи данных.
with open('res6.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # Записываем заголовки столбцов в первый ряд файла.
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель','Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'])
# Словарь для соответствия индексов категорий и их названий.
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
# Внешний цикл перебирает категории товаров (всего 5 категорий).
for i in range(5):
    # Внутренний цикл перебирает все страницы товаров в категории (всего 32 страницы).
    for j in range(32):
        # Формируем URL для каждой страницы товара.
        url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        # Делаем HTTP-запрос к странице.
        response = requests.get(url)
        response.encoding = 'utf-8'
        # Парсим HTML-код страницы с помощью BeautifulSoup.
        soup = BeautifulSoup(response.text, 'lxml')
        # Извлекаем данные о товаре из соответствующих элементов HTML.
        name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
        article = [x.text.split(':')[1].strip() for x in soup.find_all('p', class_='article')]
        brand = [x.text.split(':')[1].strip() for x in soup.find_all('li',id='brand')]
        model = [x.text.split(':')[1].strip() for x in soup.find_all('li',id='model')]
        stock = [x.text.split(':')[1].strip() for x in soup.find_all('span', id='in_stock')]
        price = [x.text for x in soup.find_all('span', id='price')]
        old_price = [x.text for x in soup.find_all('span', id='old_price')]
        link_card = [product_card for product_card in [url]]
        # Открываем CSV файл для дозаписи данных.
        with open('res6.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            # Объединяем извлеченные данные в строки и записываем их в файл.
            for name, article,brand,model,stock,price,old_price,link_card in zip(name, article,brand,model,stock,price,old_price,link_card):
                flatten = name, article,brand,model,stock,price,old_price,link_card
                writer.writerow(flatten)
# Сообщаем пользователю об успешном создании файла.
print('Файл res6.csv создан')