import requests

url = 'https://parsinger.ru/4.6/1/res.json'
response = requests.get(url).json()
category_counts = {
    'watch': 0,
    'mobile': 0,
    'mouse': 0,
    'hdd': 0,
    'headphones': 0
}
for item in response:
    category = item['categories']
    if category in category_counts:
        total_count=int(item['article'])*item['description']['rating']
        category_counts[category] += total_count

print(category_counts)