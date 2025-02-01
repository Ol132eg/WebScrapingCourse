import requests
total_sum=0
for page_number in range(1,201):
    url=f'https://parsinger.ru/3.3/2/{page_number}.html'
    try:
        response=requests.get(url,timeout=5)
        total_sum+=response.status_code
    except requests.RequestException as e:
        print(f'Ошибка при {url}: {e}')
print(total_sum)