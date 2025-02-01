import requests
for i in range(1,161):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')

    with open(f'{i}.png', 'wb') as file:
        file.write(response.content)