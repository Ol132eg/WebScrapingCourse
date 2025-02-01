import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/4.8/7/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
#table = soup.find_all('table')
#count=0
#for row in table:
#    c = [float(col.text.strip()) for col in row.find_all('td') if float(col.text.strip()) %3 ==0]
#    for i in c:
#         count+=i
#print(count)
result = 0
for tag in soup.select("table tr td"):
    number = int(tag.text)
    if number % 3 == 0:
        result += number

print(result)

