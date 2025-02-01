import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'
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
    if category in category_counts:  # Проверяем, существует ли категория в словаре
        category_counts[category] += int(item['count'])

print(category_counts)
#----------------------------------------------------------------
#data = {}
#for item in response:
#    data[item["categories"]] = data.get(item["categories"], 0) + int(item["count"])
#print(data)
#----------------------------------------------------------------
#count1=0
#count2=0
#count3=0
#count4=0
#count5=0
#dict_card={}

#for item in response:
#    if item['categories']=='watch':
#        count1+=int(item['count'])
#        dict_card['watch']=count1
#    if item['categories'] == 'mobile':
#        count2 += int(item['count'])
#        dict_card['mobile'] = count2
#    if item['categories']=='mouse':
#        count3+=int(item['count'])
#        dict_card['mouse']=count3
#    if item['categories'] == 'hdd':
#        count4 += int(item['count'])
#        dict_card['hdd'] = count4
#    if item['categories']=='headphones':
#        count5 += int(item['count'])
#        dict_card['headphones'] = count5

#print(dict_card)


