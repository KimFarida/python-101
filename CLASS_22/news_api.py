import requests
from requests.exceptions import HTTPError

API_KEY = "006a94d29e5446f98beb85490d8aea5a"
url = "https://newsapi.org/v2/top-headlines"
params={
    "country": "us",
    "category": "business",
    "apiKey": API_KEY
}

try:
    response = requests.get(url,params=params)
    data = response.json()

    for article in data['articles']:
        print(f'''
        Title : {article['title']}
        Author : {article['author']}
        URL : {article['url']}
        Published: {article['publishedAt']}
        
        ''')

except HTTPError as e:
    print("An HTTP ERROR OCCURRED", e)
except Exception as e:
    print("An error ocurred", e)

