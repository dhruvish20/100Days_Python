import smtplib

my_email = "colabmachine99@gmail.com"
password = "hxjxepeqogmuooti"
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user= my_email , password= password)
connection.sendmail(from_addr= my_email , 
                    to_addrs= "parekhdhruvish1331@gmail.com" ,
                    msg= "Subject: Hello\n\n this is the body part" 
)
connection.close()