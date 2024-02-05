import smtplib
import datetime as dt
import os
import random

quotes_path = os.path.join(os.path.dirname(__file__), "quotes.txt")
my_email = "colabmachine99@gmail.com"
password = "hxjxepeqogmuooti"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 0:
    with open(quotes_path) as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email , password= password)
        connection.sendmail(from_addr=my_email , 
                                to_addrs= "solaceai20@gmail.com" ,
                                msg=f"Subject: Monday Motivation\n\n{quote}")


