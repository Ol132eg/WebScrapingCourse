from bs4 import BeautifulSoup
import requests
import lxml
with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')    # file: Файловый объект на уровне Python (файловый дескриптор), предоставляющий более
    #удобный и высокоуровневый интерфейс для работы с файлом.
    # parser: str  # Название парсера (строка)
    print("Анализ файла с использованием менеджера контекста:\n", soup2)