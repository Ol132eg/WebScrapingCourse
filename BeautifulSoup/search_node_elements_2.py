from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'
html = response.text
print (html)



soup = BeautifulSoup(html, 'lxml')



old_price = float(soup.find('span', id='old_price').text.split(' ')[0])

print(old_price)
price =float(soup.find('span', id='price').text.split(' ')[0])
print(price)
result = ((old_price-price)/old_price)*100
print(round(result,1))



