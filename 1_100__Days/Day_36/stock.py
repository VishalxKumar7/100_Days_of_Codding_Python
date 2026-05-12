import requests
import os
from dotenv import load_dotenv

load_dotenv()

stock_api_key = os.environ.get("VINTAGE_API_KEY")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_close_price)


difference = round(abs(float(yesterday_closing_price) - float(day_before_yesterday_close_price)), 2)
print(difference)

diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
print(diff_percent)

if diff_percent > 5:
    print("Get News")