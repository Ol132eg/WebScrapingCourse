from bs4 import BeautifulSoup
from bs4.element import Tag #просто для обозначения типа элемента
from fake_useragent import UserAgent
import csv, lxml, requests

url = "https://parsinger.ru/html/index3_page_2.html"
header = {"user-agent": UserAgent().chrome}

response = requests.get(url, headers=header); response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

def get_data(str: Tag) -> list:
    """Собираем данные и возвращаем готовый список-строку, для одного товара"""
    name = str.find('a', {"class": "name_item"}).text
    price = str.find("p", {"class": "price"}).text
    brand, type_, connection, purpose = [i.text for i in str.find_all("li",)]
    return [name, price, brand, type_, connection, purpose]
# создаем список для строк с первой строкой
result = [["Наименовани", "Цена", "Бренд", "Тип", "Подключение", "Назначение"]]
# добавляем строки с информацией о товарах
for i in soup.find_all("div", {"class": "item"}):
    result.append(get_data(i))

with open("res1.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(result) # записываем все строки в файл сразу