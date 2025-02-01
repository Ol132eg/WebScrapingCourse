import csv
import requests
from bs4 import BeautifulSoup

# Создаем и открываем CSV файл для записи данных.
with open('res7.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    # Записываем заголовки столбцов в первый ряд файла.
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',
                     'Ссылка на карточку с товаром'])

# Словарь для соответствия индексов категорий и их названий.
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}

errors_occurred = False  # Флаг для отслеживания ошибок.
data_added = False  # Флаг для проверки добавления данных.

# Используем сессию для повторного использования соединений.
with requests.Session() as session:
    # Внешний цикл перебирает категории товаров (всего 5 категорий).
    for i in range(5):
        # Вложенный цикл перебирает страницы товаров в текущей категории (всего 32 страницы).
        for j in range(32):
            try:
                # Формируем URL для каждой страницы товара.
                url = f"https://parsinger.ru/html/{index_labels[i + 1]}/{i + 1}/{i + 1}_{j + 1}.html"

                # Делаем HTTP-запрос к странице.
                response = session.get(url, timeout=10)
                response.raise_for_status()  # Проверяем статус ответа.
                response.encoding = 'utf-8'

                # Парсим HTML-код страницы с помощью BeautifulSoup.
                soup = BeautifulSoup(response.text, 'lxml')

                # Извлекаем данные о товаре из соответствующих элементов HTML.
                name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
                article = [x.text.split(':')[1].strip() for x in soup.find_all('p', class_='article')]
                brand_model = [(x.text.split(':')[1].strip(), y.text.split(':')[1].strip()) for x, y in
                               zip(soup.find_all('li', id='brand'), soup.find_all('li', id='model'))]
                stock = [x.text.split(':')[1].strip() for x in soup.find_all('span', id='in_stock')]
                price = [x.text for x in soup.find_all('span', id='price')]
                old_price = [x.text for x in soup.find_all('span', id='old_price')]
                link_card = [product_card for product_card in [url]]  # Ссылка на текущую страницу товара.

                # Проверяем, извлечены ли данные.
                if not (name and article and brand_model and stock and price and old_price):
                    raise ValueError("Данные извлечены не полностью")

                # Открываем CSV файл для дозаписи данных.
                with open('res7.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    # Объединяем извлеченные данные в строки и записываем их в файл.
                    for name, article, (brand, model), stock, price, old_price, link_card in zip(name, article,
                                                                                                 brand_model, stock,
                                                                                                 price, old_price,
                                                                                                 link_card):
                        flatten = name, article, brand, model, stock, price, old_price, link_card
                        writer.writerow(flatten)
                        data_added = True

            except requests.exceptions.RequestException as e:
                errors_occurred = True
                print(f"Ошибка подключения к {url}: {e}")
            except (IndexError, AttributeError, ValueError) as e:
                errors_occurred = True
                print(f"Ошибка обработки данных на странице {url}: {e}")

# Сообщаем пользователю об итогах выполнения.
if data_added:
    print('Файл res7.csv создан и заполнен данными.')
else:
    print('Файл res7.csv создан, но данных не добавлено.')

if errors_occurred:
    print('Во время выполнения возникли ошибки. Проверьте вывод выше.')
