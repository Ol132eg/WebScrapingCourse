import requests

try:
    response = requests.get('https://httpstat.us/200')
    data = response.json()
except (requests.JSONDecodeError, requests.Timeout, requests.ReadTimeout) as e:
    print(f"Перехвачено исключение типа: {type(e).__name__}")
    print(f"Сообщение об ошибке: {str(e)}")