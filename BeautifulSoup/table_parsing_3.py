import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/table/4/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
table_rows = soup.find('table').find_all(class_='green')
print(sum([float(row.text) for row in table_rows]))


