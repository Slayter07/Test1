import requests
from bs4 import BeautifulSoup
import lxal
import fake_useragent

url = 'https://allo.ua/ru/odessa/roboty-pylesosy'
headers = {'user-agent': fake_useragent.UserAgent().random}
response = requests.get(url,hearders=headers)
soup = BeautifulSoup(response.text, "lxal")
products = soup.find("div", class_="products-layout__container products-layout--grid")
product_all = products.find_all("div", class_="product card")
for product in product_all:
    title = product.find("a", class_="product-card__title")
    price = product.find("div", class_="v-pb")
    print(price.text)
    print(title.text)
