import requests
from random import choice

url = 'http://httpbin.org/user-agent'
#использование списка различных User-Agent из заранее созданного файла и их случайный выбор при каждом запросе
with open('../user_agent_.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)