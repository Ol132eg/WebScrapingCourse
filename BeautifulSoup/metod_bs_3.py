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

    prices = soup.find_all('p',class_='price product_price')

    count = 0
    for price in prices:
        count+=int(price.text.replace(' ','').strip('руб'))

    return count

print(get_html(html))