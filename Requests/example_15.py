import requests
r = requests.get('https://parsinger.ru/3.4/1/json_weather.json')
data_sheet = r.json()
temp={}
for data in data_sheet:
    a=int(data['Температура воздуха'].split("°C")[0])
    temp[data['Дата']]=a
    min_temp_data =min(temp,key=temp.get)
print(min_temp_data)


