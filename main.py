from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://sunlight.net/catalog').text

soup = LxmlSoup(html)

links = soup.find_all('a', class_='cl-item-link js-cl-item-link js-cl-item-root-link')
with open('catalog.txt', 'w', encoding="UTF-8") as f:
    for i, link in enumerate(links):
        url = link.get("href")  # получаем ссылку товара
        name = link.text()  # извлекаем наименование из блока со ссылкой
        price = soup.find_all("div", class_="cl-item-info-price-discount")[i].text()
        f.write(f"""
         id - {i}
         Url - {url}
         Name - {name}
         Price - {price}\n
         """)
