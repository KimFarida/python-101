# Scrape https://books.toscrape.com/
# book title, price, availability, image, category, rating
from unicodedata import category

main_url = 'https://books.toscrape.com/'
#Warm Up
import requests
from bs4 import BeautifulSoup

def getAndParseURL(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return soup


def getBooksURLS(url):
    soup = getAndParseURL(main_url)

    product_pods = soup.findAll("article", class_="product_pod")
    book_links = []

    for product_pod in product_pods:
        link = main_url + product_pod.div.a.get("href")
        book_links.append(link)

    return book_links

# all_books = getBooksURLS(main_url)
# print(all_books)

def getCategoryURLS(url):
    soup = getAndParseURL(main_url)

    categories = soup.find("ul", class_= "nav nav-list").findAll("li")[1:]
    category_urls = []

    for category in categories:
        temp = main_url + category.a.get("href")
        category_urls.append(temp)

    return category_urls

print(getCategoryURLS(main_url))


