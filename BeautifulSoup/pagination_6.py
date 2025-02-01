import requests
from bs4 import BeautifulSoup
session = requests.Session()
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
product_adreses = []
for i in range(5):
    for j in range(32):
        product_adreses.append(f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html")
SummaProductS = 0
for x in product_adreses:
    response = session.get(url=x)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    SummaProduct = int(soup.find('span', {'id':'in_stock'}).text.split()[-1])*int(soup.find('span', {'id': 'price'}).text.split()[0])
    SummaProductS += SummaProduct
print(f'Сумма всех товаров {SummaProductS}')