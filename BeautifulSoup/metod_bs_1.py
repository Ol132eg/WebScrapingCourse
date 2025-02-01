from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://parsinger.ru/4.1/1/index2.html'
with open('index2.html', 'wb') as f:
    response = requests.get(url)
    f.write(response.content)
with open('index2.html', 'r',encoding='utf-8') as f:
    html = f.read()

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find('li', {
    'class': ['description_detail', 'class1','class2','class3'],
    'data-fdg45': 'value13',
    'data-54dfg60': 'value14',
    'data-d6f50hg': 'value15'
})

    print(tag.text)


get_html(html)