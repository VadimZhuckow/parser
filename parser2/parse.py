from bs4 import BeautifulSoup
with open('index.html', 'r', encoding="UTF-8") as f:
    src = f.read()

soup = BeautifulSoup(src, "lxml")

# Метод работы с заголовком
title = soup.title

# Методы find/find_all
# Парсим все ссылки с html дока
all_lin_in_html = soup.find_all('a')
# Объект возвращает список, поэтому перебираем его циклом и забираем только текст
for link in all_lin_in_html:
    print(link.text)
# Поиск по классам
user_name = soup.find('div', class_='user__name')
print(user_name.text.strip())

# Поиск по классу и тегу который лежит в классе
user_info_all = soup.find('div', class_='user__info').find_all('span')
for item in user_info_all:
    print(item.text)

print(user_info_all[0].text)  #В ответ пришел список, можно искользовать методы списка


# Поиск всех ссылок на странице
all_link = soup.find_all('a')

# Перебор всех ссылок, вывод текста и ссылки по ключу объекта href
for i in all_link:
    print(f'{i.text} : {i.get("href")}')



