import requests
from bs4 import BeautifulSoup
url = 'https://parsinger.ru/4.8/8/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
combined_cell_data = [int(cell.text) for cell in soup.select('[colspan]') if cell.text.strip().isdigit()]
print(sum(combined_cell_data))