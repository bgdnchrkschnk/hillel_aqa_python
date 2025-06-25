from bs4 import BeautifulSoup
import requests

# Завантаження HTML-сторінки
url = 'https://sinoptik.ua/'
response = requests.get(url)
html_content = response.content # html text

# Аналіз HTML-документу з використанням BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Вилучення тексту з тегу <title> за допомогою CSS-локатора
title = soup.select_one('a[href="/pohoda/odesa"]').text
print(title)



# xPath locators

xpath_home_locator = "//a[@class='btn']"
