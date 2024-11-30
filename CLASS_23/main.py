# Scrape https://books.toscrape.com/
# book title, price, availability, image, category, rating
import re
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

# print(getCategoryURLS(main_url))



# def getPageURLS(main_url, pages_url=[]):
#     if not pages_url:
#         pages_url = [main_url]
#
#     soup = getAndParseURL(pages_url[-1])
#
#     page_url = soup.find("li", class_="next")
#     page_url = page_url.a.get("href") if page_url else None
#
#
#     if not page_url:
#         return pages_url
#
#     pages_url.append(main_url + page_url)
#
#     return getPageURLS(main_url, pages_url)

# print(getPageURLS(main_url))


pages_urls = [main_url]

soup = getAndParseURL(pages_urls[0])

while len(soup.findAll("a", href=re.compile("page"))) == 2  or len(pages_urls) == 1:
    new_url = "/".join(pages_urls[-1].split("/")[:-1]) + "/" + soup.findAll("a", href=re.compile("page"))[-1].get(
        "href")
    pages_urls.append(new_url)

    soup = getAndParseURL(new_url)

print(str(len(pages_urls)) + " fetched URLs")
print("Some examples:")
print(pages_urls[:5])






