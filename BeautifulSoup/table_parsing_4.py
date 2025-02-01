import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
orange = soup.find('table').find_all(class_='orange')
blue = soup.select('td:last-child')
x=[float(row.text) for row in orange]
y=[float(row.text) for row in blue]
print(sum(map(lambda a, b: a*b,x,y)))
