from bs4 import BeautifulSoup
import requests

# Задаем URL-адрес веб-страницы для парсинга
url = 'http://parsinger.ru/html/index1_page_3.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем блок пагинации и извлекаем все вложенные ссылки
pagen = soup.find('div', class_='pagen').find_all('a')

# Инициализируем список для хранения абсолютных URL-адресов
#list_link = []

# Задаем схему URL-адреса, которая будет использоваться для преобразования относительных путей в абсолютные URL
schema = 'http://parsinger.ru/html/'

# Цикл по всем найденным ссылкам для преобразования их в абсолютные URL-адреса
#for link in pagen:
#    list_link.append(f"{schema}{link['href']}")
list_link = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
# Выводим на экран список абсолютных URL-адресов
print(list_link)