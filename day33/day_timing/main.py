import requests
from datetime import datetime

parameters = {
    "lat": 21.170240,
    "lng" : 72.831062,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json" , params= parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

times = (sunrise.split("T")[1].split(":")[0], sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
# print(time_now)
print(times)