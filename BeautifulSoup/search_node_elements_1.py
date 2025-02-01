from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
html = response.text


soup = BeautifulSoup(html, 'lxml')

a=sum([int(price.text.split(' ')[0]) for price in soup.find_all('div', class_='price_box')])
print(a)