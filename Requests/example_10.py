import requests

for page_number in range(1,201):
    url=f'https://parsinger.ru/3.3/1/{page_number}.html'
    response = requests.get(url, timeout=1)

    if response.status_code == 200:
        print(f'Страница {page_number} загружена успешно',response.text)
    else:
        print(f'Ошибка загрузки страницы {page_number}, код ошибки: {response.status_code}')




