import smtplib
import random
import os
import datetime as dt
import pandas

my_email = "colabmachine99@gmail.com"
password = "hxjxepeqogmuooti"

today = dt.datetime.now()
today_tuple = (today.month , today.day)

data_path = os.path.join(os.path.dirname(__file__),"birthdays.csv")
data = pandas.read_csv(data_path)

birthday_dict = {(data_row["month"] , data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = os.path.join(os.path.dirname(__file__),"letter_templates", f"letter_{random.randint(1,3)}.txt")
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]" , birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com" , 587) as connection:
        connection.starttls()
        connection.login(user= my_email , password= password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg= f"Subject: HAPPY BIRTHDAY\n\n{contents}")