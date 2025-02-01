from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/4.1/1/index4.html'
with open('index4.html', 'wb') as f:
    response = requests.get(url)
    f.write(response.content)
with open('index4.html', 'r',encoding='utf-8') as f:
    html = f.read()

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('a',href=True,class_=True)
    for tag in tags:
        print(tag.text.strip())  # Извлеките текст и обрежьте лишние пробелы

get_html(html)