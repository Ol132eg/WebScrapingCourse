import requests
def count_messages_by_user(json_data, user_count):

    username = json_data.get("username", "")
    # Увеличиваем счетчик для данного пользователя
    if username in user_count:
        user_count[username] += 1
    else:
        user_count[username] = 1

    # Если есть вложенные комментарии, обрабатываем их рекурсивно
    if "comments" in json_data:
        for comment in json_data["comments"]:
            count_messages_by_user(comment, user_count)

def sort_dict_by_value(input_dict):

    # Сортировка по убыванию значения, а затем по возрастанию ключа
    sorted_dict = {k: v for k, v in sorted(input_dict.items(), key=lambda item: (-item[1], item[0]))}
    return sorted_dict

data = requests.get('https://parsinger.ru/3.4/3/dialog.json').json()

# Инициализация словаря для подсчета сообщений
user_count = {}

# Подсчет сообщений
count_messages_by_user(data, user_count)

# Сортировка и вывод результатов
sorted_user_count = sort_dict_by_value(user_count)
print(sorted_user_count)