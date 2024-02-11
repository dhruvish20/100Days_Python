import requests
from twilio.rest import Client
import os

api_key = "Your API key"
account_sid = "AC6ba7083ba575be412db24f384ff29b43"
auth_token = "Your Auth key"


parampeter = {
    "lat":21.170240,
    "lon":72.831062,
    "cnt":4,
    "appid":api_key,
}

response = requests.get(url=f"http://api.openweathermap.org/data/2.5/forecast", params= parampeter)
response.raise_for_status()
data=response.json()
weather_id = data["list"][0]["weather"][0]["id"]


will_rain= False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code <= 800:
       will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                        body="ALERT , hehehe Tension mat le ye me hu",
                        from_='+16592700876',
                        to='+918141230876'
                    )





#
# print(message.sid)