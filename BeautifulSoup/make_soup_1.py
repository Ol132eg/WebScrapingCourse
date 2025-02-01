from bs4 import BeautifulSoup
import requests
import lxml

# Пример 3. Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding= 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
tag = soup.li
print(type(tag))
print(tag)
print(tag.attrs)
print(tag.string)
