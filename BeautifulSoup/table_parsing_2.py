import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/2/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[1:]
print(rows)
b=[]
for row in rows:
    cols = row.find_all('td')
    c=[float(col.text.strip()) for col in cols]
    b.append(c[0])
print(sum(b))