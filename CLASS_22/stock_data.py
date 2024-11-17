import requests
from requests.exceptions import HTTPError

def get_stock_data():
    url = "https://www.alphavantage.co/query"

    try:
        #QUERY PARAMETERS
        response = requests.get(url, params={
            "function": "TIME_SERIES_INTRADAY",
            "symbol": "IBM",
            "interval": "5min",
            "outputsize": "full",
            "apikey": "1JUUH8N0UKWKIDA7"
        })

        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            price = data["Time Series (5min)"][last_refreshed]["1. open"]

            return price

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return None

stock_price = {}
price = get_stock_data()
symbol ='IBM'
if price:
    stock_price[symbol] = price

print(f"{symbol}: {price}")


