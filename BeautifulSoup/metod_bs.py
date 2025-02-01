from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/4.1/1/index3.html'
with open('index3.html', 'wb') as f:
    response = requests.get(url)
    f.write(response.content)
with open('index3.html', 'r',encoding='utf-8') as f:
    html = f.read()


def get_html(html):

    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})

    print(tag.text)


get_html(html)