import requests
from datetime import datetime
import smtplib
import time

my_email = "colabmachine99@gmail.com"
password = "hxjxepeqogmuooti"
MY_LAT = 21.170240,
MY_LNG = 72.831062

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng" : MY_LNG,
        "formatted" : 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json" , params= parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    times = (sunrise, sunset)
    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email , password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs= "parekhdhruvish1331@gmail.com",
                                msg= "Subject:Look UP!!!\n\nThe ISS is above you in the sky!!")