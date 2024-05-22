from bs4 import BeautifulSoup
with open('index.html', 'r', encoding="UTF-8") as f:
    src = f.read()

soup = BeautifulSoup(src, "lxml")

# Метод работы с заголовком
title = soup.title

# Методы find/find_all

test = soup.find_all('a')


for i in test:
    print(i)
