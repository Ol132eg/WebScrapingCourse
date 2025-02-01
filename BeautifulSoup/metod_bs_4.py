from bs4 import BeautifulSoup
import requests
import lxml
url = 'https://parsinger.ru/4.1/1/index5.html'
with open('index5.html', 'wb') as f:
    response = requests.get(url)
    f.write(response.content)
with open('index5.html', 'r',encoding='utf-8') as f:
    html = f.read()

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
#    emls = soup.find_all(class_='email_field')
#    emails =[eml.text.strip().replace('Электронная почта: ','') for eml in emls]
#    return emails

    results = []
    emails = soup.select(".email_field strong")
    for email in emails:
        results.append(email.next_sibling.strip())

    return results

print(get_html(html))