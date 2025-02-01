from bs4 import BeautifulSoup
import requests
import lxml
with open('index_1.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    print(soup2)