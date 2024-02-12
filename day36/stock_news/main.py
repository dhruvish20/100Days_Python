import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "X99ULJ8R1W9ZKZVD"
NEWS_API_KEY = "7fd31339f7f34a59b90294371d53e5d6"

TWILIO_SID = "AC6ba7083ba575be412db24f384ff29b43"
TWILIO_AUTH = "eac23de39f586293c0aa040bd34287e4"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT , params= stock_params)
data = stock_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_data = data_list[1]["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data))
difference_percentage = (difference/float(yesterday_closing_price)) * 100

if difference_percentage > 2:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT , params= news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_article = [f"Headline : {article['title']} , Description : {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for articles in formatted_article:
        message = client.messages \
                    .create(
                            body=articles,
                            from_='+16592700876',
                            to='+918141230876'
                        )




